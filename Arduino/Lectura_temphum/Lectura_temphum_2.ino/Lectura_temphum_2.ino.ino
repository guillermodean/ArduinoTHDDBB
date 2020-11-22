

/*
  Internet de las cosas III: Monitor de temperatura
  Este programa mide la humedad y temperatura de un sensor DHT
   y manda los resultados por el puerto Serie como una cadena JSOn.
*/
#include <DHT11.h>

int pin=2;
DHT11 dht11(pin); // definir pin


 
void setup() {
  //INicializacion del puerto serie.
  Serial.begin(9600);
 
 
}
 
void loop() {
 
 
  int dato = DHT11.read11(DHT_PIN);//Lectura del dato.
  Serial.print("{\"humidity\":");
  Serial.print(DHT11.humidity);
  Serial.print(",");
  Serial.print("\"temperature\":");
  Serial.print(DHT11.temperature);
  Serial.println("}\n");
  delay(300000);//esperamos 5 minutos.
 
}
