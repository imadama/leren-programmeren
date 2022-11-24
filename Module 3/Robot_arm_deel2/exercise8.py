from RobotArm import RobotArm
robotArm = RobotArm('exercise 8')
# Jouw python instructies zet je vanaf hier:
for x in range(8):
    robotArm.moveRight()
    for x in range(0,7):
        robotArm.grab()
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()