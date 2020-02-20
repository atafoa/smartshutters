#include <BLEDevice.h>
#include <BLEUtils.h>
#include <BLEServer.h>

#define SERVICE_UUID        "4fafc201-1fb5-459e-8fcc-c5c9c331914b"
#define CHARACTERISTIC_UUID "beb5483e-36e1-4688-b7f5-ea07361b26a8"
#define speed       2       // Speed Range 10 to 2  10 = lowest , 2 = highest
#define clockwise   0       // Clockwise direction
#define c_clockwise 1       // Counter clockwise direction
#define Motor_data1 32      // Inputs for motor controller
#define Motor_data2 33
#define Motor_data3 25
#define Motor_data4 28
#define Degree_Range 180    // Max Number of degrees
#define ADC_Rotary_input 32 // ADC input from rotary sensor
#define ADC_Rotary_power 33 // Power / Voltage for rotary sensor

int Location = 0;
int CurrentLocation = 0;
String a;

void full_drive (int direction){    // Function to drive motor
    if (direction == c_clockwise){
        //motor_data = 0b0011;
        digitalWrite(Motor_data1, HIGH);
        digitalWrite(Motor_data2, HIGH);
        digitalWrite(Motor_data3, LOW);
        digitalWrite(Motor_data4, LOW);
        delay(speed);
        //motor_data = 0b0110;
        digitalWrite(Motor_data1, LOW);
        digitalWrite(Motor_data2, HIGH);
        digitalWrite(Motor_data3, HIGH);
        digitalWrite(Motor_data4, LOW);
        delay(speed);
        //motor_data = 0b1100;
        digitalWrite(Motor_data1, LOW);
        digitalWrite(Motor_data2, LOW);
        digitalWrite(Motor_data3, HIGH);
        digitalWrite(Motor_data4, HIGH);
        delay(speed);
        //motor_data = 0b1001;
        digitalWrite(Motor_data1, HIGH);
        digitalWrite(Motor_data2, LOW);
        digitalWrite(Motor_data3, LOW);
        digitalWrite(Motor_data4, HIGH);
        delay(speed);
        /////////////////
        digitalWrite(Motor_data1, LOW);
        digitalWrite(Motor_data2, LOW);
        digitalWrite(Motor_data3, LOW);
        digitalWrite(Motor_data4, LOW);
    }
    if (direction == clockwise){
        //motor_data = 0b1100;
        digitalWrite(Motor_data1, LOW);
        digitalWrite(Motor_data2, LOW);
        digitalWrite(Motor_data3, HIGH);
        digitalWrite(Motor_data4, HIGH);
        delay(speed);
        //motor_data = 0b0110;
        digitalWrite(Motor_data1, LOW);
        digitalWrite(Motor_data2, HIGH);
        digitalWrite(Motor_data3, HIGH);
        digitalWrite(Motor_data4, LOW);
        delay(speed);
        //motor_data = 0b0011;
        digitalWrite(Motor_data1, HIGH);
        digitalWrite(Motor_data2, HIGH);
        digitalWrite(Motor_data3, LOW);
        digitalWrite(Motor_data4, LOW);
        delay(speed);
        //motor_data = 0b1001;
        digitalWrite(Motor_data1, HIGH);
        digitalWrite(Motor_data2, LOW);
        digitalWrite(Motor_data3, LOW);
        digitalWrite(Motor_data4, HIGH);
        delay(speed);
        /////////////////
        digitalWrite(Motor_data1, LOW);
        digitalWrite(Motor_data2, LOW);
        digitalWrite(Motor_data3, LOW);
        digitalWrite(Motor_data4, LOW);
    }      
}

void moveto(int newLocation){   // Function for moving the shutter 
    if (CurrentLocation != newLocation){
        // Turn on motor
        while (CurrentLocation > newLocation){
          full_drive(c_clockwise);
          CurrentLocation--;
        }
        while (CurrentLocation < newLocation){
          full_drive(clockwise);
          CurrentLocation++;
        }
        // Turn off motor
    }
}

class MyCallbacks: public BLECharacteristicCallbacks {
    void onWrite(BLECharacteristic *pCharacteristic) {
      std::string value = pCharacteristic->getValue();

      if (value.length() > 0) {

        digitalWrite(ADC_Rotary_power, HIGH);                               // Turn on power for the rotary sensor
        CurrentLocation = Degree_Range*analogRead(ADC_Rotary_input)/4095;   // Read Value from the rotary sensor
        digitalWrite(ADC_Rotary_power, LOW);                                // Turn off power for the rotary sensor
        
        Serial.println("**********");
        a=value.c_str();
        Location = a.toInt();

        if (a == "Battery\r\n") {
            
          // turn on switch for battery check
          // check battery status
          // turn off switch for battery check     
        
          Serial.print("Battery Level: ");
          if (CurrentLocation > 45){    // WILL NEED TO BE CHANGED LATER / current location used for testing
            Serial.print("Good");
            pCharacteristic->setValue("Battery Level: Good");
          }
          if (CurrentLocation < 46){    // WILL NEED TO BE CHANGED LATER / current location used for testing
            Serial.print("Bad");
            pCharacteristic->setValue("Battery Level: Bad");
          }
          pCharacteristic->notify(); // Send the text to the app!
          Location = -1;  // Placed to skip next if statement
        }
      
        if (Location >= 0 && Location <= Degree_Range) {
          
          Serial.print("Desired Position: ");
          Serial.print(a);
          
          Serial.print("Current Position: ");
          Serial.print(CurrentLocation);
          
          Serial.print("\n   Difference   : ");
          Serial.print(Location - CurrentLocation);
          
          moveto(Location);

          //Serial.print("\n New Position : ");
          //Serial.print(CurrentLocation);
  
          pCharacteristic->setValue("Moving to ");
          pCharacteristic->notify();
          pCharacteristic->setValue(value);
          pCharacteristic->notify();
        }

        Serial.println();
        Serial.println("**********");
        
        //pCharacteristic->setValue(a);
        //pCharacteristic->notify(); 
      }
      
    }
};

void setup() {
  Serial.begin(115200);

  pinMode(Motor_data1, OUTPUT);
  pinMode(Motor_data2, OUTPUT);
  pinMode(Motor_data3, OUTPUT);
  pinMode(Motor_data4, OUTPUT);
  pinMode(ADC_Rotary_power, OUTPUT);
  
  Serial.println("\nConnect to ESP32 Motor\n");
  BLEDevice::init("ESP32 Motor");
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
  //put your main code here, to run repeatedly:
  //digitalWrite(ADC_Rotary_power, HIGH);
  //delay(50);
  //CurrentLocation = Degree_Range*analogRead(ADC_Rotary_input)/4095;
  //digitalWrite(ADC_Rotary_power, LOW);
  //Serial.println(CurrentLocation);
  //delay(1000); 
}
