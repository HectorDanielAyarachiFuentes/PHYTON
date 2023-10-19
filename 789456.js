const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('Ingresa el primer número: ', function(numero1) {
  rl.question('Ingresa el segundo número: ', function(numero2) {
    // Convertir los números a enteros
    numero1 = parseInt(numero1);
    numero2 = parseInt(numero2);

    // Comparar los números
    if (numero1 > numero2) {
      console.log(`${numero1} es mayor que ${numero2}.`);
    } else if (numero1 < numero2) {
      console.log(`${numero1} es menor que ${numero2}.`);
    } else {
      console.log(`${numero1} es igual a ${numero2}.`);
    }

    rl.close();
  });
});
