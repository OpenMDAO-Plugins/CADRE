import os.path
import numpy as np



from openmdao.main.api import Assembly
#from openmdao.lib.drivers.api import CONMINdriver


import warnings
try:
    from pyopt_driver import pyopt_driver
except ImportError:
    warnings.warn(
        "pyopt_driver must be installed to run the full CADRE optimization",
        ImportWarning)

from openmdao.main.test.simpledriver import SimpleDriver


from CADRE.CADRE_assembly import CADRE


class CADRE_Optimization(Assembly):

    def __init__(self, n=1500, m=300, npts=6):
        super(CADRE_Optimization, self).__init__()

        # add SNOPT driver
        # self.add("driver", pyopt_driver.pyOptDriver())
        # self.driver.optimizer = "SNOPT"
        # self.driver.options = {'Major optimality tolerance': 1e-3,
        #                        'Iterations limit': 500000000,
        #                        "New basis file": 10}
        # if os.path.exists("fort.10"):
        #     self.driver.options["Old basis file"] = 10

        #driver = self.add("driver", CONMINdriver())
        self.add("driver", SimpleDriver())


        # Raw data to load
        fpath = os.path.dirname(os.path.realpath(__file__))
        fpath = os.path.join(fpath, 'src/CADRE/data')
        solar_raw1 = np.genfromtxt(fpath + '/Solar/Area10.txt')
        solar_raw2 = np.loadtxt(fpath + '/Solar/Area_all.txt')
        comm_rawGdata = np.genfromtxt(fpath + '/Comm/Gain.txt')
        comm_raw = (10 ** (comm_rawGdata / 10.0)
                    ).reshape((361, 361), order='F')
        power_raw = np.genfromtxt(fpath + '/Power/curve.dat')

        # Load launch data
        launch_data = np.loadtxt(fpath + '/Launch/launch1.dat')

        # orbit position and velocity data for each design point
        r_e2b_I0s = launch_data[1::2, 1:]

        # number of days since launch for each design point
        LDs = launch_data[1::2, 0] - 2451545

        # build design points
        names = ['pt%s' % i for i in range(npts)]
        for i, name in enumerate(names):
            comp = self.add(name, CADRE(n, m, solar_raw1, solar_raw2,
                                        comm_raw, power_raw))
            self.driver.workflow.add(name)
            comp.set("LD", LDs[i])
            comp.set("r_e2b_I0", r_e2b_I0s[i])

            # add parameters to driver
            self.driver.add_parameter("%s.CP_Isetpt" % name, low=0., high=0.4)
            self.driver.add_parameter("%s.CP_gamma" %
                                      name, low=0, high=np.pi / 2.)
            self.driver.add_parameter("%s.CP_P_comm" % name, low=0., high=25.)
            self.driver.add_parameter("%s.iSOC[0]" % name, low=0.2, high=1.)

            # add constraints
            self.driver.add_constraint("%s.ConCh <= 0" % name)
            self.driver.add_constraint("%s.ConDs <= 0" % name)
            self.driver.add_constraint("%s.ConS0 <= 0" % name)
            self.driver.add_constraint("%s.ConS1 <= 0" % name)
            self.driver.add_constraint(
                "%s.SOC[0][0] = %s.SOC[0][-1]" % (name, name))

        # add parameter groups
        cell_param = ["%s.cellInstd" % name for name in names]
        self.driver.add_parameter(cell_param, low=0, high=1)

        finangles = ["%s.finAngle" % name for name in names]
        self.driver.add_parameter(finangles, low=0, high=np.pi / 2.)

        antangles = ["%s.antAngle" % name for name in names]
        self.driver.add_parameter(antangles, low=-np.pi / 4, high=np.pi / 4)

        # add objective
        obj = ''.join(["-%s.Data[0][-1]" % name for name in names])
        self.driver.add_objective(obj)
