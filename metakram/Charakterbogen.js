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

//Erstelle ein dict mit Attribut:id(k1 usw.) zum schnelleren Finden
const idcorp = {}
for (let i=1;i<9;i++) {
    idcorp[getHelp("k"+i).parentNode.parentNode.childNodes[1].innerText] = "k"+i;
}
for (let i=1;i<10;i++) {
    idcorp[getHelp("m"+i).parentNode.parentNode.childNodes[1].innerText] = "m"+i;
}
for (let i=1;i<11;i++) {
    idcorp[getHelp("w"+i).parentNode.parentNode.childNodes[1].innerText] = "w"+i;
}
for (let i=1;i<9;i++) {
    idcorp[getHelp("s"+i).parentNode.parentNode.childNodes[1].innerText] = "s"+i;
}


//Insgesamt zu vergebene Punkte
const punkte = 400;

//Array mit den ids aller festen Fähigkeitn
const fest = ["schwimm","reit","les","schreib","mathe"]

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
        getHelp("soziales").innerText = Math.round(aver);
    }
    else if (section == "w") {
        w[index] = input;
        let aver = w.reduce((a, b) => a+b, 0) / w.length;
        getHelp("wissen").innerText = Math.round(aver);
    }
   else if (section == "k") {
        k[index] = input;
        let aver = k.reduce((a, b) => a+b, 0) / k.length;
        getHelp("korper").innerText = Math.round(aver);
   }
   else if (section == "m") {
        m[index] = input;
        let aver = m.reduce((a, b) => a+b, 0) / m.length;
        getHelp("mentales").innerText = Math.round(aver);
   }

   updateWerte();
};


function getHelp(id) {
    return document.getElementById(id);
}


//Öffne und schließe das Rassenmenü
function klappenregler(klappe) {
    getHelp(klappe.id).classList.toggle("klappeauf");
}

//Schließe Menü wenn woanders hingeklickt wird
window.onclick = function(event) {
    if (!event.target.matches('.klappe')) {
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
function namechanger(id, target) {
    if (id == null || target == null) return;
    target.innerText = id.innerText;
    updateWerte();
}

//Zeige ausgewählte Klasse an
function changeLabel(klasse) {
    getHelp("talentart").innerText = klasse.innerText
    getHelp("talente").innerText = klasse.title
}

//Allgemeine Charakterwerte auf dem Laufenden halten
function updateWerte() {
    //Noch zu vergebene Punkte
    let total = (
        s.reduce((a,b) => a+b, 0) + k.reduce((a,b) => a+b, 0)+
        w.reduce((a,b) => a+b, 0) + m.reduce((a,b) => a+b, 0)
    );
    //5 Punkte pro fester Fähigkeit
    fest.forEach(function (item) {
        if (getHelp(item).innerText=="Ja") {
            total=total+5;
        }
    }); 

    total = punkte-total;
    getHelp("total").innerText = total;

    //Leben; Default bis Rasse gewählt ist
    if (getHelp("raceselect").innerText == "Auswahl") {
        getHelp("leben").innerText = "Wähle eine Rasse";
    }
    else {
    let modi = race[getHelp("raceselect").innerText];
        let vitali = (
            Number(getHelp("korper").innerText)+
            (Number(getHelp("mentales").innerText)/2)+
            modi
        );
        //checkerito, dass alles passt
        if (vitali<1) vitali = 0;
        //Wert einfügen
        getHelp("leben").innerText = Math.round(vitali);
    }

    //Geistige Gesundheit
    //Attributwerte holen und daraus GG berechnen
    let gg = (
        Number(getHelp("m9").value)+Number(getHelp("m3").value)+
        Number(getHelp("m1").value)+Number(getHelp("m6").value)
    );
    gg = (gg/4)*5;
    //checkerito, dass alles passt
    if (gg<5) gg = 5;
    else if (gg>100) gg=100;
    //Wert einfügen
    getHelp("gege").innerText = Math.round(gg);

    //Mana
    //Attributwerte holen und daraus Mana berechnen
    let mana = (
        Number(getHelp("m1").value)+
        Number(getHelp("w8").value)+Number(getHelp("k8").value)
    );
    mana = (mana/3)*10;
    //checkerito, dass alles passt
    if (mana<10) mana = 10;
    else if (mana>200) mana = 200;
    //Wert einfügen
    getHelp("mana").innerText = Math.round(mana);

    //Stärke
    //Attributwerte holen und daraus Stärke berechnen
    let stark = (
        (Number(getHelp("leben").innerText)*0,05)+
        ((Number(getHelp("k1").value)+Number(getHelp("k4").value))/4)+3
    );
    if (stark<7) stark = 7;
    else if (stark>20) stark = 20;
    //Wert einfügen
    getHelp("stark").innerText = Math.round(stark);

    //Kombis
    let tier = (Number(getHelp("w2").value)+Number(getHelp("s6").value))/2;
    getHelp("tiere").innerText = Math.round(tier);
    let dieb = (Number(getHelp("k6").value)+Number(getHelp("k5").value))/2;
    getHelp("dieb").innerText = Math.round(dieb);
    let fahrt = (Number(getHelp("m4").value)+Number(getHelp("w2").value))/2;
    getHelp("tierspur").innerText = Math.round(fahrt);
    let spur = (Number(getHelp("m4").value)+Number(getHelp("m3").value))/2;
    getHelp("spur").innerText = Math.round(spur);
    let klette = (Number(getHelp("k1").value)+Number(getHelp("k4").value))/2;
    getHelp("klette").innerText = Math.round(klette);
    let werf = (Number(getHelp("m1").value)+Number(getHelp("k1").value))/2;
    getHelp("werf").innerText = Math.round(werf);

    //Bonuswerte Kampf
    let kling = (Number(getHelp("k8").value)+Number(getHelp("m1").value)+Number(getHelp("k3").value))*0.1;
    getHelp("klingbonus").innerText = Math.round(kling);
    let schlag = (Number(getHelp("stark").innerText)+Number(getHelp("s8").value)+Number(getHelp("k1").value))*0.1;
    getHelp("schlagbonus").innerText = Math.round(schlag);
    let stich = (Number(getHelp("k4").value)+Number(getHelp("k6").value)+Number(getHelp("k1").value))*0.1;
    getHelp("stichbonus").innerText = Math.round(stich);
    let kampf = (Number(getHelp("k4").value)+Number(getHelp("k2").value)+Number(getHelp("k1").value))*0.1;
    getHelp("kunstbonus").innerText = Math.round(kampf);
    let rauf = (Number(getHelp("m8").value)+Number(getHelp("s8").value)+Number(getHelp("k3").value))*0.1;
    getHelp("raufbonus").innerText = Math.round(rauf);
    let worf = (Number(getHelp("k8").value)+Number(getHelp("m1").value)+Number(getHelp("werf").innerText))*0.1;
    getHelp("wurfbonus").innerText = Math.round(worf);
    let fern = (Number(getHelp("k8").value)+Number(getHelp("m1").value)+Number(getHelp("m2").value))*0.1;
    getHelp("fernbonus").innerText = Math.round(fern);
}
