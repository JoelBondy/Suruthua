//Zum Abgleich und den Modifikator zu bekommen
const race = {
    "Amaka": 112,
    "Guqual": 101,
    "Avzitil": 94,
    "Vadonier": 87,
    "Elb": 81,
    "Augling": 75,
    "Quork": 73,
    "Draske": 70
};

//leere Arrays um den Durchschnitt der Kategorie zu errechnen
let s = Array(8).fill(1);
let w = Array(10).fill(1);
let k = Array(8).fill(1);
let m = Array(9).fill(1);


//Action wenn eine Zahl geändert wird
function getValue(id) {

    //Geänderte Zahl
    let input = Number(id.value);
    
    //Zahl zurücksetzen falls nicht zwischen 1 und 20
    if (input > 20) {
        input = 20;
        id.value = input;
    }
    else if (input < 0) {
        input = 1;
        id.value = input;
    }
 
    //Welches Attribut in welcher Kategorie geändert wurde
    let section = id.id[0];
    let index = id.id[1]-1;

    //Zahl im entsprechenden Array updaten und dann Durchschnitt der Kategorie gerundet neu berechnen und ändern
    if (section == "s") {
        s[index] = input;
        let aver = s.reduce((a, b) => a+b, 0) / s.length;
        document.getElementById("soziales").innerText = Math.round(aver);
    }
    else if (section == "w") {
        w[index] = input;
        let aver = w.reduce((a, b) => a+b, 0) / w.length;
        document.getElementById("wissen").innerText = Math.round(aver);
    }
   else if (section == "k") {
        k[index] = input;
        let aver = k.reduce((a, b) => a+b, 0) / k.length;
        document.getElementById("korper").innerText = Math.round(aver);
   }
   else if (section == "m") {
        m[index] = input;
        let aver = m.reduce((a, b) => a+b, 0) / m.length;
        document.getElementById("mentales").innerText = Math.round(aver);
   }
};

//Öffne und schließe das Rassenmenü
function klappenregler() {
    document.getElementById("auswahl").classList.toggle("klappeauf");
}

//Schließe Menü wenn woanders hingeklickt wird
window.onclick = function(event) {
    if (!event.target.matches('.klappe')) {
        document.getElementById("auswahl");
        let dropdowns = document.getElementsByClassName("klappezu");
        let i;
        for (i = 0; i < dropdowns.length; i++) {
            let openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('klappeauf')) {
                openDropdown.classList.remove('klappeauf');
            }
        }
    }
}

//Zeige ausgewählte Rasse an
function namechanger(id) {
    document.getElementById("menuanzeige").innerText = id.innerText;
}

