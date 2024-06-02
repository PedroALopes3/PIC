import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time


def aceMag (aX, aY, aZ):
    return math.sqrt((aX**2)+(aY**2)+(aZ**2))

def gyroMag (gX, gY, gZ):
    return math.sqrt((gX**2)+(gY**2)+(gZ**2))

def angle (aMag):
    return (math.acos(aMag/9.8)*180)

def plot(data):
    fig, ax = plt.subplots()
    ax.set_title('Dynamic Angle Plot')
    ax.set_xlabel('Time')
    ax.set_ylabel('Angle (degrees)')
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 180)
    line, = ax.plot([], [], marker='o')



def tralho (aX, aY, aZ, gX, gY, gZ):
    
    aMag = aceMag(aX, aY, aZ)
    gMag = gyroMag(gX, gY, gZ)
    ang = angle(aMag)