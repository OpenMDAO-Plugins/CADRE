
================
Package Metadata
================

- **author:** Tristan A. Hearn

- **author-email:** tristan.a.hearn@nasa.gov

- **classifier**:: 

    Intended Audience :: Science/Research
    Topic :: Scientific/Engineering

- **description-file:** README.txt

- **entry_points**:: 

    [openmdao.component]
    CADRE.solar.Solar_ExposedArea=CADRE.solar:Solar_ExposedArea
    CADRE.comm.Comm_GainPattern=CADRE.comm:Comm_GainPattern
    CADRE.attitude.Attitude_Attitude=CADRE.attitude:Attitude_Attitude
    CADRE.comm.Comm_VectorECI=CADRE.comm:Comm_VectorECI
    CADRE.reactionwheel.ReactionWheel_Power=CADRE.reactionwheel:ReactionWheel_Power
    CADRE.comm.Comm_BitRate=CADRE.comm:Comm_BitRate
    CADRE.orbit.Orbit_Initial=CADRE.orbit:Orbit_Initial
    CADRE.reactionwheel.ReactionWheel_Torque=CADRE.reactionwheel:ReactionWheel_Torque
    CADRE.attitude.Attitude_Angular=CADRE.attitude:Attitude_Angular
    CADRE.sun.Sun_PositionBody=CADRE.sun:Sun_PositionBody
    CADRE.comm.Comm_EarthsSpinMtx=CADRE.comm:Comm_EarthsSpinMtx
    CADRE.comm.Comm_LOS=CADRE.comm:Comm_LOS
    CADRE.CADRE_launch.Uniformity=CADRE.CADRE_launch:Uniformity
    CADRE.comm.Comm_GSposEarth=CADRE.comm:Comm_GSposEarth
    CADRE.comm.Comm_VectorBody=CADRE.comm:Comm_VectorBody
    CADRE.sun.Sun_PositionSpherical=CADRE.sun:Sun_PositionSpherical
    CADRE.attitude.Attitude_RotationMtx=CADRE.attitude:Attitude_RotationMtx
    CADRE.attitude.Attitude_Roll=CADRE.attitude:Attitude_Roll
    CADRE.power.Power_SolarPower=CADRE.power:Power_SolarPower
    CADRE.sun.Sun_PositionECI=CADRE.sun:Sun_PositionECI
    CADRE.attitude.Attitude_Torque=CADRE.attitude:Attitude_Torque
    CADRE.battery.BatteryConstraints=CADRE.battery:BatteryConstraints
    CADRE.power.Power_CellVoltage=CADRE.power:Power_CellVoltage
    CADRE.attitude.Attitude_RotationMtxRates=CADRE.attitude:Attitude_RotationMtxRates
    CADRE.battery.BatteryPower=CADRE.battery:BatteryPower
    CADRE.rk4.RK4=CADRE.rk4:RK4
    CADRE.CADRE_launch.GroundLOC=CADRE.CADRE_launch:GroundLOC
    CADRE.comm.Comm_AntRotationMtx=CADRE.comm:Comm_AntRotationMtx
    CADRE.power.Power_Total=CADRE.power:Power_Total
    CADRE.test.test_rk_deriv.RKTest=CADRE.test.test_rk_deriv:RKTest
    CADRE.CADRE_assembly.CADRE=CADRE.CADRE_assembly:CADRE
    CADRE.comm.Comm_EarthsSpin=CADRE.comm:Comm_EarthsSpin
    CADRE.comm.Comm_AntRotation=CADRE.comm:Comm_AntRotation
    CADRE.comm.Comm_VectorAnt=CADRE.comm:Comm_VectorAnt
    CADRE.KS.KSComp=CADRE.KS:KSComp
    CADRE.reactionwheel.ReactionWheel_Motor=CADRE.reactionwheel:ReactionWheel_Motor
    CADRE.attitude.Attitude_Sideslip=CADRE.attitude:Attitude_Sideslip
    CADRE.parameters.BsplineParameters=CADRE.parameters:BsplineParameters
    CADRE.comm.Comm_VectorSpherical=CADRE.comm:Comm_VectorSpherical
    CADRE.attitude.Attitude_AngularRates=CADRE.attitude:Attitude_AngularRates
    CADRE.comm.Comm_GSposECI=CADRE.comm:Comm_GSposECI
    CADRE.sun.Sun_LOS=CADRE.sun:Sun_LOS
    CADRE.CADRE_mdp.CADRE_Optimization=CADRE.CADRE_mdp:CADRE_Optimization
    CADRE.thermal_temperature.ThermalTemperature=CADRE.thermal_temperature:ThermalTemperature
    CADRE.CADRE_launch.CADRE_Launch=CADRE.CADRE_launch:CADRE_Launch
    CADRE.comm.Comm_Distance=CADRE.comm:Comm_Distance
    [openmdao.container]
    CADRE.solar.Solar_ExposedArea=CADRE.solar:Solar_ExposedArea
    CADRE.comm.Comm_GainPattern=CADRE.comm:Comm_GainPattern
    CADRE.attitude.Attitude_Attitude=CADRE.attitude:Attitude_Attitude
    CADRE.comm.Comm_VectorECI=CADRE.comm:Comm_VectorECI
    CADRE.reactionwheel.ReactionWheel_Power=CADRE.reactionwheel:ReactionWheel_Power
    CADRE.comm.Comm_BitRate=CADRE.comm:Comm_BitRate
    CADRE.orbit.Orbit_Initial=CADRE.orbit:Orbit_Initial
    CADRE.reactionwheel.ReactionWheel_Torque=CADRE.reactionwheel:ReactionWheel_Torque
    CADRE.attitude.Attitude_Angular=CADRE.attitude:Attitude_Angular
    CADRE.sun.Sun_PositionBody=CADRE.sun:Sun_PositionBody
    CADRE.comm.Comm_EarthsSpinMtx=CADRE.comm:Comm_EarthsSpinMtx
    CADRE.comm.Comm_LOS=CADRE.comm:Comm_LOS
    CADRE.CADRE_launch.Uniformity=CADRE.CADRE_launch:Uniformity
    CADRE.comm.Comm_GSposEarth=CADRE.comm:Comm_GSposEarth
    CADRE.comm.Comm_VectorBody=CADRE.comm:Comm_VectorBody
    CADRE.sun.Sun_PositionSpherical=CADRE.sun:Sun_PositionSpherical
    CADRE.attitude.Attitude_RotationMtx=CADRE.attitude:Attitude_RotationMtx
    CADRE.attitude.Attitude_Roll=CADRE.attitude:Attitude_Roll
    CADRE.power.Power_SolarPower=CADRE.power:Power_SolarPower
    CADRE.sun.Sun_PositionECI=CADRE.sun:Sun_PositionECI
    CADRE.attitude.Attitude_Torque=CADRE.attitude:Attitude_Torque
    CADRE.battery.BatteryConstraints=CADRE.battery:BatteryConstraints
    CADRE.power.Power_CellVoltage=CADRE.power:Power_CellVoltage
    CADRE.attitude.Attitude_RotationMtxRates=CADRE.attitude:Attitude_RotationMtxRates
    CADRE.battery.BatteryPower=CADRE.battery:BatteryPower
    CADRE.rk4.RK4=CADRE.rk4:RK4
    CADRE.CADRE_launch.GroundLOC=CADRE.CADRE_launch:GroundLOC
    CADRE.comm.Comm_AntRotationMtx=CADRE.comm:Comm_AntRotationMtx
    CADRE.power.Power_Total=CADRE.power:Power_Total
    CADRE.test.test_rk_deriv.RKTest=CADRE.test.test_rk_deriv:RKTest
    CADRE.CADRE_assembly.CADRE=CADRE.CADRE_assembly:CADRE
    CADRE.comm.Comm_EarthsSpin=CADRE.comm:Comm_EarthsSpin
    CADRE.comm.Comm_AntRotation=CADRE.comm:Comm_AntRotation
    CADRE.comm.Comm_VectorAnt=CADRE.comm:Comm_VectorAnt
    CADRE.KS.KSComp=CADRE.KS:KSComp
    CADRE.reactionwheel.ReactionWheel_Motor=CADRE.reactionwheel:ReactionWheel_Motor
    CADRE.attitude.Attitude_Sideslip=CADRE.attitude:Attitude_Sideslip
    CADRE.parameters.BsplineParameters=CADRE.parameters:BsplineParameters
    CADRE.comm.Comm_VectorSpherical=CADRE.comm:Comm_VectorSpherical
    CADRE.attitude.Attitude_AngularRates=CADRE.attitude:Attitude_AngularRates
    CADRE.comm.Comm_GSposECI=CADRE.comm:Comm_GSposECI
    CADRE.sun.Sun_LOS=CADRE.sun:Sun_LOS
    CADRE.CADRE_mdp.CADRE_Optimization=CADRE.CADRE_mdp:CADRE_Optimization
    CADRE.thermal_temperature.ThermalTemperature=CADRE.thermal_temperature:ThermalTemperature
    CADRE.CADRE_launch.CADRE_Launch=CADRE.CADRE_launch:CADRE_Launch
    CADRE.comm.Comm_Distance=CADRE.comm:Comm_Distance

- **home-page:** https://github.com/OpenMDAO-Plugins/CADRE

- **keywords:** openmdao

- **license:** Apache 2.0

- **maintainer:** Tristan A. Hearn

- **maintainer-email:** tristan.a.hearn@nasa.gov

- **name:** CADRE

- **requires-dist**:: 

    openmdao.main
    MBI

- **requires-python**:: 

    >=2.6
    <3.0

- **static_path:** [ '_static' ]

- **summary:** OpenMDAO implementation of the CADRE CubeSat design problem

- **version:** 0.4

