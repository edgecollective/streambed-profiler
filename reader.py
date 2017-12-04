import sys
import glob
import serial


def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result[0]


if __name__ == '__main__':
    #print(serial_ports())
    port=serial_ports()
    print(serial_ports())
    #serial_port = '/dev/ttyACM0';
    baud_rate = 9600; #In arduino, Serial.begin(baud_rate)
    write_to_file_path = "output.txt";

    output_file = open(write_to_file_path, "w+");
    ser = serial.Serial(port, baud_rate)
    ser.close()
    ser.open()
    ser.write("OK")

    while True:
        line = ser.readline();
        line = line.decode("utf-8") #ser.readline returns a binary, convert to string
        print(line);
        output_file.write(line);
    
    
