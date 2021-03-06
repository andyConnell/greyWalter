import RPi.GPIO as GPIO
import time
import enums

GPIO.setmode(GPIO.BCM)

class Actuators:

    def __init__(self):

        self.led_pin = [-1,-1,-1,-1]
        self.led_state = [-1,-1,-1,-1]


    #if everything OK, return 0. If actuator type unknown or position > limit, return -1
    def initActuator(self, actuator_type, pos, pin):

        idx = pos - 1

        if actuator_type == enums.ActuatorType.led:


            if pos <= len(self.led_pin) and pos > 0:
                self.led_pin[idx] = pin
                GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
                self.led_state[idx] = 0
                return 0

            else:
                raise RuntimeError('LED can only be assigned to position 1-' + str(len(self.led_pin)))
                return -1

        else:
            raise RuntimeError('Unknown actuator type!')
            return -1


    #if everything OK, return 0. If actuator type unknown or position > limit or value is not (0 or 1), return -1
    def setActuatorValue(self, actuator_type, pos, value):

        idx = pos - 1

        if actuator_type == enums.ActuatorType.led:

            if not (value==1 or value==0):
                raise RuntimeError('LED value can only be 1 or 0!')
                return -1

            if pos <= len(self.led_pin) and pos > 0:

                if(self.led_pin[idx] == -1):
                    raise RuntimeError('Pin for LED in position ' + str(pos) + ' is not assigned')
                    return -1

                else:

                    GPIO.output(self.led_pin[idx],value)
                    self.led_state[idx] = value
                    return 0

            else:
                raise RuntimeError('LED can only be assigned to position 1-' + str(len(self.led_pin)))
                return -1

        else:
            raise RuntimeError('Unknown actuator type!')
            return -1



    def getActuatorValue(self, actuator_type, pos):

        idx = pos - 1

        if actuator_type == enums.ActuatorType.led:

            if pos <= len(self.led_pin) and pos > 0:

                if(self.led_state[idx] == -1) :
                    raise RuntimeError('Pin for LED in position ' + str(pos) + ' is not assigned')
                    return -1

                else:

                    return self.led_state[idx]

            else:
                raise RuntimeError('LED are only assigned to positions 1-' + str(len(self.led_pin)))
                return -1

        else:
            raise RuntimeError('Unknown actuator type!')
            return -1
