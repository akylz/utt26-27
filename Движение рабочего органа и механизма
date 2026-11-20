#include <Servo.h>
#include <math.h>

// ==================== КОНСТАНТЫ И НАСТРОЙКИ ====================
#define STEPS_PER_MM_X 77.8
#define STEPS_PER_MM_Y 77.4

// ==================== СКОРОСТЬ ====================
#define STEP_DELAY_US 100

// ==================== СЕРВОПРИВОД ====================
Servo s;
#define SERVO_PIN 9

// ==================== ПИНЫ МОТОРОВ ====================
#define STEPX 41
#define DIRX 40
#define ENX 36
#define MS1_X 39
#define MS2_X 38

#define STEPY 34
#define DIRY 37
#define ENY 33
#define MS1_Y 32
#define MS2_Y 35

#define MAGNET_PIN 31

// ==================== ПЕРЕМЕННЫЕ ====================
float currentX = 0.0;
float currentY = 0.0;

// ==================== ИНИЦИАЛИЗАЦИЯ ====================
void initMotors() {
  pinMode(MAGNET_PIN, OUTPUT);
  digitalWrite(MAGNET_PIN, LOW);

  s.attach(SERVO_PIN);

  pinMode(STEPX, OUTPUT);
  pinMode(DIRX, OUTPUT);
  pinMode(ENX, OUTPUT);
  pinMode(MS1_X, OUTPUT);
  pinMode(MS2_X, OUTPUT);

  pinMode(STEPY, OUTPUT);
  pinMode(DIRY, OUTPUT);
  pinMode(ENY, OUTPUT);
  pinMode(MS1_Y, OUTPUT);
  pinMode(MS2_Y, OUTPUT);

  digitalWrite(MS1_X, HIGH);
  digitalWrite(MS2_X, HIGH);
  digitalWrite(MS1_Y, HIGH);
  digitalWrite(MS2_Y, HIGH);

  digitalWrite(ENX, HIGH);
  digitalWrite(ENY, HIGH);
}

void enableMotors() {
  digitalWrite(ENX, LOW);
  digitalWrite(ENY, LOW);
}

void disableMotors() {
  digitalWrite(ENX, HIGH);
  digitalWrite(ENY, HIGH);
}

// ==================== УПРАВЛЕНИЕ СЕРВОПРИВОДОМ ====================
void setPenLevel(int level) {
  int targetAngle = 90 + (level * 18);
  int currentAngle = s.read();

  if (targetAngle > currentAngle) {
    for (int angle = currentAngle; angle <= targetAngle; angle++) {
      s.write(angle);
      delay(10);
    }
  } else {
    for (int angle = currentAngle; angle >= targetAngle; angle--) {
      s.write(angle);
      delay(10);
    }
  }
}

void penDown() {
  setPenLevel(1);
}

void penUp() {
  setPenLevel(5);
}

// ==================== ДВИЖЕНИЕ ПО ОСЯМ (ОДНООСЕВОЕ) ====================
void moveXRaw(long steps) {
  if (steps == 0) return;

  bool direction = steps > 0;
  digitalWrite(DIRX, direction ? HIGH : LOW);
  delayMicroseconds(5);

  for (long i = 0; i < abs(steps); i++) {
    digitalWrite(STEPX, HIGH);
    delayMicroseconds(STEP_DELAY_US);
    digitalWrite(STEPX, LOW);
    delayMicroseconds(STEP_DELAY_US);
  }

  currentX += (float)steps / STEPS_PER_MM_X;
}

void moveYRaw(long steps) {
  if (steps == 0) return;

  bool direction = steps > 0;
  digitalWrite(DIRY, direction ? HIGH : LOW);
  delayMicroseconds(5);

  for (long i = 0; i < abs(steps); i++) {
    digitalWrite(STEPY, HIGH);
    delayMicroseconds(STEP_DELAY_US);
    digitalWrite(STEPY, LOW);
    delayMicroseconds(STEP_DELAY_US);
  }

  currentY += (float)steps / STEPS_PER_MM_Y;
}

void moveXmm(float mm) {
  moveXRaw((long)(mm * STEPS_PER_MM_X));
}

void moveYmm(float mm) {
  moveYRaw((long)(mm * STEPS_PER_MM_Y));
}

// ==================== СИНХРОННОЕ ВЕКТОРНОЕ ДВИЖЕНИЕ ====================
void moveVector(float deltaX, float deltaY) {
  long dx = round(deltaX * STEPS_PER_MM_X);
  long dy = round(deltaY * STEPS_PER_MM_Y);

  digitalWrite(DIRX, (dx > 0) ? HIGH : LOW);
  digitalWrite(DIRY, (dy > 0) ? HIGH : LOW);
  delayMicroseconds(5);

  long aX = abs(dx);
  long aY = abs(dy);

  long errX = 0;
  long errY = 0;

  long maxT = max(aX, aY);

  for (long i = 0; i < maxT; i++) {
    bool makeStepX = false;
    bool makeStepY = false;

    errX += aX;
    if (errX >= maxT) {
      makeStepX = true;
      errX -= maxT;
    }

    errY += aY;
    if (errY >= maxT) {
      makeStepY = true;
      errY -= maxT;
    }

    if (makeStepX) digitalWrite(STEPX, HIGH);
    if (makeStepY) digitalWrite(STEPY, HIGH);

    delayMicroseconds(STEP_DELAY_US);

    if (makeStepX) digitalWrite(STEPX, LOW);
    if (makeStepY) digitalWrite(STEPY, LOW);

    delayMicroseconds(STEP_DELAY_US);
  }

  currentX += deltaX;
  currentY += deltaY;
}

void moveTo(float targetX, float targetY) {
  float deltaX = targetX - currentX;
  float deltaY = targetY - currentY;
  moveVector(deltaX, deltaY);
}

// ==================== УПРАВЛЕНИЕ ЭЛЕКТРОМАГНИТОМ ====================
void setMagnet(bool state) {
  digitalWrite(MAGNET_PIN, state ? HIGH : LOW);
}

void magnetOn() {
  setMagnet(true);
}

void magnetOff() {
  setMagnet(false);
}
