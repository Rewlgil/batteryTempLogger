import serial
import datetime

def main():
    ser = serial.Serial('COM7', 115200)
    line_count = 0
    current_time = datetime.datetime.now()
    file_name = "tempLog_" + current_time.strftime("%Y_%m_%d_%H_%M_%S") + ".csv"
    file = open(file_name, 'w')
    file.close()

    try:
        while True:
            if ser.is_open:
                try:
                    line = str(ser.readline()).strip("b'").strip("'\\n")
                    temp = line.split(',')
                    
                    if len(temp) != 9:
                        continue
                    
                    current_time = datetime.datetime.now()
                    current_time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
                    
                    write_line = current_time_str + ", " + ", ".join(temp) + "\n"
                    print(write_line, end='')

                    if line_count >= 1000:
                        file_name = "tempLog_" + current_time.strftime("%Y_%m_%d_%H_%M_%S") + ".csv"
                        line_count = 0

                    file = open(file_name, 'a')
                    file.write(write_line)
                    file.close()
                    line_count += 1
                
                except KeyboardInterrupt:
                    raise
                except:
                    ser.close()
            else:
                try:
                    ser.open()
                except KeyboardInterrupt:
                    raise
                except:
                    pass
        on_exit(ser, file)
    except KeyboardInterrupt:
        on_exit(ser, file)


def on_exit(s, f):
    print('on exit')
    if not f.closed:
        f.close()
    if s.is_open:
        s.close()

if __name__ == '__main__':
    main()
