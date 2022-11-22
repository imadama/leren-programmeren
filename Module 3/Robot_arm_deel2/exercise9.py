from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 3

x = 1

for y in range(0,4): 
    for z in range(x):
        robotArm.grab()
        for y in range(0,5):
            robotArm.moveRight()
        robotArm.drop()
        for y in range(0,5):
            robotArm.moveLeft()
    robotArm.moveRight()
    x+=1   #telt na deze hele loop 1 bij de x op, zodat hij bij de volgende kolom 2 blokjes pakt etc. 

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()