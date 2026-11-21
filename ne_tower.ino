void setup() {
  initMotors();
  enableMotors();
}

void loop() {
  penUp();
  for (int i = 5; i > 0; --i) {
    setPenLevel(i-1);
    magnetOn();
    penUp();
    moveTo(-28, 28 * i);
    penDown();
    magnetOff();
    penUp();
    moveTo(0, 0);
  }
  exit(0);
}
