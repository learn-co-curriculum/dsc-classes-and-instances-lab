
# Classes and Instances - Lab

## Introduction
Okay, you've learned how to declare classes and create instances in the last lesson. Now it's time to put these new skills to the test!

## Objectives

You will be able to:

* Describe a class and how it can be used to create objects
* Describe an instance object
* Create an instance of a class

## Defining Classes


You're about to create your first packages with class definitions! You've already seen how to import packages such as NumPy and Pandas, and you can organize your own code in a similar manner. For example, once you define the ride class in a file ride.py you can then import said code in another notebook or script with `import ride`. 

So without further ado, create three files in this folder: **ride.py**, **driver.py**, and **passenger.py**. In each of these, define an accompanying class. By convention, you should capitalize the first letter of the names of these classes within the .py file. For example, in the ride.py file, define a Ride class. For now, the classes need not do anything, just write the keyword `pass` on the first line under each of your class definitions.


```python
from ride import Ride
```


```python
# __SOLUTION__ 
from ride import Ride
```


```python
# import Driver class here
```


```python
# __SOLUTION__ 
# import Driver class here
from driver import Driver
```


```python
# import Passenger class here
```


```python
# __SOLUTION__ 
# import Passenger class here
from passenger import Passenger
```

## Creating Instances

Now practice using your classes to make instances of those classes. Make two instances of the Passenger class and assign them to the variables `meryl` and `daniel`, respectively.


```python
meryl = None
daniel = None
print(meryl, daniel)
```


```python
# __SOLUTION__ 
meryl = Passenger()
daniel = Passenger()
print(meryl, daniel)
```

    <passenger.Passenger object at 0x10ad13390> <passenger.Passenger object at 0x10ad13358>


Next, make one instance of the driver class and assign it to the variable, `flatiron_taxi`.


```python
flatiron_taxi = None
print(flatiron_taxi)
```


```python
# __SOLUTION__ 
flatiron_taxi = Driver()
print(flatiron_taxi)
```

    <driver.Driver object at 0x10ad132e8>


Finally, make two instances of the Ride class and assign them to `ride_to_school` and `ride_home`. 


```python
ride_to_school = None
ride_home = None
print(ride_to_school, ride_home)
```


```python
# __SOLUTION__ 
ride_to_school = Ride()
ride_home = Ride()
print(ride_to_school, ride_home)
```

    <ride.Ride object at 0x10ad13550> <ride.Ride object at 0x10ad13518>


## Summary
Great! In this lab, you were able to define multiple classes and create instances of those classes.
