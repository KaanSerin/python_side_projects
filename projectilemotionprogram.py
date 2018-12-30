import math

def message():
    print("Projectile motion distance calculator." + "\nThe program will calculate the max height as well.")
    #print("Enter the projectile's initial velocity(in m/s) and the angle to the horizontal(in degrees)..")
    #print("Enter the gravitational constant..(Optional)")
    #print("Thats pretty much it. :D")


#Print the greeting message
message()

#Getting the input from the user
velocity = float(input("Please enter the initial velocity(in meters/second): "))
angle = float(input("Please enter the velocity's angle to horizontal(in degrees): "))
g_constant = input("Please enter the gravitational constant(leave empty for 9.8): ")

if (g_constant == ""):
    g_constant = 9.8
else:
    g_constant = float(g_constant)

#Calculating the time of flight, horizontal distance and maximum height
t_flight = (velocity * math.sin(math.radians(angle))) / (g_constant / 2)
distance = (velocity * math.cos(math.radians(angle))) * t_flight
h_max = (velocity * math.sin(math.radians(angle)))**2 / (2 * g_constant)

#Printing it out
print("\nHorizontal distance of the projectile from the origin", format(distance, ".3f") + " meters")
print("Maximum vertical height: ", format(h_max, ".3f") + " meters")
