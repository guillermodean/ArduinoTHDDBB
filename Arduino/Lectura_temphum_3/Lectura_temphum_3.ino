#include <DHT11.h>

int pin=2;
DHT11 dht11(pin); // definir pin

void setup()
   {
       Serial.begin(9600);
   }

void loop()
   {
       int err;
       float temp, hum;
    
       if((err = dht11.read(hum, temp)) == 0)    // Si devuelve 0 es que ha leido bien
          {
             Serial.print("{\"Humedad\":");
             Serial.print(hum);
             Serial.print(",");
             Serial.print("\"Temperatura\":");
             Serial.print(temp);
             Serial.println("}\n");           
             
          }
       else
          {
             Serial.println();
             Serial.print("Error Num :");
             Serial.print(err);
             Serial.println();
          }
       delay(300000);            //Recordad que solo lee una vez cada 5 minutos
   }
