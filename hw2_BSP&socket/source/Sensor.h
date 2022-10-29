#include "mbed.h"
#include <map>
#include <string>


class Sensor
{
    private:
    float sensor_value = 0;
    int16_t pDataXYZ[3] = {0};
    float pGyroDataXYZ[3] = {0};
    public:
    Sensor();
    ~Sensor();
    void readSensor(std::map<std::string,float>&sensorData);
};
