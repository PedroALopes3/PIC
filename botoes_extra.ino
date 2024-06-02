#define BUZZER_PIN 14 // Define o pino do buzzer
#define BUTTON_PIN 17 // Define o pino onde o botão está conectado

void setup() {
  pinMode(BUZZER_PIN, OUTPUT); // Define o pino do buzzer como saída
  pinMode(BUTTON_PIN, INPUT_PULLUP); // Define o pino do botão como entrada com resistor de pull-up interno ativado
}

void loop() {
  // Verifica se o botão foi pressionado
  if (digitalRead(BUTTON_PIN) == LOW) {
    // Emite um som com frequência de 1000 Hz
    
    tone(BUZZER_PIN, 1000); // Liga o buzzer com frequência de 1000 Hz
    delay(100); // Aguarda 500 milissegundos (meio segundo)

    // Para o som
    noTone(BUZZER_PIN); // Desliga o buzzer
  }
}
