//Tehtävä 6

//alert('Should I calculate the square root?'));

const answer = confirm('Should I calculate the square root?');

console.log(answer);

  if (answer === true) {
    let numero = prompt("Anna laskettava numero: ");
    var numeroInt = parseInt(numero)
  }
//console.log(Math.sqrt(numero));
  else
    document.querySelector('#t6').innerHTML = "The square root is not calculated.";
    //document.querySelector('#p2').innerHTML = "Laskettu neliöjuuri: " + Math.sqrt(numero) + "!";
    //alert("The square root is not calculated.")


if (numeroInt >= 0) {
  var neljur = Math.sqrt(numeroInt)
  document.querySelector("#t6").innerHTML = "Numeron " + numeroInt + " neliöjuuri on " + neljur }
else if (numeroInt < 0)
  document.querySelector("#t6").innerHTML = "The square root of a negative number " + numeroInt + "  is not defined"

/*
>= 0 = plusluku
< 0 = miinusluku

let numero = prompt("Anna laskettava numero: ");
//console.log(Math.sqrt(numero));
//let numero = neljur;
document.querySelector('#p2').innerHTML = "Laskettu neliöjuuri: "+Math.sqrt(numero)+"!";
*/