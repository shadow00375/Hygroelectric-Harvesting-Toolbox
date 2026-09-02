#include <DHT.h>

#define DHTPIN 2        // Data pin connected to D2
#define DHTTYPE DHT22   // Change to DHT11 if you are using that

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  delay(2000);  // Wait 2 seconds between readings

  float h = dht.readHumidity();
  float t = dht.readTemperature();

  // Check if any reads failed
  if (isnan(h) || isnan(t)) {
    Serial.println("err,err");
    return;
  }

  // Print as CSV: temperature,humidity
  Serial.print(t);
  Serial.print(",");
  Serial.println(h);
}
