# from flask import Flask
# import serial
# import json
# app = Flask(__name__)

# @app.route("/")
# def hello():


#     # port = "COM3" 
#     baudrate =9600
#     ports = ('COM3', 'COM3')
    
#     for port in ports:
 
#         try:
#             ser = serial.Serial(port, baudrate=baudrate)
#             print("Serial connection established.")              

#             while True:
#                 line = ser.readline().decode().strip()

#                 if line:
#                     result = str(line)
#                     if result[3:5] =="GS":
#                         container_mode = "on"
#                     else: container_mode = "off"
#                     if result[0:2] == "ST":
#                         weight_stability = "stable"
#                     else: weight_stability = "unstable"
#                     python_obj = {'weight': result[8:13], 'unit of measurement': result[14:], 'container mode': container_mode, 'weight stability': weight_stability}
#                     json_string = json.dumps(python_obj)
#                     break
                

#         except serial.SerialException as se:
#             print("Serial port error:", str(se))
#             continue
            


#         except KeyboardInterrupt:
#             pass

#         finally:
#             if ser.is_open:
#                 ser.close()
#                 print("Serial connection closed.")
#                 print("Your port name - " + str(port))
            
#         print(json_string)
#         print(result)
#         return str(json_string)
    

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=5000)

from flask import Flask
import serial
import json

app = Flask(__name__)

@app.route("/")
def hello():
    ports = ('COM4', 'COM3') 

    for port in ports:
        ser = None  
        try:
            ser = serial.Serial(port, baudrate=9600)
            print(f"Serial connection established on port: {port}")

            while True:
                line = ser.readline().decode().strip()
                if line:
                    result = str(line)
                    print(f"Data received: {result}")

                    container_mode = "off"
                    if result[3:5] == "GS":
                        container_mode = "on"

                    weight_stability = "unstable"
                    if result[0:2] == "ST":
                        weight_stability = "stable"

                    if len(result) >= 15:
                        python_obj = {
                            'weight': result[8:13],
                            'unit of measurement': result[14:],
                            'container mode': container_mode,
                            'weight stability': weight_stability
                        }
                        json_string = json.dumps(python_obj)
                        return str(json_string)  
                    else:
                        print(f"Skipping line {line}: Invalid data format")
                        continue


        except serial.SerialException as se:
            print(f"Serial port error on {port}: {str(se)}")
            continue
        finally:
            if ser and ser.is_open:
                ser.close()
                print(f"Serial connection closed on {port}")

    return "No valid serial data received from any ports." 

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)