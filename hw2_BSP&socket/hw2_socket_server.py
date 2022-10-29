import socket 
import json
import numpy as np
import matplotlib.pyplot as plot
HOST = '192.168.0.155'     # IP address
PORT = 65431            # Port to listen on (use ports > 1023)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Starting server at: ", (HOST, PORT))
    conn, addr = s.accept()
    with conn:
        print("Connected at", addr)
        while True:
            data = conn.recv(1024).decode('utf-8')
            print("Received from socket server:", data)
            if (data.count('{') != 1):
                # Incomplete data are received.
                choose = 0
                buffer_data = data.split('}')
                while buffer_data[choose][0] != '{':
                    choose += 1
                data = buffer_data[choose] + '}'
                
            obj = json.loads(data)
            t = obj['s']
            
            plot.subplot(4, 3, 1)
            plot.scatter(t, obj['temperature'], c='blue') # temperature, humidity, pressure, magnetox, magnetoy, magnetoz, gyrox, gyroy, gyroz, accelerox, acceleroy, acceleroz
            plot.xlabel("sample num")
            plot.ylabel("temperature")
            plot.title("temperature vs sample num")
            
            plot.subplot(4, 3, 2)
            plot.scatter(t, obj['humidity'], c='blue') # temperature, humidity, pressure, magnetox, magnetoy, magnetoz, gyrox, gyroy, gyroz, accelerox, acceleroy, acceleroz
            plot.xlabel("sample num")
            plot.ylabel("humidity")
            plot.title("humidity vs sample num")
            
            plot.subplot(4, 3, 3)
            plot.scatter(t, obj['pressure'], c='blue') # temperature, humidity, pressure, magnetox, magnetoy, magnetoz, gyrox, gyroy, gyroz, accelerox, acceleroy, acceleroz
            plot.xlabel("sample num")
            plot.ylabel("pressure")
            plot.title("pressure vs sample num")
            
            plot.subplot(4, 3, 4)
            plot.scatter(t, obj['magnetox'], c='blue') # temperature, humidity, pressure, magnetox, magnetoy, magnetoz, gyrox, gyroy, gyroz, accelerox, acceleroy, acceleroz
            plot.xlabel("sample num")
            plot.ylabel("magnetox")
            plot.title("magnetox vs sample num")
            
            plot.subplot(4, 3, 5)
            plot.scatter(t, obj['magnetoy'], c='blue') # temperature, humidity, pressure, magnetox, magnetoy, magnetoz, gyrox, gyroy, gyroz, accelerox, acceleroy, acceleroz
            plot.xlabel("sample num")
            plot.ylabel("magnetoy")
            plot.title("magnetoy vs sample num")
            
            plot.subplot(4, 3, 6)
            plot.scatter(t, obj['magnetoz'], c='blue') # temperature, humidity, pressure, magnetox, magnetoy, magnetoz, gyrox, gyroy, gyroz, accelerox, acceleroy, acceleroz
            plot.xlabel("sample num")
            plot.ylabel("magnetoz")
            plot.title("magnetoz vs sample num")
            
            plot.subplot(4, 3, 7)
            plot.scatter(t, obj['gyrox'], c='blue') # temperature, humidity, pressure, magnetox, magnetoy, magnetoz, gyrox, gyroy, gyroz, accelerox, acceleroy, acceleroz
            plot.xlabel("sample num")
            plot.ylabel("gyrox")
            plot.title("gyrox vs sample num")
            
            plot.subplot(4, 3, 8)
            plot.scatter(t, obj['gyroy'], c='blue') # temperature, humidity, pressure, magnetox, magnetoy, magnetoz, gyrox, gyroy, gyroz, accelerox, acceleroy, acceleroz
            plot.xlabel("sample num")
            plot.ylabel("gyroy")
            plot.title("gyroy vs sample num")
            
            plot.subplot(4, 3, 9)
            plot.scatter(t, obj['gyroz'], c='blue') # temperature, humidity, pressure, magnetox, magnetoy, magnetoz, gyrox, gyroy, gyroz, accelerox, acceleroy, acceleroz
            plot.xlabel("sample num")
            plot.ylabel("gyroz")
            plot.title("gyroz vs sample num")
            
            plot.subplot(4, 3, 10)
            plot.scatter(t, obj['accelerox'], c='blue') # temperature, humidity, pressure, magnetox, magnetoy, magnetoz, gyrox, gyroy, gyroz, accelerox, acceleroy, acceleroz
            plot.xlabel("sample num")
            plot.ylabel("accelerox")
            plot.title("accelerox vs sample num")
            
            plot.subplot(4, 3, 11)
            plot.scatter(t, obj['acceleroy'], c='blue') # temperature, humidity, pressure, magnetox, magnetoy, magnetoz, gyrox, gyroy, gyroz, accelerox, acceleroy, acceleroz
            plot.xlabel("sample num")
            plot.ylabel("acceleroy")
            plot.title("acceleroy vs sample num")
            
            plot.subplot(4, 3, 12)
            plot.scatter(t, obj['acceleroz'], c='blue') # temperature, humidity, pressure, magnetox, magnetoy, magnetoz, gyrox, gyroy, gyroz, accelerox, acceleroy, acceleroz
            plot.xlabel("sample num")
            plot.ylabel("acceleroz")
            plot.title("acceleroz vs sample num")
            
            plot.pause(1)