void setup() {
  initMotors();
  enableMotors();
}

void loop() {
  penUp();
  moveXmm(-28 * 4);
  moveXmm(28 * 4);
  moveYmm(28 * 4);
  moveYmm(-28 * 4);
  moveTo(-28 * 6, 28 * 3);
  penDown();
  penUp();
  exit(0);
}
