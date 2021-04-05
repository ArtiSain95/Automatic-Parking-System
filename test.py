import unittest
from validations import parking_slots, parking_space_is_full, vehicle_parking, slot_number_availability, slot_by_reg_num, slot_by_driver_age


class TestParkingLotUtilities(unittest.TestCase):
    """
    Unit Test Cases
    """

    def test_size_of_parking(self):
        testParkingLot = parking_slots(str(6))
        self.assertEqual(len(testParkingLot.park_slot), 6)

    def test_vehicle_parking_lot_allocated(self):
        testParkingLot = parking_slots(str(6))
        testString = vehicle_parking(testParkingLot, 'PB-01-HH-1234', 21)
        self.assertEqual('Slot Number 0 is allocated', testString)

    def test_parking_space_is_full(self):
        testParkingLot = parking_slots(str(6))
        self.assertEqual(parking_space_is_full(testParkingLot), False)

    def test_vehicle_parking_lot_not_defined(self):
        testString = vehicle_parking(None, 'PB-01-HH-1234', 21)
        self.assertEqual('Undefined Parking space', testString)

    def test_slot_by_driver_age(self):
        testParkingLot = parking_slots(str(6))
        testParkString = vehicle_parking(testParkingLot, 'PB-01-HH-1110', 21)
        testString = slot_by_driver_age(testParkingLot, 21)
        self.assertEqual(testString, '1, ')

    def test_slot_number_availability(self):
        testParkingLot = parking_slots(str(6))
        testParkString = vehicle_parking(testParkingLot, 'PB-01-HH-4321', 21)
        testString = slot_number_availability(testParkingLot, '1')
        self.assertEqual('Slot number 1 is available now', testString)

    def test_slot_number_availability_cannot_exit(self):
        testParkingLot = parking_slots(str(6))
        testParkString = vehicle_parking(testParkingLot, 'PB-01-HH-3314', 21)
        testString = slot_number_availability(testParkingLot, '7')
        self.assertEqual('Slot number 7 does not exists!', testString)

    def test_slot_by_reg_num(self):
        testParkingLot = parking_slots(str(6))
        testParkString = vehicle_parking(testParkingLot, 'PB-01-HH-5436', 21)
        testString = slot_by_reg_num(testParkingLot, 'PB-01-HH-5436')
        self.assertEqual(testString, '1, ')


if __name__ == '__main__':
    unittest.main()