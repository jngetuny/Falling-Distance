#13. Falling Distance When an object is falling because of gravity, 
#the following formula can be used to determine the distance the object 
#falls in a specific time period: d=12gt2 The variables in the formula are as follows: 
#d is the distance in meters, g is 9.8, and t is the amount of time,
#in seconds, that the object has been falling. 
#Write a function named falling_distance that accepts an object’s falling time (in seconds) as an argument. 
#The function should return the distance, in meters, that the object has fallen during that time interval.
#Write a program that calls the function in a loop that passes 
#the values 1 through 10 as arguments and displays the return value.
#Gravity constant
Gravity = 9.8
#Define falling_ distance function as fall_time
def falling_distance(fall_time):
#distance the object
    distance = (1/2) * Gravity * (fall_time**2)
#let function return the distance
    return distance
#Define main() function 
def main():
# Supply headers seconds and Distance 
  print('Seconds\tDistance')
#Underline the headers 
  print('------------------')
#Run function in a loop
  for Time_in_seconds  in range(1, 11):
     print(Time_in_seconds,'\t', format(falling_distance(Time_in_seconds),'.2f'))
main()