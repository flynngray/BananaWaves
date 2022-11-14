from turtle import speed
import wimbdy
import tube


def mainMethod(name):
    coordinates = tube.beach_location(name)
    dirandspeed = wimbdy.wimbdy(coordinates[0], coordinates[1])
    direction = float(dirandspeed[0])
    speed = float(dirandspeed[1])



    finalScore = tube.final_rating(name, direction, speed)


    return finalScore



for i in tube.beaches:
    print(mainMethod(i))
    print('')