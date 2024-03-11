from math import pi 
radius = float(input('Enter radius : '))
height = float(input('Enter height : '))
slope_length = float(input('Enter The slope length of the cone : '))
class volume:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    
    def get_The_volume_and_area_of_butter(self):
        a1 = 4/3 * pi * radius ** 3 
        a2 = 4 * pi * radius ** 2
        print('The volume of butter is %f ' % a1 )
        print('The area of butter is %f ' % a2 )
    def get_The_volume_and_area_of_cylindrical(self):
        b1 = pi * radius ** 2 * height
        b2 = 2 * pi * radius * height
        print('The volume of cylindrical is %f ' % b1 )
        print('The area of cylindrical is %f ' % b2 )
    def get_The_volume_and_area_of_cones(self):
        c1 = 1/3 * pi * radius ** 2 * height
        c2 = pi * radius * slope_length
        print('The volume of cones is %f ' % c1 )
        print('The area of cones is %f ' % c2 )
    
kore = volume (radius , height)
kore.get_The_volume_and_area_of_butter()

ostovane = volume (radius , height)
ostovane.get_The_volume_and_area_of_cylindrical()

makhroot = volume (radius , height)
makhroot.get_The_volume_and_area_of_cones()
