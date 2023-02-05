# include<Servo.h>
Servo
myservo;
const
int
trigPin = 3;
const
int
echoPin = 5;
long
tmeduration;
int
distance;

void
setup()
{
    myservo.attach(9);
pinMode(trigPin, OUTPUT);
pinMode(echoPin, INPUT);
Serial.begin(9600);

pinMode(2, OUTPUT); // 2
2
g

pinMode(4, OUTPUT); // 3
y

pinMode(6, OUTPUT); // 4
r

pinMode(7, OUTPUT); // 5
g

pinMode(8, OUTPUT); // 6
y

pinMode(10, OUTPUT); // 7
r

pinMode(11, OUTPUT); // 8
g

pinMode(12, OUTPUT); // 9
y

pinMode(13, OUTPUT); // 10
r
}

void
loop()
{
    digitalWrite(trigPin, LOW);
delayMicroseconds(2);
digitalWrite(trigPin, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin, LOW);

tmeduration = pulseIn(echoPin, HIGH);
distance = (0.034 * tmeduration) / 2;

if (distance <= 10)
{

    myservo.write(90);
}
else {
    myservo.write(0);}

Serial.print("distance:");
Serial.println(distance);

delay(1);

if (distance <= 20)
{
    digitalWrite(2, 1); // enables
the
1
st
set
of
signals

digitalWrite(10, 1);

digitalWrite(13, 1);

digitalWrite(4, 0);

digitalWrite(7, 0);

digitalWrite(6, 0);

digitalWrite(8, 0);

digitalWrite(12, 0);

digitalWrite(11, 0);

delay(10000);

digitalWrite(4, 1); // enables
the
yellow
lights

digitalWrite(8, 1);

digitalWrite(2, 0);

digitalWrite(13, 0);

delay(1500);

digitalWrite(6, 1); // enables
the
2
nd
set
of
signals

digitalWrite(7, 1);

digitalWrite(13, 1);

digitalWrite(2, 0);

digitalWrite(4, 0);

digitalWrite(8, 0);

digitalWrite(11, 0);

digitalWrite(12, 0);

digitalWrite(10, 0);

delay(5000);

digitalWrite(12, 1); // enables
the
yellow
lights

digitalWrite(8, 1);

digitalWrite(13, 0);

digitalWrite(7, 0);

digitalWrite(6, 0);

delay(1500);

digitalWrite(11, 1); // enables
the
3
rd
set
of
signals

digitalWrite(6, 1);

digitalWrite(10, 1);

digitalWrite(2, 0);

digitalWrite(4, 0);

digitalWrite(7, 0);

digitalWrite(8, 0);

digitalWrite(12, 0);

digitalWrite(13, 0);

delay(5000);

digitalWrite(12, 1); // enables
the
yellow
lights

digitalWrite(4, 1);

digitalWrite(10, 0);

digitalWrite(11, 0);

digitalWrite(6, 0);

delay(1500);
}
else {
    digitalWrite(2, 1); // enables
the
1
st
set
of
signals

digitalWrite(10, 1);

digitalWrite(13, 1);

digitalWrite(4, 0);

digitalWrite(7, 0);

digitalWrite(6, 0);

digitalWrite(8, 0);

digitalWrite(12, 0);

digitalWrite(11, 0);

delay(1000);

digitalWrite(4, 1); // enables
the
yellow
lights

digitalWrite(8, 1);

digitalWrite(2, 0);

digitalWrite(13, 0);

delay(1500);

digitalWrite(6, 1); // enables
the
2
nd
set
of
signals

digitalWrite(7, 1);

digitalWrite(13, 1);

digitalWrite(2, 0);

digitalWrite(4, 0);

digitalWrite(8, 0);

digitalWrite(11, 0);

digitalWrite(12, 0);

digitalWrite(10, 0);

delay(1000);

digitalWrite(12, 1); // enables
the
yellow
lights

digitalWrite(8, 1);

digitalWrite(13, 0);

digitalWrite(7, 0);

digitalWrite(6, 0);

delay(1500);

digitalWrite(11, 1); // enables
the
3
rd
set
of
signals

digitalWrite(6, 1);

digitalWrite(10, 1);

digitalWrite(2, 0);

digitalWrite(4, 0);

digitalWrite(7, 0);

digitalWrite(8, 0);

digitalWrite(12, 0);

digitalWrite(13, 0);

delay(1000);

digitalWrite(12, 1); // enables
the
yellow
lights

digitalWrite(4, 1);

digitalWrite(10, 0);

digitalWrite(11, 0);

digitalWrite(6, 0);

delay(1500);
}

}