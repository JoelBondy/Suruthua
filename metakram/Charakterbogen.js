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
//Insgesamt zu vergeben Punkte
const punkte = 400;

//Arrays mit allen Werten nach Kategorie seprariert
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

   updateWerte();
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
    updateWerte();
}

//Allgemeine Charakterwerte auf dem Laufenden halten
function updateWerte() {
    //Noch zu vergeben Punkte
    let total = (
        s.reduce((a,b) => a+b, 0)+k.reduce((a,b) => a+b, 0)+
        w.reduce((a,b) => a+b, 0) + m.reduce((a,b) => a+b, 0)
    );
    total = punkte-total;
    document.getElementById("total").innerText = total;

    //Leben
    //Attributwerte holen und daraus Leben berechnen
    let modi = race[document.getElementById("menuanzeige").innerText];
    let vitali = (
        Number(document.getElementById("korper").innerText)+
        (Number(document.getElementById("mentales").innerText)/2)+
        modi
    );
    //checkerito, dass alles passt
    if (vitali<1) vitali = 0;
    //Wert einfügen
    document.getElementById("leben").innerText = vitali;
  

    //Geistige Gesundheit
    //Attributwerte holen und daraus GG berechnen
    let gg = (
        Number(document.getElementById("m9").value)+Number(document.getElementById("m3").value)+
        Number(document.getElementById("m1").value)+Number(document.getElementById("m6").value)
    );
    gg = (gg/4)*5;
    //checkerito, dass alles passt
    if (gg<5) gg = 5;
    else if (gg>100) gg=100;
    //Wert einfügen
    document.getElementById("gege").innerText = gg;

    //Mana
    //Attributwerte holen und daraus Mana berechnen
    let mana = (
        Number(document.getElementById("m1").value)+
        Number(document.getElementById("w8").value)+Number(document.getElementById("k8").value)
    );
    mana = (mana/3)*10;
    //checkerito, dass alles passt
    if (mana<10) mana = 10;
    else if (mana>200) mana = 200;
    //Wert einfügen
    document.getElementById("mana").innerText = mana;

    //Stärke
    //Attributwerte holen und daraus Stärke berechnen
    let stark = (
        (Number(document.getElementById("leben").innerText)*0,05)+
        ((Number(document.getElementById("k1").value)+Number(document.getElementById("k4").value))/4)+3
    );
    if (stark<7) stark = 7;
    else if (stark>20) stark = 20;
    //Wert einfügen
    document.getElementById("stark").innerText = stark;
}
