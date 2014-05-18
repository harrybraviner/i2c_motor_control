from smbus import SMBus

# Commands we may send the control board
MOTOR_CONTROL_SET_DIR_SPEED_CMD = 0x01
# Direction signals
MOTOR_CONTROL_LEFT_FORE = 0b00000001
MOTOR_CONTROL_LEFT_BACK = 0b00000010
MOTOR_CONTROL_LEFT_STOP = 0b00000000
MOTOR_CONTROL_RIGHT_FORE = 0b00000100
MOTOR_CONTROL_RIGHT_BACK = 0b00001000
MOTOR_CONTROL_RIGHT_STOP = 0b00000000


class motorControlBoard:
    """Class to allow communication with the motor
       control board built by me using I2C."""
    __board_I2C_address = 0

    def __init__(self, board_address):
        if isinstance(board_address, int):
            if board_address > 0 and board_address < 0x78:
                self.__board_I2C_address = int
            else:
                raise Exception("Board address must be an integer between 0 and 0b1111000 (=120) exclusive.")
        else:
                raise Exception("Board address must be an integer.")
        self.__bus = SMBus(1)   # FIXME = have an option to make this zero for the old Raspberry Pis

    def set_speeds(left_speed, right_speed):
        # Enforce limits due to 8-bit resolution
        if(left_speed < -0xff):		left_speed = -0xff
        if(left_speed > +0xff):		left_speed = +0xff
        # Enforce limits due to 8-bit resolution
        if(right_speed < -0xff):	right_speed = -0xff
        if(right_speed > +0xff):	right_speed = +0xff

        direction = 0x00;
        if(left_speed < 0):     direction |= MOTOR_CONTROL_LEFT_BACK
        elif(left_speed > 0):   direction |= MOTOR_CONTROL_LEFT_FORE
        if(right_speed < 0):    direction |= MOTOR_CONTROL_RIGHT_BACK
        elif(right_speed > 0):  direction |= MOTOR_CONTROL_RIGHT_FORE

        bus.write_i2c_block_data(self.__board_I2C_address, MOTOR_CONTROL_SET_DIR_SPEED_CMD, [direction, abs(left_speed), abs(right_speed)])
