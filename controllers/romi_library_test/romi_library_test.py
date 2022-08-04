"""romi_test controller."""

# create the Robot instance.
#instantiating a Romi library object in simulation mode
#automatically loads proper WeBots libraries.
#the webots robot class lives inside of romi.simromi
romi = Romi(sim=True)

# get the time step of the current world.
timestep = int(romi.simromi.getBasicTimeStep())
#initialize a simulation time for us to use
simtime = 0

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while romi.simromi.step(timestep) != -1:
    simtime+=(timestep/1000.0)

    #send a sine wave motor command to the wheels
    motorspeed_amp = 100
    wheelcmd = motorspeed_amp*sin(simtime)

    romi.update(motorspeed_amp,motorspeed_amp,90,90,90)

    pass
