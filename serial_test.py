import serial
import time

arduino = serial.Serial(port='COM6',  baudrate=115200, timeout=0.7)


def write_read(x):
    arduino.write(bytes(x,  'utf-8'))
    arduino.flush()
    data = arduino.readline()
    return  data


while True:
    #user_input = int(input("number: "))
    rf = '%02d,%02d,%02d,%02d'% (50,40,30,20)
    num = (rf)
    value  = write_read(num)
    
    
    print(value)
    
    #%02d,%02d,%02d,%02d,%02d,%02d,%02d,%02d,%02d\n' % (rf_command[0],rf_command[1],rf_command[2],rf_command[3],rf_command[4],rf_command[5],rf_command[6],0,0)