
import unittest
import numpy as np

from openmdao.main.api import Assembly, set_as_top
from openmdao.lib.datatypes.api import Float, Array
from openmdao.util.testutil import assert_rel_error

from CADRE.rk4 import RK4


class RKTest(RK4):

    ''' Simple case with 2 states, 2 time points, and a 2-wide time-invariant
    input'''

    def __init__(self, n_times):
        super(RKTest, self).__init__()

        self.add("yi", Array(np.zeros((2, 3)), iotype='in'))
        self.add("yv", Array(np.zeros((2, n_times)), iotype='in'))

        self.add("x", Array(np.zeros((2, n_times)), iotype='out'))
        self.add("x0", Array(np.array([1.6, 2.7]), iotype='in'))

        self.state_var = "x"
        self.init_state_var = "x0"
        self.external_vars = ["yv"]
        self.fixed_external_vars = ["yi", ]

    def list_deriv_vars(self):
        input_keys = ('yi', 'yv','x0',)
        output_keys = ('x',)
        return input_keys, output_keys

    def f_dot(self, external, state):

        df = np.zeros((2))
        yvar = external[:2]
        yinv = external[2:]

        for i in range(0, 2):
            df[i] = 0.1 * state[i] * yinv[0] * yinv[1] * \
                yinv[4] - .32 * state[i] * yinv[2] * yinv[3] * yinv[5]

        return df

    def df_dy(self, external, state):

        df = np.zeros((2, 2))
        yvar = external[:2]
        yinv = external[2:]

        for i in range(0, 2):
            df[i, i] = 0.1 * yinv[0] * yinv[i] * \
                yinv[4] - .32 * yinv[2] * yinv[3] * yinv[5]

        return df

    def df_dx(self, external, state):

        df = np.zeros((2, 8))
        yvar = external[:2]
        yinv = external[2:]

        for i in range(0, 2):
            df[i, 2] = 0.1 * state[i] * yinv[1] * yinv[4]
            df[i, 3] = 0.1 * state[i] * yinv[0] * yinv[4]
            df[i, 4] = -.32 * state[i] * yinv[3] * yinv[5]
            df[i, 5] = -.32 * state[i] * yinv[2] * yinv[5]
            df[i, 6] = 0.1 * state[i] * yinv[0] * yinv[1]
            df[i, 7] = -.32 * state[i] * yinv[2] * yinv[3]

        return df

NTIME = 4


class Testcase_RK_deriv(unittest.TestCase):

    """ Test run/step/stop aspects of a simple workflow. """

    def setUp(self):
        """ Called before each test. """
        self.model = set_as_top(Assembly())

    def tearDown(self):
        """ Called after each test. """
        self.model = None

    def setup(self, compname, inputs, state0):

        self.model.add('comp', eval('%s(NTIME)' % compname))
        self.model.driver.workflow.add('comp')

        #data = pickle.load(open("data1346.pkl", 'rb'))

        for item in inputs + state0:
            val = self.model.comp.get(item)
            #key = "%d:%s" % (NTIME, item)
            if hasattr(val, 'shape'):
                shape1 = val.shape
                #self.model.comp.set(item, data[key])
                self.model.comp.set(item, np.random.random(shape1))
            else:
                #self.model.comp.set(item, data[key][0])
                self.model.comp.set(item, random.random())

    def run_model(self):

        self.model.comp.h = 0.01
        self.model.run()

    def compare_derivatives(self, var_in, var_out):

        wflow = self.model.driver
        inputs = ['comp.%s' % v for v in var_in]
        outputs = ['comp.%s' % v for v in var_out]

        # Numeric
        self.model.driver.update_parameters()
        Jn = wflow.calc_gradient(inputs=inputs,
                                 outputs=outputs,
                                 mode="fd")

        # Analytic forward
        self.model.driver.update_parameters()
        Jf = wflow.calc_gradient(inputs=inputs,
                                 outputs=outputs)

        diff = abs(Jf - Jn)
        assert_rel_error(self, diff.max(), 0.0, 1e-5)

        # Analytic adjoint
        self.model.driver.update_parameters()
        Ja = wflow.calc_gradient(inputs=inputs,
                                 outputs=outputs,
                                 mode='adjoint')

        diff = abs(Ja - Jn)
        assert_rel_error(self, diff.max(), 0.0, 1e-5)

    def test_with_time_invariant(self):

        compname = 'RKTest'
        inputs = ['yi', 'yv']
        outputs = ['x']
        state0 = ['x0']

        self.setup(compname, inputs, state0)
        self.run_model()
        self.compare_derivatives(inputs, outputs)


if __name__ == "__main__":

    unittest.main()
