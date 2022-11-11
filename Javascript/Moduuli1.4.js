//Tehtävä 4 Sortteri Hattu

let name = prompt("Anna nimi")
let stunum = Math.floor(Math.random() *3)+1;

switch (stunum) {
 case 1:
  document.querySelector("#t4").innerHTML = name + " you are Daredevils"
    break;
 case 2:
  document.querySelector("#t4").innerHTML = name + " you are Slytherin"
    break;
 case 3:
  document.querySelector("#t4").innerHTML = name + " you are Hufflepuff"
    break;
 case 4:
  document.querySelector("#t4").innerHTML = name + " you are Ravenclaw"
    break;
 default:
  document.querySelector("#t4").innerHTML = name + " you are a pumpking"
}

/*
switch(expression) {
  case x:
    // code block
    break;
  case y:
    // code block
    break;
  default:
    // code block
}
*/