from openmdao.lib.casehandlers.api import JSONCaseRecorder, BSONCaseRecorder
from CADRE_mdp import CADRE_Optimization

print "setting up"
top = CADRE_Optimization(n=1500, m=300)
# Could also use JSONCaseRecorder but that would be 3 to 4 times the size
top.recorders = [BSONCaseRecorder('CADRE.bson')]

# Only include what we need for the post processing plots.
#   Otherwise the BSON file will be 15 times the size
includes = [ 'pt' + str(i) + '.Data' for i in range(6)]
includes.extend( [ "_pseudo_" + str(i) for i in range(30) ] ) # the constraints values are in psuedos
includes.append( "pt5.CP_gamma")
top.includes = includes
print "running"
top.run()
