//Rasse:Lebensmodifikator
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
//Faulheit
const v = "v";
const t = "t";


//Arrays mit den ids aller festen Fähigkeiten, Waffenklassen, Zauberklassen
const fest = ["schwimm","reit","les","schreib","mathe"];
const waffenklassen = ["kling", "schlag", "stich", "kunst", "rauf", "wurf","fern"];
const magie =["feuer","wasser","erde","luft","beschwer","verstark","phys","psych"];
//bonus=bonuswert.id:[3 attribute.id zum berechnen];kombi=kombis.id:[attribut1.id,attribut2.id];selected=klappe.id:[auswahl.id,auswahl.value]
const bonus = {"kling":["k8","m1","k3"],"schlag":["stark","s8","k1",],"stich":["k4","k6","k1"],
"kunst":["k4","k2","k1"],"rauf":["m8","s8","k3"],"wurf":["k8","m1","werf"], "fern":["k8","m1","m2"]};
const kombi = {"tiere":["w2","s6"],"dieb":["k6","k5"],"tierspur":["m4","w2"],"spur":["m4",
"m3"],"klette":["k1","k4"],"werf":["m1","k1"],"werk":["k6","k8"]};
const selected = {"raceselect":["raceselect","Auswahl"],"schwimm":["schwimmno","Nein"],"reit":["reitno","Nein"],"les":["lesno","Nein"],
"schreib":["schreibno","Nein"],"mathe":["matheno","Nein"],"klasse1":["default1","Klasse"],"klasse2":["default2","Klasse"],
"klasse3":["default3","Klasse"],"klasse4":["default4","Klasse"],"klasse5":["default5","Klasse"],"klasse6":["default6","Klasse"],
"klasse7":["default7","Klasse"],"klasse8":["default8","Klasse"]}
//dict mit Attribut:Attributsid für alle Attribute
const idcorp = {
    "Beweglichkeit":"k1",
    "Reaktion":"k2",
    "Schnelligkeit":"k3",
    "Gleichgewicht":"k4",
    "Schleichen":"k5",
    "Fingerfertigkeit":"k6",
    "Ausdauer":"k7",
    "Geschicklichkeit":"k8",
    "Fokus":"m1",
    "Geduld":"m2",
    "Wahrnehmung":"m3",
    "Untersuchen":"m4",
    "Erinnerung":"m5",
    "Vorsicht":"m6",
    "Orientierung":"m7",
    "Mut":"m8",
    "Willenskraft":"m9",
    "Medizin":"w1",
    "Tierkunde":"w2",
    "Pflanzenkunde":"w3",
    "Religionswissen":"w4",
    "Kultur":"w5",
    "Ortskunde":"w6",
    "Gassenwissen":"w7",
    "Magie":"w8",
    "Geschichte":"w9",
    "Etikette":"w10",
    "Menschenkenntnis":"s1",
    "Lügen":"s2",
    "Täuschen":"s3",
    "Überzeugen":"s4",
    "Feilschen":"s5",
    "Charisma":"s6",
    "Betören":"s7",
    "Einschüchtern":"s8"
}


//Blank Arrays mit allen Werten nach Kategorie seprariert
let s = Array(8).fill(1);
let w = Array(10).fill(1);
let k = Array(8).fill(1);
let m = Array(9).fill(1);


//Helperfunctions
//Kurze Variante;Nimmt ID als input und returned Element mit dieser ID
function getHelp(id) {
    return document.getElementById(id);
}
//Holt den Inhalt eines Elements per ID je nach Art
//type= v(=value),t(=innerText)
function getVal(type,id) {
    if (type==v) return getHelp(id).value;
    else if (type==t) return getHelp(id).innerText;
    return;
}
//Holt Inhalt eines Elements per ID und ersetzt ihn durch value
function setVal(type,id,value) {
    if (type==v) getHelp(id).value = value;
    else if (type==t) getHelp(id).innerText = value;
}
//getVal aber von String zu number umgewandelt
function getNum(type,id) {
    if (type==v||type==t) return Number(getVal(type,id));
    return;
}

//Punkte
let punkte = 400; //default 400
setVal(t,"pointstotal",punkte); //insgesamt
setVal(t,"pointsleft",punkte);  //noch übrig

//setzt die insgesamt Punkte auf die Eingabe nach Enter drücken
function setTotal() {
    getHelp("settotal").addEventListener("keydown",(e)=> {
        if (e.key==="Enter") { //ändere nummer wenn Enter gedrückt wurde
            let number = getVal(v,"settotal"); //Eingegebene Zahl
            let pointsspent = getVal(t,"pointstotal")-getVal(t,"pointsleft"); //totalpunkte-restliche_punkte=bisher ausgegebene punkte

            //Eingabe darf nicht weniger als insgesamt ausgegeben sein und muss mind. 50 sein (jedes Attribut auf 1)
            if (number>=pointsspent&&number>=50) {
            setVal(t,"pointstotal",number); //Neue total punkte
            setVal(t,"pointsleft",number-pointsspent); //Neue noch übrige Punkte
            punkte=number; //update variable für spätere berechnungen
            }
        }
    });
}

