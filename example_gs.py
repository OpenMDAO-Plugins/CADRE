from openmdao.lib.casehandlers.api import JSONCaseRecorder, BSONCaseRecorder
from openmdao.main.api import Component
from openmdao.main.datatypes.api import Float
from CADRE_mdp import CADRE_Optimization
import urllib
import json
import numpy as np


class Elevation(Component):

    """
    Computes elevation with respect to mean sea level on Earth at a given
    latitude and longitude.

    Uses google maps API.
    """

    lon = Float(-83.7264, iotype="in", units="deg", descr="Longitude")
    lat = Float(42.2708, iotype="in", units="deg", descr="Latitude")
    alt = Float(0.256, iotype="out", units="km", descr="Elevation")

    lon_ = Float(-83.7264, iotype="out")
    lat_ = Float(42.2708, iotype="out")

    def __init__(self):
        super(Elevation, self).__init__()
        self.J = np.zeros(2)
        self.resolution = 0.001

    def execute(self):
        self.lat_ = self.lat
        self.lon_ = self.lon
        lt1 = self.lat
        ln1 = self.lon
        lt2 = self.lat + self.resolution
        ln2 = self.lon
        lt3 = self.lat
        ln3 = self.lon + self.resolution
        try:
            url = "http://maps.googleapis.com/maps/api/elevation/json?locations=%s,%s|%s,%s|%s,%s&sensor=false" % (
                str(lt1), str(ln1), str(lt2), str(ln2), str(lt3), str(ln3))
            response = ''.join(urllib.urlopen(url).readlines())
            data = json.loads(response)

            self.alt = float(data["results"][0]["elevation"]) / 1000.

            e1 = float(data["results"][1]["elevation"]) / 1000.
            e2 = float(data["results"][2]["elevation"]) / 1000.

            self.J[0] = (e1 - self.alt) / self.resolution
            self.J[1] = (e2 - self.alt) / self.resolution
        except:
            pass

    def list_deriv_vars(self):
        """Provide full Jacobian."""

        input_keys = ('alt')
        output_keys = ('lat', 'lon')

        return input_keys, output_keys

    def provideJ(self):
        pass

    def apply_deriv(self, arg, result):
        if "alt" in result:
            if "lat" in arg:
                result["arg"] += self.J[0] * arg["lat"]
            if "lon" in arg:
                result["arg"] += self.J[1] * arg["lon"]

    def apply_derivT(self, arg, result):
        if "alt" in arg:
            if "lat" in result:
                result["lat"] += self.J[0] * arg["alt"]
            if "lon" in result:
                result["lon"] += self.J[1] * arg["alt"]

print "setting up"
top = CADRE_Optimization(n=1500, m=300)
top.add("Elevation", Elevation())
top.driver.workflow.add("Elevation")
for i in xrange(6):
    top.connect("Elevation.alt", "pt%s.alt" % str(i))
lons = ["pt" + str(i) + ".lon" for i in xrange(6)] + ["Elevation.lon"]
lats = ["pt" + str(i) + ".lat" for i in xrange(6)] + ["Elevation.lat"]
top.driver.add_parameter(lons, low=-180, high=180)
top.driver.add_parameter(lats, low=-90, high=90)

top.recorders = [JSONCaseRecorder('CADRE_gs.json')]
includes = [ 'pt' + str(i) + '.Data' for i in range(6)]
includes.extend( [ "_pseudo_" + str(i) for i in range(30) ] )
includes.append( "Elevation.alt")
top.includes = includes
print "running"
top.run()
