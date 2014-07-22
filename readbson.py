import numpy as np
import pylab

from openmdao.lib.casehandlers.api import CaseDataset

def get_constraint_value_from_case( cds, case, constraint_name ):
    # can get at constraints using
    #    cds.simulation_info[ 'expressions' ] to get the pseudos that 
    #    have that value
    #      cds.simulation_info[ 'expressions' ]['pt1.ConS0 <= 0']
    #     equals
    #      {u'pcomp_name': u'_pseudo_7', u'data_type': u'Constraint'}
    return case[ cds.simulation_info[ 'expressions' ][constraint_name][ 'pcomp_name' ] ]

cds = CaseDataset("CADRE.bson", "bson")
vnames = cds.data.var_names().fetch()
cases = cds.data.driver("driver").fetch()
print "# cases", len(cases)

X, Y, Z = [], [], []
pcom = []


for case in cases:
    data = [ case['pt' + str(i) + '.Data'][0][1499] for i in xrange(6) ]
    sumdata = sum([float(i) for i in data if i])

    c1 = [get_constraint_value_from_case( cds, case, "pt" + str(i) + ".ConCh <= 0") for i in xrange(6)]
    c2 = [get_constraint_value_from_case( cds, case, "pt" + str(i) + ".ConDs <= 0") for i in xrange(6)]
    c3 = [get_constraint_value_from_case( cds, case, "pt" + str(i) + ".ConS0 <= 0") for i in xrange(6)]
    c4 = [get_constraint_value_from_case( cds, case, "pt" + str(i) + ".ConS1 <= 0") for i in xrange(6)]
    c5 = [get_constraint_value_from_case( cds, case, "pt" + str(i) + ".SOC[0][0] = pt" + str(i) + ".SOC[0][-1]") for i in xrange(6)]


    c1_f = sum([float(i) for i in c1 if i])
    c2_f = sum([float(i) for i in c2 if i])
    c3_f = sum([float(i) for i in c3 if i])
    c4_f = sum([float(i) for i in c4 if i])
    c5_f = sum([float(i) for i in c5 if i])

    feasible = [c1_f, c2_f,  c3_f, c4_f, c5_f]

    X.append(sumdata), Y.append(sum(feasible)), Z.append(feasible)

    pcom.append([float(case["pt5.CP_gamma"][i])for i in xrange(300)])

    # print sumdata, sum(feasible), max(feasible) #,[ '%.1f' % i for i in
    # feasible]
    print sumdata

pylab.figure()
pylab.plot(pcom[-1])

Z = np.array(Z)
if not len(Z):
    print "no data yet..."
    quit()
pylab.figure()
pylab.subplot(311)
pylab.title("total data")
pylab.plot(X, 'b')
pylab.plot([0, len(X)], [3e4, 3e4], 'k--', marker="o")
pylab.subplot(312)
pylab.title("Sum of Constraints")
pylab.plot([0, len(Y)], [0, 0], 'k--', marker="o")
pylab.plot(Y, 'k')
pylab.subplot(313)
pylab.title("Max of Constraints")
pylab.plot([0, len(Z)], [0, 0], 'k--')
pylab.plot(Z[:, 0], marker="o", label="c1")
pylab.plot(Z[:, 1], marker="o", label="c2")
pylab.plot(Z[:, 2], marker="o", label="c3")
pylab.plot(Z[:, 3], marker="o", label="c4")
pylab.plot(Z[:, 4], marker="o", label="c5")
pylab.legend(loc="best")

pylab.show()
