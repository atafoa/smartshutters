/*
    Based on Neil Kolban example for IDF: https://github.com/nkolban/esp32-snippets/blob/master/cpp_utils/tests/BLE%20Tests/SampleWrite.cpp
    Ported to Arduino ESP32 by Evandro Copercini
*/

#include <BLEDevice.h>
#include <BLEUtils.h>
#include <BLEServer.h>

// See the following for generating UUIDs:
// https://www.uuidgenerator.net/

#define SERVICE_UUID        "4fafc201-1fb5-459e-8fcc-c5c9c331914b"
#define CHARACTERISTIC_UUID "beb5483e-36e1-4688-b7f5-ea07361b26a8"
#define speed       2       // Speed Range 10 to 1  10 = lowest , 1 = highest
#define step        2000       // how many steps to take
#define clockwise   0       // clockwise direction macro
#define c_clockwise 1       // anti clockwise direction macro

int data1 = 12;
int data2 = 26;
int data3 = 33;
int data4 = 32;
int location = 0;
char recval[40];

void full_drive (int direction){
    if (direction == c_clockwise){
        //motor_data = 0b0011;
        digitalWrite(data1,LOW);
        //LCD_short_busy();
        digitalWrite(data2,LOW);
        //LCD_short_busy();
        digitalWrite(data3,HIGH);
        //LCD_short_busy();
        digitalWrite(data4,HIGH);
        delay(speed);
        //motor_data = 0b0110;
        digitalWrite(data1,LOW);
        //LCD_short_busy();
        digitalWrite(data2,HIGH);
        //LCD_short_busy();
        digitalWrite(data3,HIGH);
        //LCD_short_busy();
        digitalWrite(data4,LOW);
        delay(speed);
        //motor_data = 0b1100;
        digitalWrite(data1,HIGH);
        //LCD_short_busy();
        digitalWrite(data2,HIGH);
        //LCD_short_busy();
        digitalWrite(data3,LOW);
        //LCD_short_busy();
        digitalWrite(data4,LOW);
        delay(speed);
        //motor_data = 0b1001;
        digitalWrite(data1,HIGH);
        //LCD_short_busy();
        digitalWrite(data2,LOW);
        //LCD_short_busy();
        digitalWrite(data3,LOW);
        //LCD_short_busy();
        digitalWrite(data4,HIGH);
        delay(speed);
        
        /////////////////
        //digitalWrite(data1,LOW);
        //LCD_short_busy();
        //digitalWrite(data2,LOW);
        //LCD_short_busy();
        //digitalWrite(data3,LOW);
        //LCD_short_busy();
        //digitalWrite(data4,LOW);
        //LCD_short_busy();
    }
    if (direction == clockwise){
        //motor_data = 0b1100;
        digitalWrite(data1,HIGH);
        //LCD_short_busy();
        digitalWrite(data2,HIGH);
        //LCD_short_busy();
        digitalWrite(data3,LOW);
        //LCD_short_busy();
        digitalWrite(data4,LOW);
        delay(speed);
        //motor_data = 0b0110;
        digitalWrite(data1,LOW);
        //LCD_short_busy();
        digitalWrite(data2,HIGH);
        //LCD_short_busy();
        digitalWrite(data3,HIGH);
        //LCD_short_busy();
        digitalWrite(data4,LOW);
        delay(speed);
        //motor_data = 0b0011;
        digitalWrite(data1,LOW);
        //LCD_short_busy();
        digitalWrite(data2,LOW);
        //LCD_short_busy();
        digitalWrite(data3,HIGH);
        //LCD_short_busy();
        digitalWrite(data4,HIGH);
        delay(speed);
        //motor_data = 0b1001;
        digitalWrite(data1,HIGH);
        //LCD_short_busy();
        digitalWrite(data2,LOW);
        //LCD_short_busy();
        digitalWrite(data3,LOW);
        //LCD_short_busy();
        digitalWrite(data4,HIGH);
        delay(speed);
        
        /////////////////
        //digitalWrite(data1,LOW);
        //LCD_short_busy();
        //digitalWrite(data2,LOW);
        //LCD_short_busy();
        //digitalWrite(data3,LOW);
        //LCD_short_busy();
        //digitalWrite(data4,LOW);
        //LCD_short_busy();
    }      
}


void moveto(int newlocation){
    
    while (location > newlocation){
        full_drive(c_clockwise);
        location--;
    }
    while (location < newlocation){
        full_drive(clockwise);
        location++;
    }
}
    
    

