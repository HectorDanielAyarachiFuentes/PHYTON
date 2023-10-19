const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('Ingresa la base del triángulo: ', function(base) {
  rl.question('Ingresa la altura del triángulo: ', function(altura) {
    // Convertir los valores a números de punto flotante
    base = parseFloat(base);
    altura = parseFloat(altura);

    // Calcular el área del triángulo
    const area = (base * altura) / 2;

    console.log(`El área del triángulo es: ${area}`);

    rl.close();
  });
});

