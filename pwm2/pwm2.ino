int sensorPin = A0;
int on_time=0;
float duty=79.67;
int ledPin = 13;    
float sensorValue=0;
float voltage = 0;
const int period=22;
void setup() 
{
    Serial.begin(9600);
    pinMode(ledPin, OUTPUT);
     digitalWrite(ledPin, LOW);
}

void loop() 
{
  sensorValue = analogRead(sensorPin);
  voltage=(sensorValue*5)/1023;
  //on_time=(voltage/5)*22;
  
   if(voltage<2.5)
      on_time++;   
   else if(voltage>2.5)
      on_time--;
    duty=(100/22)*on_time;
    
    Serial.print(duty);
    Serial.print("   ");
    Serial.print(voltage);
    Serial.print("   ");
    Serial.print(on_time);
    Serial.print("\r");
    
  // on_time=(22/100)*duty;
  digitalWrite(ledPin, HIGH);
  delayMicroseconds(on_time);
  digitalWrite(ledPin, LOW);
 delayMicroseconds(period-on_time);
}
