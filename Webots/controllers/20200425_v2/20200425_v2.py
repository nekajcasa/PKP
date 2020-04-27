from controller import Robot

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

senzorji=[]
senzorji_vrednosti=[]
senzorji_imena = ["position_sensor_os1",\
            "position_sensor_os2",\
            "position_sensor_os3",\
            "position_sensor_os4",\
            "position_sensor_os5",\
            "position_sensor_os6"]
         
for i in senzorji_imena:
    senzorji.append(robot.getPositionSensor(i))
for i in senzorji:
    i.enable(timestep)
for i in senzorji:
    senzorji_vrednosti.append(0.0)
            
osi=[]
osi_imena=["motor_os1",\
        "motor_os2",\
        "motor_os3",\
        "motor_os4",\
        "motor_os5",\
        "motor_os6"]
        
for i in osi_imena:
    osi.append(robot.getMotor(i))
for i in osi:
    i.setPosition(float('inf'))
    i.setVelocity(0.0)

print("test")

osi[5].setVelocity(1)
        
# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getMotor('motorname')
#  ds = robot.getDistanceSensor('dsname')
#  ds.enable(timestep)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    
    for i in range(len(senzorji)):
        senzorji_vrednosti[i]=senzorji[i].getValue()

    print(senzorji_vrednosti)
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    pass

# Enter here exit cleanup code.
