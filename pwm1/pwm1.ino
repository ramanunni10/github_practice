 int x=11;
char incomingByte = '0';
void setup() 
{
  Serial.begin(9600);
  pinMode(13,OUTPUT);

}

void loop() 
{
   if (Serial.available() > 0)
   {
     incomingByte = Serial.read();
   if(incomingByte=='+')
     x=x+1;
   else if(incomingByte=='-')
    x=x-1;
    Serial.println(x); 
   }
   
  digitalWrite(13,HIGH);
  delayMicroseconds(x);
  digitalWrite(13,LOW);
  delayMicroseconds(22-x);
}
