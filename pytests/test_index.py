import pytest
from ipynb.fs.full.index import Driver, Passenger, Ride, meryl, daniel, flatiron_taxi, ride_to_school, ride_home

def test_class_definitions():
    class ExampleClass:
        pass
     assert type(Driver) == type(ExampleClass)
     assert type(Passenger) == type(ExampleClass)
     assert type(Ride) == type(ExampleClass)


def test_instances():
     assert type(meryl) == type(Passenger())
     assert type(daniel) == type(Passenger())
     assert type(flatiron_taxi) == type(Driver())
     assert type(ride_to_school) == type(Ride())
     assert type(ride_home) == type(Ride())
