'''
This File will validate all the edge cases
'''

from parking_processing import Parkingprocess


def parking_slots(size):
    """
    Check the total size of our Parking Space
    """
    parking_process = Parkingprocess(int(size))
    return parking_process


def parking_space_is_full(parking_space):
    """
    checks whether parking space is full or not

    Params:
        parking_space - Object of the class parking_process
    """
    return len(parking_space.park_slot) <= 0


def vehicle_parking(parking_space, registration_number, driver_age):
    """
    parking of all the vehicles one by one and prints the allocated slot in the parking space

    Params:
        parking_space - Object of the class parking_process
        registration_number - registration number of the vehicles
        driver_age - age of the drivers
    """
    message = ''
    if parking_space:
        if not parking_space_is_full(parking_space):
            slot = parking_space.get_spot()
            _ = parking_space.set_spot(slot, registration_number)

            parking_space.vehicle_info_dict[slot] = {
                'reg_num' : registration_number,
                'age' : driver_age
            }
            message = 'Slot Number ' + str(slot) + ' is allocated'
    else:
        message = 'Undefined Parking space'
    return message


def slot_number_availability(parking_space, input_slot):
    """
    Check if the slot number exists or not.
    if exists, will check which one is available now

    Params:
        parking_space - Object of the class parking_process
        input_slot - Slot number in the Parking Space
    """
    message = ''
    if parking_space:
        if len(parking_space.park_slot) is None:
            message = 'Parking Space is not avaialble now'
        elif int(input_slot) >= 1 and int(input_slot) <= len(parking_space.park_slot):
            parking_slot = parking_space.park_slot
            value = parking_slot[int(input_slot)]
            if value is not None:
                parking_space.set_spot(int(input_slot), None)
                parking_space.vacant_spot(value)
                message = 'Slot number ' + input_slot + ' is available now'
        else:
            message = 'Slot number ' + input_slot + ' does not exists!'
    else:
        message = 'Undefined Parking space'
    return message


def slot_by_reg_num(parking_space, reg_number):
    """
    Check the slot number by Registration number of a vehicle

    Params:
        parking_space - Object of the class parking_process
        reg_number - Registration number of a Vehicle
    """
    message = ''
    if parking_space:
        if len(parking_space.park_slot) is None:
            message = 'Parking Space is not avaialble now'
        else:
            flag = False
            parking_slot = parking_space.park_slot
            for parked_car_rnum in parking_slot:
                if parked_car_rnum is not None:
                    if parked_car_rnum == reg_number:
                        flag = True
                        message += str(parking_space.get_spot()) + ', '
                        break
            if not flag:
                message = 'Registration Number is not found in the Records!'
    else:
        message = 'Undefined Parking Space'
    return message


def slot_by_driver_age(parking_space, age):
    """
    Check the slot number by age of driver

    Params:
        parking_space - Object of the class parking_process
        age - Age of a driver
    """
    message = ''
    if parking_space:
        if len(parking_space.park_slot) is None:
            message = 'Parking Space is not avaialble now'
        else:
            flag = False
            #spot = parking_space.get_spot()
            parking_slot = parking_space.vehicle_info_dict[0].get('age')

            if parking_slot == age:
                flag = True
                message += str(parking_space.get_spot()) + ', '
            if not flag:
                message = 'Driver Age is not found in the Records!'
    else:
        message = 'Undefined Parking Space'
    return message
