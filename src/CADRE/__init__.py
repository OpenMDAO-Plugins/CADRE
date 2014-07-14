#from .CADRE_mdp import CADRE_Optimization
from CADRE_assembly import CADRE, Attitude_Angular, Attitude_AngularRates, \
    Attitude_Attitude, Attitude_Roll, Attitude_RotationMtx, \
    Attitude_RotationMtxRates, Attitude_Sideslip, Attitude_Torque, \
    BatteryConstraints, BatteryPower, BatterySOC, BsplineParameters, \
    Comm_AntRotation, Comm_AntRotationMtx, Comm_BitRate, Comm_DataDownloaded, \
    Comm_Distance, Comm_EarthsSpin, Comm_EarthsSpinMtx, Comm_GainPattern, \
    Comm_GSposEarth, Comm_GSposECI, Comm_LOS, Comm_VectorAnt, Comm_VectorBody,\
    Comm_VectorECI, Comm_VectorSpherical, Orbit_Initial, Orbit_Dynamics, \
    ReactionWheel_Motor, ReactionWheel_Power, ReactionWheel_Torque, \
    ReactionWheel_Dynamics, Solar_ExposedArea, Sun_LOS, Sun_PositionBody, \
    Sun_PositionECI, Sun_PositionSpherical, ThermalTemperature, \
    Power_CellVoltage, Power_SolarPower, Power_Total
from .rk4 import RK4

from numpy import loadtxt
import os

# load launch data
fpath = os.path.dirname(os.path.realpath(__file__))
launch_data = loadtxt(fpath + '/data/Launch/launch1.dat')

# orbit position and velocity data for each design point
r_e2b_I0s = launch_data[1::2, 1:]

# number of days since launch for each design point
LDs = launch_data[1::2, 0] - 2451545
