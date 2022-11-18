// Numeroita nollaan asti

let numbLi;
numbLi = []

let numero = prompt("Anna numero")

numbLi.push(numero)

while (numero == 0) {
  numero = prompt("Anna numero")
  numbLi.push(numero)
}

console.log(numbLi)

/*
Use loop and give condition like this
while (number==0)
Then break;
Otherwise user input continue.
*/
