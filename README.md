
# Classes and Instances - Lab

## Introduction

Okay, you've learned how to declare classes and create instances in the last lesson. Now it's time to put these new skills to the test!

## Objectives

In this lab you will: 

* Create an instance of a class

## Classes


You're about to create your first package with class definitions! You've already seen how to import packages such as NumPy and Pandas, and you can organize your own code in a similar manner. For example, once you define the `Ride` class in a file **ride.py**, you can then import said code in another notebook or script using:


```python
# Import the entire file
import ride

# Import only the Ride class
from ride import Ride
```


```python
# __SOLUTION__ 
# Import the entire file
import ride

# Import only the Ride class
from ride import Ride
```

In addition to **ride.py** file, we also created another file **driver.py** that contains the `Driver` class. Import this class in the cell below: 


```python
# Import only the Driver class

```


```python
# __SOLUTION__ 
# Import only the Driver class
from driver import Driver
```

Create a `Passenger` class that doesn't contain anything in the following cell: 

> Note: By convention, you should use CamelCase to name the class. Also, you can't create an "empty" class. At the least, you need to specify the pass keyword to ensure the class definition is syntactically valid. 


```python
# Create Passenger class

```


```python
# __SOLUTION__ 
# Create Passenger class
class Passenger(object):
    pass
```

## Instances

Now practice using these classes to create instances. First, make two instances of the `Passenger` class and assign them to the variables `meryl` and `daniel`, respectively: 


```python
# Two instances of the Passenger class
meryl = None
daniel = None
print(meryl, daniel)
```


```python
# __SOLUTION__ 
# Two instances of the Passenger class
meryl = Passenger()
daniel = Passenger()
print(meryl, daniel)
```

    <__main__.Passenger object at 0x1082ae2e8> <__main__.Passenger object at 0x1082ae2b0>


Next, make one instance of the `Driver` class and assign it to the variable, `flatiron_taxi`.


```python
# Two instances of the Driver class
flatiron_taxi = None
print(flatiron_taxi)
```


```python
# __SOLUTION__ 
# Two instances of the Driver class
flatiron_taxi = Driver()
print(flatiron_taxi)
```

    <driver.Driver object at 0x1082ae4a8>


Finally, make two instances of the `Ride` class and assign them to `ride_to_school` and `ride_home`. 


```python
# Two instances of the Ride class
ride_to_school = None
ride_home = None
print(ride_to_school, ride_home)
```


```python
# __SOLUTION__ 
# Two instances of the Ride class
ride_to_school = Ride()
ride_home = Ride()
print(ride_to_school, ride_home)
```

    <ride.Ride object at 0x1082ae908> <ride.Ride object at 0x1082ae8d0>


## Summary
Great! In this lab, you were able to define classes and create instances of those classes.
