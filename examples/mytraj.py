from math import pi, tan, cos

def height_proj(v0, y0, theta_in_degs, x):
    g = 9.81

    theta = theta_in_degs * pi / 180

    y = y0 + x * tan(theta) - (g * x ** 2) / (2 * (v0 * cos(theta)) ** 2)
    
    return y
    
print(height_proj(44, 1, 80, 0.5))    
 
