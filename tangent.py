#Incomplete

def tangent(Cx,Cy, Px,Py):
    "where (Cx, Cy) are the circle's center coordinates and (Px,Py) is the point we're trying to find the tangent to"
    #finding the slope and intercept of the two coordinates
    slope = (Cy - Py)/(Cx - Px)
    intercept = -(Cx*slope)+Cy
    
    #finding the inverse formula
    invSlope = 1/slope
    invIntercept = Cx - (Cy/slope)
    

    
    return slope, intercept, invSlope, invIntercept
