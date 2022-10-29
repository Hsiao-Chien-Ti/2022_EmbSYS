#include "mbed.h"

// Sensors drivers present in the BSP library
#include "stm32l475e_iot01_tsensor.h"
#include "stm32l475e_iot01_hsensor.h"
#include "stm32l475e_iot01_psensor.h"
#include "stm32l475e_iot01_magneto.h"
#include "stm32l475e_iot01_gyro.h"
#include "stm32l475e_iot01_accelero.h"
#include <map>
#include <string>
#include "Sensor.h"

    Sensor::Sensor()
    {
        printf("Start sensor init\n");

        BSP_TSENSOR_Init();
        BSP_HSENSOR_Init();
        BSP_PSENSOR_Init();

        BSP_MAGNETO_Init();
        BSP_GYRO_Init();
        BSP_ACCELERO_Init();
    }
    Sensor::~Sensor()
    {

    }
    
    void Sensor::readSensor(std::map<std::string,float>&sensorData)
    {
        sensor_value = BSP_TSENSOR_ReadTemp();
        sensorData["Temperature"]=sensor_value;

        sensor_value = BSP_HSENSOR_ReadHumidity();
        sensorData["Humidity"]=sensor_value;

        sensor_value = BSP_PSENSOR_ReadPressure();
        sensorData["Pressure"]=sensor_value;

        ThisThread::sleep_for(1s);

        BSP_MAGNETO_GetXYZ(pDataXYZ);
        sensorData["MAGNETO_X"]=pDataXYZ[0];
        sensorData["MAGNETO_Y"]=pDataXYZ[1];
        sensorData["MAGNETO_Z"]=pDataXYZ[2];

        BSP_GYRO_GetXYZ(pGyroDataXYZ);
        sensorData["GYRO_X"]=pGyroDataXYZ[0];
        sensorData["GYRO_Y"]=pGyroDataXYZ[1];
        sensorData["GYRO_Z"]=pGyroDataXYZ[2];

        BSP_ACCELERO_AccGetXYZ(pDataXYZ);
        sensorData["ACCELERO_X"]=pDataXYZ[0];
        sensorData["ACCELERO_Y"]=pDataXYZ[1];
        sensorData["ACCELERO_Z"]=pDataXYZ[2];

        ThisThread::sleep_for(1s);

    }
