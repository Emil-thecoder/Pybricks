from pybricks.hubs import MoveHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Stop, Color
from pybricks.tools import wait

# Define functions

# wiggle function to make sure pieces are picked up and attached properly
def wiggle(w, sp, loc):
    belt.run_target(speed=sp, target_angle=loc - w)
    belt.run_target(speed=sp, target_angle=loc + w)
    wait(100)


# Initialize the arm motor
arm = Motor(Port.D)
arm.run_until_stalled(-100, duty_limit=30)
arm.reset_angle(0)

# Initialize the belt motor
belt = Motor(Port.B)
belt.run_until_stalled(-100, duty_limit=30)
belt.reset_angle(0)

# Initialize flag

flag = Motor(Port.A)

# Component positions
FEET = 0
BELLY = 365
HEAD = 128
ARMS = 244
NECK = 521
BASE = 712

# Place all the elements
for element in (FEET, BELLY, ARMS, NECK, HEAD):

    # Go to the element
    belt.run_target(speed=200, target_angle=element)

    # Grab the element
    arm.run_time(speed=300, time=2000)
    wait(100)

    # wiggle
    wiggle(w=2, sp=400, loc = element)
    wiggle(w=3, sp=400, loc = element)

    # Lift the element by going back to nearly zero
    arm.run_target(speed=300, target_angle=55)

    # Go to the base
    belt.run_target(speed=200, target_angle=BASE)
    wait(500)

    # Put the element down
    arm.run_time(speed=800, time=3000)

    # wiggle
    wiggle(w=2, sp=500, loc = BASE)
    wiggle(w=3, sp=500, loc = BASE)

    # Lift the arm back up
    arm.run_target(speed=200, target_angle=0)

# When we are done, eject the result
belt.run_target(speed=200, target_angle=FEET)
flag.run_target(speed = 2500, target_angle= 360*10)

