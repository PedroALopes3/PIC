#include <Arduino_LSM6DS3.h>// Biblioteca para recolher os dados do acelerometro e giroscopio */
#include <ArduinoBLE.h>

BLEService customService("180D"); // Custom service
BLECharacteristic customCharacteristic("2A37",  // Custom characteristic
                                       BLERead | BLENotify | BLEWrite, // Add BLEWrite to handle incoming messages
                                       64);    // Maximum characteristic length

void setup() {
  Serial.begin(9600);
  while (!Serial);

  if (!BLE.begin()) { // Erro para ligar o Bluetooth
    Serial.println("Starting BLE failed!");
    while (1);
  }

    if (!IMU.begin()) { // Erro para aceder ao acelerometro e giroscopio
    Serial.println("Failed to initialize IMU!");
    while (1);
  }

  BLE.setLocalName("Prototype_ArduinoNano2040"); // Set device name
  BLE.setAdvertisedService(customService); // Advertise the custom service

  customService.addCharacteristic(customCharacteristic); // Add the characteristic to the service
  BLE.addService(customService); // Add the service
  
  BLE.advertise(); // Start advertising

  Serial.println("Bluetooth device active, waiting for connections...");
}

void loop() {
  BLEDevice central = BLE.central();

  if (central) {
    Serial.print("Connected to central: ");
    Serial.println(central.address());

    while (central.connected()) {
      if (customCharacteristic.written()) {
        const uint8_t* receivedValue = customCharacteristic.value();
        size_t length = customCharacteristic.valueLength();
        char value[length + 1];
        memcpy(value, receivedValue, length);
        value[length] = '\0';  // Null-terminate the string
        Serial.print("Received from central: ");
        Serial.println(value);
      }

      String fall = getFallData();

      // Send data periodically
      customCharacteristic.writeValue(fall.c_str());
      delay(1000);
    }

    Serial.print("Disconnected from central: ");
    Serial.println(central.address());
  }
}

String getFallData() {
  float Ax, Ay, Az;
  float Gx, Gy, Gz;

  if (IMU.accelerationAvailable()) {
    IMU.readAcceleration(Ax, Ay, Az);
  }

  if (IMU.gyroscopeAvailable()) {
    IMU.readGyroscope(Gx, Gy, Gz);    
  }

  String dataString = String(millis()) + "," + 
                      String(Ax) + "," + 
                      String(Ay) + "," + 
                      String(Az) + "," + 
                      String(Gx) + "," + 
                      String(Gy) + "," + 
                      String(Gz);
  
  return dataString;
}
