void setup() {
  initMotors();
  enableMotors();
  penUp();
}

void loop() {
  penDown();
  magnetOn();
  penUp();
  moveTo(-28 * 6, 28 * 3);
  penDown();
  magnetOff();
  penUp();
  exit(0);
}
