from openmdao.main.api import Component
from openmdao.main.datatypes.api import Float, Array
from CADRE.CADRE_assembly import CADRE
from openmdao.lib.drivers.api import SLSQPdriver
import os
import pylab
import numpy as np


class NetGain(Component):

    """
    Computes the sum of an inputted gain array.
    """
    net = Float(iotype="out")

    def __init__(self, n):
        super(NetGain, self).__init__()
        self.n = n
        self.add('gain', Array(np.zeros(n), iotype='in', shape=(n,)))

    def execute(self):
        self.net = sum(self.gain)

    def list_deriv_vars(self):
        input_keys = ('gain', )
        output_keys = ('net', )
        return input_keys, output_keys

    def apply_derivT(self, arg, result):
        if 'gain' in result and 'net' in arg:
            result['gain'] += arg['net'] * np.ones(self.n)


n, m = 1500, 150
top = CADRE(n, m)

# orbit initial position and velocity
r_e2b_I0 = [-4969.91222,  4624.84149,
            1135.9414,  0.1874654, -1.62801666,  7.4302362]

# number of days since launch
LD = 5417.5

top.set("LD", LD)
top.set("r_e2b_I0", r_e2b_I0)

# Run model to get baseline net gain value
top.run()

obj1 = sum(top.Comm_GainPattern.gain)

# Add in optimization driver
top.add("driver", SLSQPdriver())

# top.add("NetGain", NetGain(n))
# top.driver.workflow.add("NetGain")

# top.connect("Comm_GainPattern.gain", "NetGain.gain")

top.driver.add_parameter("CP_gamma", low=0, high=np.pi / 2.)
# top.driver.add_objective("-NetGain.net")

top.driver.add_objective("-sum(Comm_GainPattern.gain)")

pylab.figure()
pylab.subplot(211)
pylab.title("Roll angle $\gamma$, Before optimization")
pylab.plot(top.CP_gamma)
pylab.ylabel("$\gamma$")

top.run()
obj2 = sum(top.Comm_GainPattern.gain)

pylab.subplot(212)
pylab.title("After optimization")
pylab.plot(top.CP_gamma)
pylab.ylabel("$\gamma$")
pylab.xlabel("time")

# pylab.show()

print "Net comm gain before optimization:", obj1
print "Net comm gain after optimization:", obj2
