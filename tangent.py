import matplotlib.pyplot as plt
import numpy as np

def tangent(Cx,Cy, Px,Py):
    "where (Cx, Cy) are the circle's center coordinates and (Px,Py) is the point we're trying to find the tangent to"
    #finding the slope and intercept of the two coordinates
    slope = (Cy - Py)/(Cx - Px)
    #intercept = -(Cx*slope)+Cy
    
    #finding the slope and intercept for the tangent line
    tanSlope = -1/slope
    tanIntercept = Py - tanSlope*Px
    
    #plotting the circle
    radius = np.sqrt(((Px-Cx)**2)+((Py-Cy)**2))
    x = np.linspace(Cx-2*radius, Cx+2*radius, 100)
    y = tanSlope*x + tanIntercept
    
    figure, axes = plt.subplots()
    draw_circle = plt.Circle((Cx, Cy), radius, fill=False)
    plt.xlim(Cx-2*radius, Cx+2*radius)
    plt.ylim(Cy-2*radius, Cy+2*radius)
    plt.gcf().gca().add_artist(draw_circle)
    axes.set_aspect(1)
    plt.plot(x,y)
    
    return tanSlope, tanIntercept
