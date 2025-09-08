int ledPin[] = {8, 9, 10, 11};
int LED_num = 4;
int analogue_pin = A3;
int analogue_val = 0;
int cpt = 0;
void setup() {
  for (int i = 0; i < LED_num; i++) {
    pinMode(ledPin[i], OUTPUT);
  }
}
void loop() {
  analogue_val = analogueRead(analogue_pin);

  digitalWrite(ledPin[cpt], HIGH);

  delay(analogue_val);

  digitalWrite(ledPin[cpt], LOW);

  cpt++;

  if (cpt == LED_num) {
    cpt = 0;
  }
}