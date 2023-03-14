void setup() {
    Serial.begin(9600);
    randomSeed(analogRead(0));
}

void loop() {
    unsigned long millTime = millis();
    int randTemp = random(200);
    int randPres = random(200);

    Serial.println(String(millTime) + ',' + String(randTemp) + ',' + String(randPres));
    delay(200);
}