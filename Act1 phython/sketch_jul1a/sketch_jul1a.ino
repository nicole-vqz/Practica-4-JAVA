#define LED1 18
#define LED2 19

String cad;

void setup() {
  Serial.begin(9600);
  
  // Configurar ambos pines como salidas
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  
  Serial.println("Sistema listo. Usa los comandos: ON1, OFF1, ON2, OFF2");
}

void loop() {
  if (Serial.available() > 0) {
    cad = Serial.readStringUntil('\n');
    cad.trim(); // Elimina espacios y saltos de línea (\r, \n)

    // --- Control del LED 1 ---
    if (cad == "ON1") {
      digitalWrite(LED1, HIGH);
    }
    else if (cad == "OFF1") {
      digitalWrite(LED1, LOW);
    }
    
    // --- Control del LED 2 ---
    else if (cad == "ON2") {
      digitalWrite(LED2, HIGH);
    }
    else if (cad == "OFF2") {
      digitalWrite(LED2, LOW);
    }

    Serial.println(cad);
  }

  delay(50); 
}