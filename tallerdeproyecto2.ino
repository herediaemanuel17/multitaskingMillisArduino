/*
 * Esqiema_TP2_1.0
 * 
 * Este programa implementa la funcionalidad de multitasking utilisando 
 * la funcion mullis(), para simular concurrencia.
 * Los elementos a utilizar son: 
 * sensor ultrasonico para medir distancia y un potenciometro que tomara 
 * las graduaciones de giro y se vera reflejado en el servo motor.
 * Todo esto en tiempos de ejecucion diferentes pero al indetectable al ojo humando.
 * 
 */
#include<Servo.h>
#include<Wire.h>

Servo servo; 

const int periodotrabajo = 5;
const int usvcc = 8;
const int usgnd = 11;
const int tri = 9;
const int echo = 10;
const int pote = 0; 
const long int distanciamin = 6;
long int duracion = 0;
long int dista = 0;
long int analogrd;
unsigned long tiempoanterior = 0;
int distant = 0; 
int gradant = 0; 
int anant = 0;
int graduacion = 0;

int uno=1;

/*
 * Funcion distancia()
 * Funcion que mediante la generacion de un pulso ultrasonico en el tri del ultrasonido, el cual rebota y 
 * es detectado con el echo. 
 * Mediante el calculo de tiempo que tarda el pulso en ir, rebotar en un objeto y ser detectado pro el echo 
 * se puede estimar la distancia que se encuentra dicho objeto el cual rebota el pulso.
 *   distancia= duracion/2/29.1
 * returns = long int
 * 
 */
int distancia()
{
 long int dist;
 digitalWrite(tri, LOW);
 delayMicroseconds(2);
 digitalWrite(tri, HIGH);       // Activamos el pulso de salida
 delayMicroseconds(10);             // Esperamos 10µs. El pulso sigue active este tiempo
 digitalWrite(tri, LOW);        // Cortamos el pulso y a esperar el echo
 duracion = pulseIn(echo, HIGH) ;
 dist = duracion / 2 / 29.1  ;          
 return dist;
}

void setup() {
  Serial.begin(9600); //configuracion de velocidad de transferencia en baudios para la comunicacion serial
  servo.attach(7);    //configuracion de los puertos del servo
  
  //configuracion de los puertos para el ultra sonido
  pinMode(usvcc , OUTPUT);  
  pinMode(tri, OUTPUT);
  pinMode(echo, INPUT);
  pinMode(usgnd, INPUT);
  digitalWrite(usvcc, HIGH); //configura el puerto #8 digital como Vcc
  digitalWrite(usgnd, HIGH); //configura el puerto #11 digital como Gnd

  
  tiempoanterior = millis(); //obtiene el tiempo actual transcurrido desde que 
                            //se encendio el arduino mediante la funcion millis()
    
}

void loop() {
 
  if(millis()-tiempoanterior >= periodotrabajo){
    dista = distancia();
    tiempoanterior=millis();
  }
  if(millis()-tiempoanterior >= periodotrabajo){
    if(dista < distanciamin){
      analogrd = analogRead(pote);
      graduacion= analogrd*180/1023;
      servo.write(graduacion);
    }
   tiempoanterior=millis();
  }
  if((millis()-tiempoanterior >= periodotrabajo) && (dista != distant) && (graduacion != gradant) && (analogrd != anant)){
     Serial.println("Distancia/" + String(dista) + "/Grados/" + String(graduacion) + "/potenciometro/" + String(analogrd));
     distant = dista; gradant = graduacion; anant = analogrd;
     tiempoanterior=millis();
  }
}
