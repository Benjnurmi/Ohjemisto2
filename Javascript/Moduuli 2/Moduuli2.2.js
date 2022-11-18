// Osallistujien nimet

let osall = prompt("Montako osallistujaa?")
let Particints = parseInt(osall)

let partici = []
for (let i = 0; i < Particints; i++) {
  let nimet = prompt("Anna nimi")
  partici.push(nimet)
}
partici.sort()
console.log(partici)

// HTML printti
// document.querySelector('#t1').innerHTML = 'Heiti noppaa '+partici+' kertaa saadaksesi silmäluvun 6';