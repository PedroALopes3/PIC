#include <Arduino_LSM6DS3.h>// Biblioteca para recolher os dados do acelerometro e giroscopio */
#include <ArduinoBLE.h>
#include <Wire.h>
#include "MAX30105.h"
#include "heartRate.h"

#define BUZZER_PIN 4 // Define o pino do buzzer
#define BUTTON1_PIN 8 // Define o pino do botão de SOS
#define BUTTON2_PIN 6 // Define o pino do botão de falso positivo

int butPress = 0;
int sosState = -1;


BLEService customService("180D"); // Custom service
BLECharacteristic customCharacteristic("2A37",  // Custom characteristic
                                       BLERead | BLENotify | BLEWrite, // Add BLEWrite to handle incoming messages
                                       64);    // Maximum characteristic length

MAX30105 particleSensor;
const byte RATE_SIZE = 4;
byte rates[RATE_SIZE];
byte rateSpot = 0;
unsigned long lastBeat = 0;

float beatsPerMinute;
int oldbeatAvgLevel = 0;
int auxiliar = 0;
long previousMillis = 0;
int beatAvg;

void setup() {
  Serial.begin(9600);
  //while (!Serial);

  pinMode(BUZZER_PIN, OUTPUT);
  pinMode(BUTTON1_PIN, INPUT_PULLUP);
  pinMode(BUTTON2_PIN, INPUT_PULLUP);

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

  if (!particleSensor.begin(Wire, I2C_SPEED_FAST)) {
    Serial.println("MAX30105 was not found. Please check wiring/power. ");
    while (1);
  }

  Serial.println("Place your sensor on your wrist with steady pressure.");
  particleSensor.setup();
  particleSensor.setPulseAmplitudeRed(60);  // Adjust LED brightness for better wrist readings
  particleSensor.setPulseAmplitudeGreen(0);   // Green LED not used for heart rate monitoring

}

void loop() {
  BLEDevice central = BLE.central();

  String data;

  if (central) {
    Serial.print("Connected to central: ");
    Serial.println(central.address());

    tone(BUZZER_PIN, 1000); // Liga o buzzer com frequência de 1000 Hz
    delay(100); // Aguarda 500 milissegundos (meio segundo)
    noTone(BUZZER_PIN); // Desliga o buzzer


    while (central.connected()) {
      if (customCharacteristic.written()) {
        const uint8_t* receivedValue = customCharacteristic.value();
        size_t length = customCharacteristic.valueLength();
        char value[length + 1];
        memcpy(value, receivedValue, length);
        value[length] = '\0';  // Null-terminate the string
        Serial.print("Received from central: ");
        Serial.println(value);
        if (strcmp(value, "sos") == 0) {
          sosState = 1;
          Serial.println("SOS state activated");
        } else if (strcmp(value, "fp") == 0) {
          sosState = -1;
          Serial.println("False positive state deactivated");
        }
      }

      if (sosState == 1) {
        if (digitalRead(BUZZER_PIN) == LOW) {
          tone(BUZZER_PIN, 500);
          Serial.println("Buzzer ON");
        }
      } else if (sosState == -1){
        noTone(BUZZER_PIN);
        Serial.println("Buzzer OFF");
        sosState = 0;
      }

      String fall = getFallData();

      long irValue = particleSensor.getIR();

      if (checkForBeat(irValue)) 
      {
        unsigned long delta = millis() - lastBeat;
        lastBeat = millis();

        // Calculate heart rate
        beatsPerMinute = 60 / (delta / 1000.0);
        /*
        if(irValue  > 7000)
        {
          //Serial.print("IR=");
          //Serial.print();
          //BPMLevelChar.writeValue(irValue);
          //Serial.print(", BPM=");
          //Serial.print((int)beatsPerMinute);
          //BPMLevelChar.writeValue((int)beatsPerMinute);
          data = fall + "," + String(irValue) + String(beatsPerMinute);
          Serial.println();
        }

        else if( irValue  < 7000)
        {
          Serial.print("IR=");
          Serial.print(irValue);
          Serial.print(", BPM=");
          Serial.print(auxiliar);
          //BPMLevelChar.writeValue(auxiliar);
          data = fall + "," + String(beatsPerMinute);
          Serial.println();
        }*/
      }

      //data = fall + "," + String(beatsPerMinute);

      if (digitalRead(BUTTON1_PIN) == LOW){
        data = data + "," + "1";
      }else if (digitalRead(BUTTON2_PIN) == LOW){
        data = data + "," + "2";
      }else{
        data = data + "," + "0";
      }


      // Send data periodically
      customCharacteristic.writeValue(data.c_str());
    }

    Serial.print("Disconnected from central: ");
    Serial.println(central.address());
    noTone(BUZZER_PIN); // Desliga o buzzer
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
