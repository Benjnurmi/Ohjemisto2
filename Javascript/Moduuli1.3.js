//Tehtävä 3 Javascript Laskee

let x = parseInt(prompt("Anna ensimmäinen numero."));
let y = parseInt(prompt("Anna toinen numero."));
let z = parseInt(prompt("Anna kolmas numero."));

alert("Antamasi numerot: "+x+", "+y+", & "+z);

let sum = x + y + z;
let product = x * y * z;
let average = sum / 3;

document.querySelector('#t3').innerHTML = "Numerot yhteensä: "+sum+"!";
document.querySelector('#t3').innerHTML = "Numerot kerrottuna: "+product+"!";
document.querySelector('#t3').innerHTML = "Numeroiden keskiarvo: "+average+"!";

/*
Arvot & Idea
let numero1 = prompt("Ensimmäinen numero");
let numero2 = prompt("Toinen numero");
let numero3 = prompt("Kolmas numero");

sum = numero1 + numero2 + numero3;
product = numero1 * numero2 * numero3;
average = sum / 3;
*/