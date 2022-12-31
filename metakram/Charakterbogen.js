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
const idcorp = {};
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

//Arrays mit den ids aller festen Fähigkeiten Waffenklassen
const fest = ["schwimm","reit","les","schreib","mathe"];
const waffenklassen = ["kling", "schlag", "stich", "kunst", "rauf", "wurf","fern"];
const bonus = {"kling":["k8","m1","k3"],"schlag":["stark","s8","k1",],"stich":["k4","k6","k1"],
"kunst":["k4","k2","k1"],"rauf":["m8","s8","k3"],"wurf":["k8","m1","werf"], "fern":["k8","m1","m2"]};
const kombi = {"tiere":["w2","s6"],"dieb":["k6","k5"],"tierspur":["m4","w2"],"spur":["m4",
"m3"],"klette":["k1","k4"],"werf":["m1","k1"]};

//Arrays mit allen Werten nach Kategorie seprariert
let s = Array(8).fill(1);
let w = Array(10).fill(1);
let k = Array(8).fill(1);
let m = Array(9).fill(1);
const v = "v";
const t = "t";


//Action wenn eine Zahl geändert wird
function changeNumber(id) {

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

   //Alles auf dem Laufenden halten
   updateWerte();
};

//Kurze Variante;Nimmt ID als input und returned Element mit dieser ID
function getHelp(id) {
    return document.getElementById(id);
}
//Holt den Inhalt eines Elements mit input ID je nach Art
//type=v,t
function getVal(type,id) {
    if (type=="v") return getHelp(id).value;
    else if (type=="t") return getHelp(id).innerText;
    return;
}
function setVal(type,id,value) {
    if (type=="v") getHelp(id).value = value;
    else if (type==t) getHelp(id).innerText = value;
    return;
}
//getVal aber von String zu number umgewandelt
function getNum(type,id) {
    if (type=="v"||type=="t") return Number(getVal(type,id));
    return;
}



//Öffne und schließe das dropdownmenü
function klappenregler(klappe) {
    getHelp(klappe.id).classList.toggle("klappeauf");
}

//Schließe Menü wenn woanders hingeklickt wird
window.onclick = function(event) {
    if (!event.target.matches('.klappe')) {
        let klappen = document.getElementsByClassName("klappezu");
        let i;
        for (i = 0; i < klappen.length; i++) {
            let klappeoffen = klappen[i];
            if (klappeoffen.classList.contains('klappeauf')) {
                klappeoffen.classList.remove('klappeauf');
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

//Erhöhe Punkt der Klasse um 1
function plus(klasse) {
    let plus = Number(getHelp(klasse.id+"punkte").innerText);
    plus += 5;
    getHelp(klasse.id+"punkte").innerText = plus;
    updateWerte();
}

//Verringere Punkt der Klasse um 1 sofern p >= 0
function minus(klasse) {
    let minus = Number(getHelp(klasse.id+"punkte").innerText);
    if (!minus == 0) minus -= 5;
    getHelp(klasse.id+"punkte").innerText = minus
    updateWerte();
}


//Allgemeine Charakterwerte auf dem Laufenden halten
function updateWerte() {

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
    //Iteriere durch alle Kombis und passe die Werte an
    Object.keys(kombi).forEach(function(item){
        let endkombi = Math.round((getNum(v,kombi[item][0])+getNum(v,kombi[item][1]))/2);
        setVal(t,item,endkombi);
    });


    //Bonuswerte Kampf
    //Iteriere durch alle Kampfklassen und passe die Boni an
    Object.keys(bonus).forEach(function(item){
        let endbonus;
        let bonus1,bonus2,bonus3;
        
        //catche stärke und werfen, da sie text und kein value enthalten
        if (bonus[item][0]=="stark") bonus1 = getNum(t,bonus[item][0]);
        else bonus1 = getNum(v,bonus[item][0]);
        bonus2 = getNum(v,bonus[item][1]);
        if (bonus[item][2]=="werf") bonus3 = getNum(t,bonus[item][2]);
        else bonus3 = getNum(v,bonus[item][2]);

        endbonus = Math.round((bonus1+bonus2+bonus3)*0.1);
        setVal(t,item+"bonus",endbonus);
    });

    

    //Kampf- und Paradewerte
    waffenklassen.forEach(function(item) {
        let neuwert;
        neuwert = Number(getHelp(item+"bonus").innerText)+(Number(getHelp(item+"punkte").innerText)/5)+5;
        getHelp(item+"kampf").innerText = Math.round(neuwert);
        //wurf- und fernwaffen haben keinen paradewert
        if (!(item == "wurf"||item=="fern")){
            getHelp(item+"parade").innerText = Math.round(neuwert/2);
        };
    });
   

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
    //5 Punkte pro Waffenklassenpunkt
    waffenklassen.forEach(function (item) {
       total= total+Number(getHelp(item+'punkte').innerText);
    })

    total = punkte-total;
    getHelp("total").innerText = total;
}