//begrenze punkteeingabe auf max. 3 Stellen
function checkInput() {
    let inputnumber = getVal(v,"settotal").toString();
    if (inputnumber.length>3) {
        inputnumber = inputnumber.substring(0,3);
        setVal(v,"settotal",Number(inputnumber));
    }
}

function reset() {
    Object.values(idcorp).forEach(function(item) {
        if (getVal(v,item)!=1) {
            setVal(v,item,1);
            updateWerte(getHelp(item))
        }
    });
    s.fill(1);
    setVal(t,"soziales",1);
    w.fill(1);
    setVal(t,"wissen",1);
    k.fill(1);
    setVal(t,"korper",1);
    m.fill(1);
    setVal(t,"mentales",1);
    fest.forEach(function(item) {
        if(getVal(t,item)=="Ja") setVal(t,item,"Nein");
    });
    waffenklassen.forEach(function(item) {
        if(getVal(t,item+"punkte")>0) setVal(t,item+"punkte",0);
    });
    magie.forEach(function(item) {
        if (getVal(t,item+"punkte")>0) setVal(t,item+"punkte",0);
    });
    for (let i=1;i<9;i++) {
        if (getVal(t,"zauber"+i+"punkte")>0) setVal(t,"zauber"+i+"punkte",0);
    }
    setVal(t,"pointsleft",getVal(t,"pointstotal"));
    updateWerte();
}

