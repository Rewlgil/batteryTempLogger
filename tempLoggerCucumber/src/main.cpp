#include <Arduino.h>
#include <OneWire.h>
#include <DallasTemperature.h>

#define ONE_WIRE_BUS 17

OneWire oneWire(ONE_WIRE_BUS);

DallasTemperature sensors(&oneWire);

// DeviceAddress device_address;
const uint8_t sensor_address[][8] = {
  {0x28, 0xad, 0x4f, 0x3a, 0x53, 0x21, 0x01, 0x19},
  {0x28, 0x2d, 0x00, 0x9f, 0x54, 0x21, 0x01, 0x27},
  {0x28, 0xc9, 0x9a, 0x2e, 0x54, 0x21, 0x01, 0xc6},
  {0x28, 0x41, 0x58, 0x11, 0x55, 0x21, 0x01, 0x55},
  {0x28, 0x2a, 0x16, 0x92, 0x54, 0x21, 0x01, 0xdf},
  {0x28, 0xb5, 0x45, 0xe6, 0x53, 0x21, 0x01, 0x4d},
  {0x28, 0x1b, 0xe6, 0x58, 0x54, 0x21, 0x01, 0x81},
  {0x28, 0x45, 0xe6, 0x0c, 0x55, 0x21, 0x01, 0xc1},
  {0x28, 0x02, 0x0b, 0x48, 0x53, 0x21, 0x01, 0x38}
};

void setup(void)
{
  Serial.begin(115200);
  sensors.begin();

  // pinMode(0, INPUT_PULLUP);
}

void loop(void)
{
  // Serial.print("Requesting temperatures...");
  sensors.requestTemperatures();
  // Serial.println("DONE");
  for (size_t i = 0; i < 9; i++)
  {
    // float tempC = sensors.getTempCByIndex(i);
    float tempC = sensors.getTempC(sensor_address[i]);

    if (tempC != DEVICE_DISCONNECTED_C)
    {
      // Serial.printf("Temperature for the device %d is: %.1f\n", i, tempC);
      Serial.printf("%.1f", tempC);
    }
    else
    {
      // Serial.println("Error: Could not read temperature data");
      Serial.printf("0");
    }
    Serial.print(i < 8 ? "," : "\n");
  }
  delay(5000);

  // if (digitalRead(0) == LOW) {
  //   if (sensors.getAddress(device_address, 0)) {
  //     for (size_t i = 0; i < 8; i++) {
  //       uint8_t tmp = device_address[i];
  //       Serial.print((tmp <= 0xF ? "0" : "") + String(tmp, HEX));
  //     }
  //     Serial.println();
  //   }
  //   delay(100);
  //   while(digitalRead(0) == LOW) delay(10);
  // }
}
