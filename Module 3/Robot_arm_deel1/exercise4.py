from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')
robotArm.speed = 3
# Jouw python instructies zet je vanaf hier:

for i in range(0,4):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()
    robotArm.moveLeft()
    
robotArm.grab()
robotArm.moveRight()
robotArm.drop()

for i in range(1,5):
    robotArm.moveRight()
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()