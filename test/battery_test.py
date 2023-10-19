from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

import unittest
import datetime

class TestNubbinBattery(unittest.TestCase):

    def test_needs_service_true(self):
        current_date = datetime.datetime(2023,10,20)
        last_service_date = datetime.datetime(2018,1,20)
        battery = NubbinBattery(current_date,last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = datetime.datetime(2023,10,20)
        last_service_date = datetime.datetime(2022,1,20)
        battery = NubbinBattery(current_date,last_service_date)
        self.assertFalse(battery.needs_service())  

class TestSpindlerBattery(unittest.TestCase):

    def test_needs_service_true(self):
        current_date = datetime.datetime(2023,10,20)
        last_service_date = datetime.datetime(2020,1,20)
        battery = SpindlerBattery(current_date,last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = datetime.datetime(2023,10,20)
        last_service_date = datetime.datetime(2022,1,20)
        battery = SpindlerBattery(current_date,last_service_date)
        self.assertFalse(battery.needs_service())