void LED(std::string value) {

  //strcpy(value, recval);

  if (value == "BLUE") {
    Serial.println("*********");
    Serial.print("New value: ");
    for (int i = 0; i < value.length(); i++)
      Serial.print(value[i]);

    Serial.println();
    Serial.println("*********");

    //digitalWrite(BLUE_motor_data2, HIGH);
    //delay(1000);
    //digitalWrite(BLUE_motor_data2, LOW);
    moveto(0);
  }

  if (value == "GREEN") {
    Serial.println("*********");
    Serial.print("New value: ");
    for (int i = 0; i < value.length(); i++)
      Serial.print(value[i]);

    Serial.println();
    Serial.println("*********");

    //digitalWrite(GREEN_motor_data3, HIGH);
    //delay(1000);
    //digitalWrite(GREEN_motor_data3, LOW);
    moveto(128);
  }

  if (value == "RED") {
    Serial.println("*********");
    Serial.print("New value: ");
    for (int i = 0; i < value.length(); i++)
      Serial.print(value[i]);

    Serial.println();
    Serial.println("*********");

    //digitalWrite(GREEN, HIGH);
    //delay(1000);
    //digitalWrite(GREEN, LOW);
    moveto(256);
  }

  if (value == "PURPLE") {
    Serial.println("*********");
    Serial.print("New value: ");
    for (int i = 0; i < value.length(); i++)
      Serial.print(value[i]);

    Serial.println();
    Serial.println("*********");

    //digitalWrite(GREEN, HIGH);
    //delay(1000);
    //digitalWrite(GREEN, LOW);
    moveto(location+128);
  }

}


class MyCallbacks: public BLECharacteristicCallbacks {
    void onWrite(BLECharacteristic *pCharacteristic) {
      std::string value = pCharacteristic->getValue();

      //esp_sleep_enable_X_wakeup();


      
            if (value.length() > 0) {     
              LED(value);
            }

//      if (value == "BLUE_motor_data2") {
//        Serial.println("*********");
//        Serial.print("New value: ");
//        for (int i = 0; i < value.length(); i++)
//          Serial.print(value[i]);
//
//        Serial.println();
//        Serial.println("*********");
//
//        digitalWrite(BLUE_motor_data2, HIGH);
//        delay(1000);
//        digitalWrite(BLUE_motor_data2, LOW);
//      }
//
//      if (value == "GREEN_motor_data3") {
//        Serial.println("*********");
//        Serial.print("New value: ");
//        for (int i = 0; i < value.length(); i++)
//          Serial.print(value[i]);
//
//        Serial.println();
//        Serial.println("*********");
//
//        digitalWrite(GREEN_motor_data3, HIGH);
//        delay(1000);
//        digitalWrite(GREEN_motor_data3, LOW);
//      }
//
//      if (value == "GREEN") {
//        Serial.println("*********");
//        Serial.print("New value: ");
//        for (int i = 0; i < value.length(); i++)
//          Serial.print(value[i]);
//
//        Serial.println();
//        Serial.println("*********");
//
//        digitalWrite(GREEN, HIGH);
//        delay(1000);
//        digitalWrite(GREEN, LOW);
//      }


    }
};

void setup() {
  Serial.begin(115200);

  pinMode(data2, OUTPUT);
  pinMode(data3, OUTPUT);
  pinMode(data1, OUTPUT);
  pinMode(data4, OUTPUT);

  Serial.println("1- Download and install an BLE scanner app in your phone");
  Serial.println("2- Scan for BLE devices in the app");
  Serial.println("3- Connect to MyESP32");
  Serial.println("4- Go to CUSTOM CHARACTERISTIC in CUSTOM SERVICE and write something");
  Serial.println("5- See the magic =)");

  BLEDevice::init("MyESP32");
  BLEServer *pServer = BLEDevice::createServer();

  BLEService *pService = pServer->createService(SERVICE_UUID);

  BLECharacteristic *pCharacteristic = pService->createCharacteristic(
                                         CHARACTERISTIC_UUID,
                                         BLECharacteristic::PROPERTY_READ |
                                         BLECharacteristic::PROPERTY_WRITE
                                       );

  pCharacteristic->setCallbacks(new MyCallbacks());

  pCharacteristic->setValue("Hello World");
  pService->start();

  BLEAdvertising *pAdvertising = pServer->getAdvertising();
  pAdvertising->start();
}







void loop() {
  //  esp_deep_sleep_start();
  //  getValue();
  //
  //  if (value == "BLUE_motor_data2") {
  //        digitalWrite(BLUE_motor_data2, HIGH);
  //        delay(1000);
  //        digitalWrite(BLUE_motor_data2, LOW);
  //  delay(2000);
  //  }
}