//Action wenn eine Zahl geändert wird
function changeNumber(element) {

    //Geänderte Zahl
    let input = Number(element.value);

    //Zahl zurücksetzen falls nicht zwischen 1 und 20
    if (input > 20) {
        input = 20;
        element.value = input;
    }
    else if (input < 0) {
        input = 1;
        element.value = input;
    }

    let section = element.id[0];
    let index = element.id[1]-1;

    //Attributskategorie (Durchschnitt aller Attributswert der Klasse s/w/k/m)
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
   //Alles auf dem Laufenden halten und geändertes Element weitergeben
   updateWerte(element);
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


//Zeige ausgewähltes Element an
function namechanger(id, target) {
    if (id == null || target == null) return;
    //reset
    target.innerText = id.innerText;
    //Änder Wert im dict selected
    selected[target.id] = [id.id,id.innerText];

    updateWerte(target);
}


//Zeige neu ausgewählte Klasse an
function changeLabel(klasse) {
    setVal(t,"talentart",klasse.innerText);
    setVal(t,"talente",klasse.title);
}

//Erhöhe Punkt der Klasse um Intervall
//klass=;intervall=um wie viel der wert erhöht werden soll;grenze=bis zu welchem wert maximal erhöht werden darf
function plus(klasse,intervall,grenze) {
    let plus = getNum(t,klasse.id+"punkte");
    let total = getNum(t,"pointsleft");
    //checke, dass nicht über das gesetzte limit erhöht wird
    //und die verfügbaren punkte nicht überschrittenw werden
    if (!((plus+intervall)>grenze)&&(total-intervall>=0)) {
        plus += intervall;
        setVal(t,klasse.id+"punkte",plus);
        updateWerte();
    }
}

//Erlaube Stufenerhöhung der Zauber je nach Zaubertwert der Zauberklasse
function zauberplus(zauberid) {
    let zauberplus = getNum(t,"zauber"+zauberid+"punkte"); //Ausgangswert
    let zauberklasse = selected["klasse"+zauberid][0].slice(0,-1); //Ausgewählte Klasse
    let total = getNum(t,"pointsleft"); //Verfügbare Punkte
    //Stoppe wenn noch keine Klasse ausgewählt ist
    if (zauberklasse != "default"&&(total!=0)) {
        let klassenwert = getNum(t,zauberklasse+"wert"); //Wert in der auswaählten Zauberklasse
        if (zauberplus==0&&klassenwert!=0) zauberplus+=1;       //Stufe 1
        else if (zauberplus==1&&klassenwert>4) zauberplus+=1;   //Stufe 2
        else if (zauberplus==2&&klassenwert>8) zauberplus+=1;   //Stufe 3
        else if (zauberplus==3&&klassenwert>12) zauberplus+=1;  //Stufe 4
    }
    setVal(t,"zauber"+zauberid+"punkte",zauberplus);
    updateWerte()
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
function updateWerte(element) {
    //Noch zu vergebene Punkte
    //Ausgegebene Attributspunkte
    let total = (
        s.reduce((a,b) => a+b, 0) + k.reduce((a,b) => a+b, 0)+
        w.reduce((a,b) => a+b, 0) + m.reduce((a,b) => a+b, 0)
    );
    //Ausgebene Punkte feste Fertigkeiten (5:1)
    fest.forEach(function (item) {
        if (getVal(t,item)=="Ja") {
           total=total+5;
        }
    });

    //Ausgegebene Punkte Waffenklassen (5:1), Wert kommt schon als Vielfaches von 5
    waffenklassen.forEach(function (item) {
    total = total+getNum(t,item+'punkte');
    });

    //Ausgebene Punkte Magie (2:1), Wert kommt schon als Vielfaches von 2
    magie.forEach(function(item) {
        total = total+getNum(t,item+"punkte");
    });
    //Ausgegebene Punkte Zauber
    for (let i=1;i<9;i++) {
        total = total+getNum(t,"zauber"+i+"punkte");
    }



    //zurücksetzen wenn mehr Punkte ausgegeben wurden als zur Verfügung standen und neu berechnen
    if (total>punkte) {
        if (element.innerText==0){  //Attribut wurde geändert
            element.value=element.value-(total-punkte);
            total=punkte;
            changeNumber(element); //element weitergeben damit es auch im array geändert wird (triggert danach wieder updateWerte mit jetzt richtigem Wert)
        }
        else {  //feste Fähigkeit wurde geändert
            element.innerText="Nein";
            total -= 5
        }
        //(alle_Punkte - total_ausgegebene)=noch übrig
        total = punkte-total;
        setVal(t,"pointsleft",total);
    }
    //wenn bei der punktevergabe alles ok war, berechne andere werte neu
    else {

        //setze leben variable um fehler bei der stärkeberechnung zu verhindern,
        //wenn noch keine Rasse ausgewählt ist
        let leben;

        //Leben
        if (getVal(t,"raceselect") == "Auswahl") { //Default bis Rasse gewählt ist
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
        let stark = Math.round(leben*0.05+((getNum(v,"k1")+getNum(v,"k4"))/4)+3); //Stärke = (Leben*0.05) + ((Beweglichkeit+Gleichgewicht)/4)+3
        if (stark<7) stark = 7; //Minwert 7
        else if (stark>20) stark = 20; //Maxwert 20
        setVal(t,"stark",stark);

        //Geistige Gesundheit
        let gg = getNum(v,"m9")+getNum(v,"m3")+getNum(v,"m1")+getNum(v,"m6"); //Geistige Gesundheit = Durchschnitt(Willenskraft+Wahrnehmung+Fokus+Vorsicht)*5
        Math.round((gg/4)*5);
        if (gg<5) gg = 5; //Minwert 5
        else if (gg>100) gg=100; //Maxwert 100
        setVal(t,"gege",gg);

        //Mana
        let mana = getNum(v,"m1")+getNum(v,"w8")+getNum(v,"k8"); //Mana = Durchschnitt(Fokus+Magie+Geschicklichkeit)*10
        mana=Math.round((mana/3)*10);
        if (mana<10) mana = 10; //Minwert 10
        else if (mana>200) mana = 200; //Maxwert 200
        setVal(t,"mana",mana);


        //Kombis
        //Iteriere durch alle Kombis und passe die Werte an
        Object.keys(kombi).forEach(function(item){
            let endkombi = Math.round((getNum(v,kombi[item][0])+getNum(v,kombi[item][1]))/2); //Kombiwerte = Durchschnitt(Attribut1+Attribut2)
            setVal(t,item,endkombi);
        });


        //Bonuswerte Kampf
        //Iteriere durch alle Kampfklassen und passe die Bonuswerte an
        Object.keys(bonus).forEach(function(item){
            let endbonus;
            let bonus1,bonus2,bonus3;

            //catche stärke und werfen, da sie text und kein value enthalten
            if (bonus[item][0]=="stark") bonus1 = getNum(t,bonus[item][0]); //Bonuswert1
            else bonus1 = getNum(v,bonus[item][0]);                        
            bonus2 = getNum(v,bonus[item][1]);                             //Bonuswert2
            if (bonus[item][2]=="werf") bonus3 = getNum(t,bonus[item][2]); //Bonuswert3
            else bonus3 = getNum(v,bonus[item][2]);

            endbonus = Math.round((bonus1+bonus2+bonus3)*0.1);  //(B1+B2+B3)*0.01
            setVal(t,item+"bonus",endbonus);
        });

        //Kampf- und Paradewerte
        waffenklassen.forEach(function(item) {
            //Kampfwert
            let neuwert;
            neuwert = Math.round(getNum(t,item+"bonus")+(getNum(t,item+"punkte")/5)+5); //Kampfwert = Bonuswert+PunkteWaffenklasse; Kosten 5:1, Grundwert 5
            setVal(t,item+"kampf",neuwert);

            //Paradewert
            if (!(item == "wurf"||item=="fern")){       //wurf- und Fernwaffen haben keinen Paradewert
                neuwert = Math.round(neuwert/2)     //Paradewert entspricht der Hälfte des Kampfwertes der entsprechenden Waffenklasse
                setVal(t,item+"parade",neuwert);
            };
        });


        //Zauberwerte
        magie.forEach(function(item) {
            let neuzauber;
            neuzauber = getNum(t,item+"punkte")/2; //Kosten 2:1
            setVal(t,item+"wert",neuzauber);
        });
    
        //Ausgegebene Punkte
        total = punkte-total;         //(alle_Punkte - total_ausgegebene)=noch übrig
        setVal(t,"pointsleft",total);
    }
}
