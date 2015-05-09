const int sensorPin = A0;
const int ledPin = 13;
const int MAX_VALUES = 1;

float windSpeed[MAX_VALUES];

const float AnemometerMinVolt = 0.4;
const float AnemometerMaxVolt = 2.0;
const float AnemometerMinWindSpeed = 0.0;
const float AnemometerMaxWindSpeed = 70.0;

void setup() {
  pinMode(ledPin,OUTPUT);
  Serial.begin(9600);
  
  for (int i = 0; i < MAX_VALUES; i++)
    windSpeed[i] = 0.0;
}

float convertToVolt(int value){
  return value*(5.0/1023.0);
}

float convertToWindSpeed(float v){
  float a = (AnemometerMaxVolt - AnemometerMinVolt)/(AnemometerMaxWindSpeed - AnemometerMinWindSpeed);
  float b = AnemometerMinWindSpeed - (AnemometerMinVolt*a);
  float result = a*v + b;
  if (result < 0)
    result = 0;
  return result;
}

void transmitWindSpeed(String separator){
  String str = "";
   for (int i = 0; i < MAX_VALUES; i++){
     String valueStr = String(windSpeed[i]);
     str += valueStr;
     if (i < MAX_VALUES-1)
       str += separator;
   }
   Serial.println(str);
   delay(100);
}

void push_wind_speed(float v){
  for (int i = MAX_VALUES; i > 0; i--){
    windSpeed[i] = windSpeed[i-1];
  }
  windSpeed[0] = v;
}

float get_mean_value(){
  float aux = 0;
  for (int i = 0; i < MAX_VALUES; i++)
      aux += windSpeed[i];
      
  return aux/MAX_VALUES;
}

float readAnemometer(){
  float sensorValue = analogRead(sensorPin);
  float volt = convertToVolt(sensorValue);
  //return volt;
  return convertToWindSpeed(volt);
}

void loop() {
  // put your main code here, to run repeatedly:
  delay(100);
  push_wind_speed(readAnemometer());
  transmitWindSpeed(",");
  
  delay(1000);
}
