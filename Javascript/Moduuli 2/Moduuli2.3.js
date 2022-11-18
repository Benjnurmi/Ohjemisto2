// Kuusi koiraa

let koirat;
koirat = []

let i;
for (i = 0; i < 6; i++) {
  let koira = prompt("Anna koiran nimi")
  koirat.push(koira)
}

koirat.sort()
koirat.reverse()

document.querySelector("#t3").innerHTML = koirat