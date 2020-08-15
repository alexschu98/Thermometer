const int LM35_PIN = A1;

int i = 0;

void setup() {
  Serial.begin(9600);  
}

void loop() {

  int adc_value;
  float temp;

  adc_value = analogRead(LM35_PIN);
  temp      = (adc_value * 4.88f);
  temp /= 10;

  Serial.print(i);
  Serial.print(',');
  Serial.print(temp);
  Serial.print('\n');

  i++;
  delay(1000);
}
