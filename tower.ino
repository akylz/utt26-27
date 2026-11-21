void setup() {
  initMotors();
  enableMotors();
}

void loop() {
  for (int i = 1; i < 6; ++i) {
    penUp();
    moveTo(-28, 28 * i);
    penDown();
    magnetOn();
    penUp();
    moveTo(0, 0);
    setPenLevel(i);
    magnetOff();
  }
  moveTo(28 * 5, 0);
  exit(0);
}
