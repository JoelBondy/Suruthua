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
const magie =["feuer","wasser","erde","luft","beschwer","verstark","phys","psych"];
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

//Helperfunctions

//Kurze Variante;Nimmt ID als input und returned Element mit dieser ID
function getHelp(id) {
    return document.getElementById(id);
}
//Holt den Inhalt eines Elements per ID je nach Art
//type=v,t
function getVal(type,id) {
    if (type==v) return getHelp(id).value;
    else if (type==t) return getHelp(id).innerText;
    return;
}
//Holt Inhalt eines Elements per ID und ersetzt ihn durch inputvalue
function setVal(type,id,value) {
    if (type==v) getHelp(id).value = value;
    else if (type==t) getHelp(id).innerText = value;
    return;
}
//getVal aber von String zu number umgewandelt
function getNum(type,id) {
    if (type==v||type==t) return Number(getVal(type,id));
    return;
}


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
        let aver = Math.round(s.reduce((a, b) => a+b, 0) / s.length);
        setVal(t,"soziales",aver);
    }
    else if (section == "w") {
        w[index] = input;
        let aver =Math.round(w.reduce((a, b) => a+b, 0) / w.length);
        setVal(t,"wissen",aver);
    }
   else if (section == "k") {
        k[index] = input;
        let aver = Math.round(k.reduce((a, b) => a+b, 0) / k.length);
        setVal(t,"korper",aver);
   }
   else if (section == "m") {
        m[index] = input;
        let aver = Math.round(m.reduce((a, b) => a+b, 0) / m.length);
        setVal(t,"mentales",aver);
   }
   //Alles auf dem Laufenden halten
   updateWerte();
};



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
    setVal(t,"talentart",klasse.innerText);
    setVal(t,"talente",klasse.title);
}

//Erhöhe Punkt der Klasse um Intervall
function plus(klasse,intervall,grenze) {
    let plus = getNum(t,klasse.id+"punkte");
    if (!((plus+intervall)>grenze)) {
        plus += intervall;
        setVal(t,klasse.id+"punkte",plus);
        updateWerte();
    }
}

//Verringere Punkt der Klasse um Intervall sofern !(p < grenze), Default grenze = 0
function minus(klasse,intervall,grenze) {
    if (grenze == undefined) grenze = 0;
    let minus = getNum(t,klasse.id+"punkte");
    if (!((minus-intervall)<grenze)) {
        minus -= intervall;
        setVal(t,klasse.id+"punkte",minus);
        updateWerte();
    }
}


//Allgemeine Charakterwerte auf dem Laufenden halten
function updateWerte() {

    //setze leben variable um fehler bei der stärkeberechnung zu verhindern,
    //wenn noch keine Rasse ausgewählt ist
    let leben;
    //Leben
    //Default bis Rasse gewählt ist
    if (getVal(t,"raceselect") == "Auswahl") {
        setVal(t,"leben","Wähle eine Rasse");
        leben=0;
    }
    else {
    let modi = race[getVal(t,"raceselect")];
        let vitali = Math.round(getNum(t,"korper")+(getNum(t,"mentales")/2)+modi);
        if (vitali<1) vitali = 0;
        setVal(t,"leben",vitali);
        leben = vitali;
    }

    //Stärke
    //Attributwerte holen und daraus Stärke berechnen
    let stark = Math.round(leben*0.05+((getNum(v,"k1")+getNum(v,"k4"))/4)+3);
    if (stark<7) stark = 7;
    else if (stark>20) stark = 20;
    setVal(t,"stark",stark);

    //Geistige Gesundheit
    //Attributwerte holen und daraus GG berechnen
    let gg = getNum(v,"m9")+getNum(v,"m3")+getNum(v,"m1")+getNum(v,"m6");
    Math.round((gg/4)*5);
    if (gg<5) gg = 5;
    else if (gg>100) gg=100;
    setVal(t,"gege",gg);

    //Mana
    //Attributwerte holen und daraus Mana berechnen
    let mana = getNum(v,"m1")+getNum(v,"w8")+getNum(v,"k8");
    Math.round(mana = (mana/3)*10);
    if (mana<10) mana = 10;
    else if (mana>200) mana = 200;
    setVal(t,"mana",mana);


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
        neuwert = Math.round(getNum(t,item+"bonus")+(getNum(t,item+"punkte")/5)+5);
        setVal(t,item+"kampf",neuwert);
        //wurf- und fernwaffen haben keinen paradewert
        if (!(item == "wurf"||item=="fern")){
            neuwert = Math.round(neuwert/2)
            setVal(t,item+"parade",neuwert);
        };
    });
   
    magie.forEach(function(item) {
        let neuzauber;
        neuzauber = getNum(t,item+"punkte")/2;
        setVal(t,item+"wert",neuzauber);
    });

    //Noch zu vergebene Punkte
    //Ausgegebene Attributspunkte
    let total = (
        s.reduce((a,b) => a+b, 0) + k.reduce((a,b) => a+b, 0)+
        w.reduce((a,b) => a+b, 0) + m.reduce((a,b) => a+b, 0)
    );
    //Ausgebene Punkte fest Fertigkeiten (5:1)
    fest.forEach(function (item) {
        if (getVal(t,item)=="Ja") {
            total=total+5;
        }
    }); 
    //Ausgegebene Punkte Waffenklassen (5:1), Wert kommt schon als vielfaches von 5
    waffenklassen.forEach(function (item) {
       total = total+getNum(t,item+'punkte');
    });
    //Ausgebene Punkte Magie (2:1), Wert kommt schon als vielfaches von 2
    magie.forEach(function(item) {
        total = total+getNum(t,item+"punkte");
    });
    //Ausgegebene Punkte Zauber
    for (let i=1;i<9;i++) {
        total = total+getNum(t,"zauber"+i+"punkte");
    }
    //Alle Punkte - total ausgegebene
    total = punkte-total;
    setVal(t,"total",total);
}
