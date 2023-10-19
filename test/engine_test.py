from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

import unittest
import datetime

class TestCapuletEngine(unittest.TestCase):

    def test_needs_service_true(self):
        last_service_date = datetime.datetime(2023,10,1)
        current_mileage = 30020
        last_service_mileage = 1
        engine = CapuletEngine(last_service_date,current_mileage,last_service_mileage)
        self.assertTrue(engine.engine_should_be_serviced())

    def test_needs_service_false(self):
        last_service_date = datetime.datetime(2023,10,1)
        current_mileage = 200200
        last_service_mileage = 1
        engine = CapuletEngine(last_service_date,current_mileage,last_service_mileage)
        self.assertFalse(engine.engine_should_be_serviced())

class TestWilloughbyEngine(unittest.TestCase):

    def test_needs_service_true(self):
        last_service_date = datetime.datetime(2023,10,1)
        current_mileage = 60020
        last_service_mileage = 1
        engine = WilloughbyEngine(last_service_date,current_mileage,last_service_mileage)
        self.assertTrue(engine.engine_should_be_serviced())

    def test_needs_service_false(self):
        last_service_date = datetime.datetime(2023,10,1)
        current_mileage = 200200
        last_service_mileage = 1
        engine = WilloughbyEngine(last_service_date,current_mileage,last_service_mileage)
        self.assertFalse(engine.engine_should_be_serviced())            

class TestSternman(unittest.TestCase):

    def test_needs_service_true(self):
        last_service_date = datetime.datetime(2023,10,1)
        warning_light_is_on = True
        engine = SternmanEngine(last_service_date,warning_light_is_on)
        self.assertTrue(engine.engine_should_be_serviced())

    def test_needs_service_false(self):
        last_service_date = datetime.datetime(2023,10,1)
        warning_light_is_on = False
        engine = SternmanEngine(last_service_date,warning_light_is_on)
        self.assertFalse(engine.engine_should_be_serviced())            