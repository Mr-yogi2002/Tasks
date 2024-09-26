class efx:
   __pi = 3.141

   def value_of_pi(self):
       return self.__pi
   def area_of_circle(self, radius=1):
       area = self.__pi * radius * radius
       return area

   def perimeter_of_circle(self, radius=1):
       perimeter = 2 * self.__pi * radius
       return perimeter

s = efx()
print(s.value_of_pi())
print(s.area_of_circle(10))
print(s.perimeter_of_circle())