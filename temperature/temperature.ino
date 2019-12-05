void setup() {
  Serial.begin(9600);
}

void loop() {
  byte adc = 0;
  for (int i = 2; i  < 10; ++i) {
    if(digitalRead(i) == HIGH){
      adc |= (1 << (i - 2));
    }
  }

  Serial.println(adc);
  delay(3000);
}
