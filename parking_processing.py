'''
File to define Vehicle and Parking Class, Execute commands and return corresponding response
'''

from constants import DEFAULT_SIZE, CREATE_PARKING_LOT, PARK, DRIVER_AGE, \
                    SLOT_NUMBERS_FOR_DRIVER_OF_AGE, SLOT_NUMBER_FOR_CAR_WITH_NUMBER, \
                    VEHICLE_REGISTRATION_NUMBER_FOR_DRIVER_OF_AGE, LEAVE, INDEX_HANDLER

class Vehicle:
    """
    Class to denote Vehicles. eg, Car
    """

    def __init__(self, registration_number, driver_age):
        """
        Constructor method for Vehicle object

        Params:
            registration_number - registration number of the vehicle
            driver_age - age of the driver
        """
        self.driver_age = driver_age
        self.registration_number = registration_number
        self.spot = None

    def get_spot(self):
        """
        Get spot
        """
        return self.spot

    def set_spot(self):
        """
        Set spot

        Params:
            slot - allocate spot for vehicle parked in the parking Space
        """
        return self.spot

    def get_reg_num(self):
        """
        Get Registration Number
        """
        return self.registration_number

    def get_driver_age(self):
        """
        Get driver_age
        """
        return self.driver_age


class Parkingprocess:
    """
    Class to explain the Overall Parking Process
    """

    def __init__(self, size):
        """
        Constructor method for Parkingprocess object

        Params:
            size - total size of our Parking Area/ Total number of spots in Parking Area
        """
        self.park_slot = [0]*size
        self.vehicle_info_dict = dict()

    def get_spot(self):
        """
        Get spot of parked vehicle and increment it to 1
        """
        index = 0
        for i in self.park_slot:
            if i == 0:
                return index
            index+=1
        return None

    def set_spot(self, i, reg_num):
        """
        Sets Up the Parking slot

        Params:
        i - Particular Spot for a vehicle to park
        reg_num - Registration Number of a vehicle
        """
        self.park_slot[int(i)] = reg_num
        return self.park_slot

    def vacant_spot(self, i):
        """
        method to vacate Parking slot

        Params:
        i - Particular Spot for a vehicle to vacate
        """
        self.park_slot[int(i)] = 0
        del self.vehicle_info_dict[int(i)]


    def validation(self):
        """
        check if the slot exists or not
        """
        if len(self.park_slot) is not None:
            return True
        return False

    def slot_numbers_for_driver_of_age(self, age):
        """
        function to get slot number by age of driver

        Params:
        age - Age of driver
        """
        req_list = list()
        for spot, meta_info in self.vehicle_info_dict.items():
            if meta_info['age'] == age.replace('\n',''):
                req_list.append(spot+INDEX_HANDLER)
        return ','.join([str(i) for i in req_list])

    def slot_number_for_car_with_number(self, reg_num):
        """
        function to get slot number with registration number of vehicle

        Parmas:
        reg_num - Registration number of Car
        """
        for spot, meta_info in self.vehicle_info_dict.items():
            if meta_info['reg_num'] == reg_num.replace('\n', ''):
                return spot+INDEX_HANDLER
        return None

    def vehicle_registration_number_for_driver_of_age(self, age):
        """
        function to get the registration numbers with the age of driver

        Params:
        age - Age of driver
        """
        req_list = list()
        for meta_info in self.vehicle_info_dict.values():
            if meta_info['age'] == age:
                req_list.append(meta_info['reg_num'])


class CommandConstants:
    """
    This class has commands to return their corresponding information
    """

    def create_parking_command(args):
        """
        Command for creation of parking space
        """
        return 'Created parking of {} slots'.format(*args)

    def parked_vehicle_info_command(args):
        """
        Command to return info of parked vehicles
        """
        args[1] = str(int(args[1]) + INDEX_HANDLER)
        return 'Car with vehicle registration number "{}" has ' \
                'been parked at slot number {}'.format(*args)

    def vacated_spots_info_command(args):
        """
        Command to return info of vacated spots in our parking space
        """
        args[0] = str(int(args[0]) + INDEX_HANDLER)
        return 'Slot number {} vacated, the car with vehicle' \
                'registration number "{}" left the space, the' \
                'driver of the car was of age {}'.format(*args)


def process_file_commands(command, class_pointer):
    """
    This methos will excute commands to return corresponding response
    """
    if CREATE_PARKING_LOT in command:
        class_pointer.park_slot = [0]*int(command.replace('\n','').split(' ')[1])
        return CommandConstants.create_parking_command([command.replace('\n','').split(' ')[1]])

    if PARK in command and DRIVER_AGE in command:
        if not class_pointer.validation():
            print('Parking Space is already full')
            return

        spot = class_pointer.get_spot()
        _ = class_pointer.set_spot(spot, command.split(' ')[1])

        class_pointer.vehicle_info_dict[spot] = {
            'reg_num' : command.split(' ')[1],
            'age' : command.split(' ')[3].replace('\n', '')
        }
        return CommandConstants.parked_vehicle_info_command([command.split(' ')[1], spot])

    if SLOT_NUMBERS_FOR_DRIVER_OF_AGE in command:
        return class_pointer.slot_numbers_for_driver_of_age(command.split(' ')[1])

    if SLOT_NUMBER_FOR_CAR_WITH_NUMBER in command:
        return class_pointer.slot_number_for_car_with_number(command.split(' ')[1])

    if VEHICLE_REGISTRATION_NUMBER_FOR_DRIVER_OF_AGE in command:
        return class_pointer.vehicle_registration_number_for_driver_of_age(command.split(' ')[1])

    if LEAVE in command:
        spot = int(command.split(' ')[1].replace('\n', ''))
        if spot not in class_pointer.vehicle_info_dict:
            return 'Slot is not occupied to vacate'
        message =  CommandConstants.vacated_spots_info_command(
                        [spot, class_pointer.vehicle_info_dict[spot]['reg_num'],
                        class_pointer.vehicle_info_dict[spot]['age']])
        _ = class_pointer.vacant_spot(command.split(' ')[1])
        return message


if __name__=="__main__":

    vehicle_info_dict = dict()
    pp = Parkingprocess(DEFAULT_SIZE)
    while True:

        fp = open(input("enter your input file:")).readlines()

        ofp = open('output.txt','+a')
        for command in fp:
            message = process_file_commands(command, pp)
            if message:
                print(message)
                ofp.write(str(message)+'\n')
        ofp.close()
        break
