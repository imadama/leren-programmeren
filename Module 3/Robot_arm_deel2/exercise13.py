from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 3

y = 1

while y < 9:
    robotArm.grab()
    color = robotArm.scan()
    if color == "":
        robotArm.wait()
    else:
        for z in range(y):
            robotArm.moveRight()
        robotArm.drop()
        for z in range(y):
            robotArm.moveLeft()
        y+=1

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()