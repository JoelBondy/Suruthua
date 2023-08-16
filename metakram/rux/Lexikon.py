import random
from time import sleep

# ['Ak', 'Akamah', 'Amaka', 'Amaka (Regelwerk)', 'Attribute', 'Augling', 'Augling (Regelwerk)', 'Avzitil', 'Avztil (Regelwerk)', 'Baumgeister', 'Berethao', 'Berge von Loromoth', 'Blauer Traum', 'Blib', 'Blutborke', 'Bodengolem', 'Charakterbogen', "Cul'thur", 'Cureg', 'Drah', 'Dras und Drus', 'Dras und Drus Feldzug', 'Draske', 'Draske (Regelwerk)', 'Drasna', 'Elb', 'Elb (Regelwerk)', 'Elbenkriege', 'Entstehung der Welt', 'Feuergolem', 'Flossenbeutler', 'Fluggolem', 'Fluropilz', 'Flüche', 'Frostwein', 'Förun', 'Gebirge', 'Gegner', 'Gemüsegolem', 'Geologie', 'Gesteinsgolem', 'Gewässer', 'Giftgolem', 'Glaubenskriege', 'Gloq', 'Golem', 'Große Persönlichkeiten', 'Guqual', 'Guqual (Regelwerk)', 'Halluzinationspilz', 'Himmelserz', 'Himmelsregen', 'Ideen', 'Ideen (Tiere)', 'Illoda', 'Inseln', 'Kalender/Zeitr', 'Kampf', 'Karte', "Keil'O Renn", 'Kiesenriller-Maus', 'Kncohengolem', 'Knochendorn', 'Koberinth', 'Kuberika', 'Kwin Stalbu', 'Lachratte', 'Loromoth', 'Magie', 'Mensch', 'Menschen Vernichtung', 'Minort (Stalbu)', 'Mithadium', 'Mond', 'Namen', 'Nautrphänomene', 'Parasitkäfer', 'Pflanzengolem', 'Pilze', 'Psychogolem', 'Puletsi', 'Quork', 'Quork (Regelwerk)', "Ras'qath", 'Regeln', 'Religion', 'Religion (Regelwerk)', 'Ruryx', 'Ry', 'Sauerbaum', 'Schlafplanze (Blauer Traum)', 'Schlangenrausch', 'Schreiender Triesel', 'Schwarze Löcher', 'Segen', 'Sonne', 'Sonnensytem', 'Stalbu', 'Suru', 'Säuregolem', 'Triesel', 'Trivia Gott', 'Trollbrücke', 'Tropfbeutel', 'Tropfbeutler', 'Turninch', 'Unhabhängigkeitskriege von Puletsi', 'Vadon', 'Vadonier', 'Vadonier (Regelwerk)', 'Vaiad', 'Verfluchte Wesen', 'Verfluchter Quork', 'Versiegeltes Schloss', 'Vier Elemente', 'Waffenklassen', 'Wassergolem', 'Wichtige Daten', 'Wirinima', 'Wrethh', 'Währung', 'Xaraton', 'Zeitrechnung', 'Übernehmen (Natur)']
vowels = ["a", "u", "ū", "ā", "û", "â"]
consonants = ["x", "g", "q", "l", "r", "n", "ð", "d", "k", "ƥ"]
alphabet = ["a", "u", "ū", "ā", "û", "â", "x", "g", "q", "l", "r", "n", "ð", "d", "k", "ƥ"]
pronouns = {"kā": "gā", "la": "gal", "rā": "gār", "kān": "gān", "lan": "gan", "rān": "grān"}
articles = {
    "gu-": ["ugu-", "gul-", "ugul-", "gur-", "āgur-"], "ga-": ["uga-", "gāl-", "gūl-", "gar-", "gār-"],
    "a-": ["ā-", "āl-", "ūl-", "ra-", "ār-"]
}
POS = {
    "V": "Verb", "N1": "Nomen (Klasse 1)", "N2": "Nomen (Klasse 2)", "N3": "Nomen (Klasse 3)",
    "PN1": "Eigenname (Klasse 1)", "PN2": "Eigenname (Klasse 2)", "PN3": "Eigenname (Klasse 3)",
    "ADJ": "Adjektiv", "DET1": "Artikel (Klasse 1)", "DET2": "Artikel (Klasse 2)", "DET3": "Artikel (Klasse 3)",
    "PREP": "Präposition", "TMP": "Temporaladverb", "KNJ": "Konjunktion", "NON": "Negation", "DIM": "Diminutiv",
    "PRO": "Pronomen", "JA": "Ja", "NO": "Nein", "ZAHL": "Zahl"
}
POS_noun = ["N1", "N2", "N3", "PN1", "PN2", "PN3"]
POS_det = ["DET1", "DET2", "DET3"]
hello = "Moin!\n'words' = Einträge mit Übersetzung\n'random' = zufälliges Wort\n'save' = speichern" \
        "\n'tschö' = beenden OHNE speichern\n'b' = bearbeiten\n'del' = löschen\n'g' = Grammatik\n'info' = Info"
info = "Befehle:\n'all' = Ganzes Lexikon\n'len' = Anzahl Einträge\n'active' = Zeige aktuelles Wort an" \
       "\n'empty' = Zeige alle Einträge ohne Übersetzung an" \
       "\n'notlist = Zeige alle Übersetzungen ohne Eintrag an\n'add' = Füge Wort zur notlist hinzu" \
       "\n'random[v/n/a][zahl]' = (Anzahl) zufällige Worte [Verb/Nomen/Adjektiv] (Keine Angabe = 1)" \
       "\n'words[zahl]' = Zeige [zahl] Wörter mit Übersetzung (Keine Angabe = 10, 0 = alle)" \
       "\n'verbs[zahl]' = Zeige [zahl] an Verben (Keine Angabe = 10, 0 = alle)" \
       "\n'nouns[zahl]' = Zeige [zahl] an Nomen (Keine Angabe = 10, 0 = alle)" \
       "\n'adjs[zahl]' = Zeige [zahl] an Adjektiven (Keine Angabe = 10, 0 = alle)" \
       "\n'save' = Speichern\n'tschö' = Beenden OHNE speichern\n'give d' = get d" \
       "\n'vowels' = print special vowels\n'abc' = ganzes Alphabet" \
       "\n'meta['vowels']' = paar zahlen [û und â aufgeführt]" \
       "\na|/u|/d|/p| = ā/ū/ð/ƥ\n+'infoling' = more info"
info_ling = "Weitere Befehle:\n'b' = Bearbeite den letztgesuchten Eintrag\n'del' = Lösche den letztgesuchten Eintrag" \
            "\n'g' = Bilde grammatikalische Formen des letztgesuchten Eintrags" \
            "\n'pos' = Zeige POS-Tag des letztgesuchten Eintrags" \
            "\n'trans' = Zeige Übersetzung(en)\n'syn' = Zeige Synonyme an" \
            "\n'root[b/n]' = Zeige Wurzel(n) des Wortes [bearbeiten/ersetzen]" \
            "\n'rel[b/n]' = Zeige verwandte Wörter [bearbeiten/ersetzen]" \
            "\n'der[b/n]' = Zeige abgeleitete Wörter [bearbeiten/ersetzen]" \
            "\n'generate[zahl]' = Generiere neue Worte aus dem Alphabet (keine Angabe = 10)" \
            "\na|/u|/d|/p| = ā/ū/ð/ƥ\n-'info' = Info"
operator = ["b", "g", "pos", "posb", "posn", "root", "rel", "derv", "rootb", "relb", "dervb", "rootn", "reln", "dervn",
            "del", "trans", "active", "syn", "add", "notlist", "info", "infoling", "save", "meta"]
exceptions = {"ûdar": ["V", ["ûda", "ûdu", "ûdad"], ["udā", "udū", "ûdud"]]}
# import dict from file
lex_file = open("rux_lex", "r", encoding="utf-8")
lex_cont = lex_file.readline()
unassigned = lex_file.readline()[:-1].split("\\")  # erstelle liste von übersetzungen ohne eintrag
lex_list = lex_cont[:-2].split("\\")  # split aber ignoriere letzten backslash und \n (sonst gibts nen leeren eintrag)
lex = {}
for x in lex_list:  # erstelle dict
    (key, val, pos, his) = x.split(":")  # trenne eintrag und bedeutungen (+pos tag und verwandte wörter)
    (root, rel, der) = his.split(">")  # trenne verwandte wörter in wurzel und ableitungen
    # erstelle liste von allen bedeutungen   (wort: ([bedeutungen], [pos], [[wurzel], [verwandt], [ableitungen]])
    lex[key] = val.split(","), pos.split(","), [root.split(","), rel.split(","), der.split(",")]
lex_file.close()

verbs = [word for word in lex if "V" in lex[word][1]]  # erstelle liste aller verben
# erstelle liste aller nomen (inkl eigennamen)
nouns = [word for word in lex if any(item in lex[word][1] for item in POS_noun)]
adjs = [word for word in lex if "ADJ" in lex[word][1]]  # erstelle liste aller adjektive


def save():
    with open("rux_lex", "w", encoding="utf-8") as f:
        for entry in lex:
            f.write(
                entry + ":" + ",".join(lex[entry][0]) + ":" + ",".join(lex[entry][1]) + ":" + ",".join(lex[entry][2][0])
                + ">" + ",".join(lex[entry][2][1]) + ">" + ",".join(lex[entry][2][2]) + "\\")
        f.write("\n")
        for word in unassigned:
            f.write(word + "\\")
    print("Lexikon gesichert:")
    print(str(len(lex)) + " Einträge")


# HELPER FUNCTIONS
def get_input(prompt, form=""):
    if not form:
        item = input(prompt)
    else:
        item = input(prompt).replace(" ", "").replace("_", " ").replace("a|", "ā") \
            .replace("u|", "ū").replace("d|", "ð").replace("p|", "ƥ").split(",")

    return item


# trenne input in buchstaben/zahlen
def separator(text):
    zif = "0123456789"  # definiere ziffern
    string = ""  # buchstaben in input
    number = ""  # zahlen in input
    for char in text:
        if char in zif:  # wenn char eine zahl, füge zu 'number' hinzu, sonst zu 'string'
            number += char
        else:
            string += char
    if not number:  # wenn keine zahl vorhanden, number = -1
        number = -1
    else:
        number = int(number)  # konvertiere number zu integer
    return string, number


def vowel_counter(string):
    count = 0
    for letter in string:
        if letter in vowels:
            count += 1
    return count


# get last vowel oder gleiche mit check ab
def last_vowel(string, check=""):
    vowel = ""
    for letter in reversed(string):
        if letter in vowels:
            vowel = letter
            break

    if check:
        return vowel == check
    else:
        return vowel


# füge 'd-' zum suffix hinzu, wenn word auf vokal endet
def end_vowel(word):
    if ends_in_vowel(word):
        word = word + "d"
    return word


# return last character
def ends_in(word):
    if word:
        return word[-1]


def ends_in_vowel(word):
    if word[-1] in vowels:
        return True
    return False


def check_lex(item, dic=None):
    if dic is None:
        dic = lex

    item = swap(item)
    for entry in dic:
        if item.casefold() == entry.casefold():
            return True

    return False


def check_antwort(prompt="Bist du sicher? j/n\n"):
    ant = get_input(prompt)
    while not ant == "j" and not ant == "n":
        ant = get_input("j/n?: ")
    if ant == "j":
        return True
    else:
        return False


# wenn active eine übersetzung und kein eintrag ist, setze active auf entsprechenden eintrag
def swap(active):
    for entry in lex:  # checken, ob der zuvor gesuchte eintrag existiert als übersetzung
        if active in (trans.lower() for trans in lex[entry][0]):
            active = entry  # setze active auf das wort des eintrages, wenn übersetzung gefunden
    return active


# update wortlisten nach tag (nouns/verbs/adjs), wenn neues wort hinzugefügt wird
def insert_poslist(postag, word):
    for tag in postag:
        if tag.upper() == "ADJ":
            adjs.append(word)
        elif tag.upper() in POS_noun:
            nouns.append(word)
        elif tag.upper() == "V":
            verbs.append(word)


# PRINTERS
def print_entry(word):  # printe eintrag aus lex
    for entry in lex:
        if word == entry or word in (trans.lower() for trans in
                                     lex[entry][0]):  # item in eintrag oder in liste_bedeutungen (caseinsensitive)
            print("Folgenden Eintrag gefunden:\n" + entry + ": " + ", ".join(lex[entry][0]))


def print_empty(liste="empty"):
    if liste == "empty":  # worte ohne übersetzung
        cont = search_empty()
    elif liste == "unassigned":  # übersetzung ohne eintrag
        cont = unassigned
    else:
        print("Inkorrekte Eingabe")
        return

    if not cont == [""]:
        print("\n".join(cont))
        print(str(len(cont)) + " Einträge gefunden")
    else:
        print("Keine Worte vorhanden")


def print_trans(word):
    if word in lex and not lex[word][0] == [""]:  # checke, ob übersetzungen vorhanden sind
        print(", ".join(lex[word][0]))
    else:
        print("Keine Übersetzung gefunden")


# print liste an einträgen. item = input (bestimmt wortart)
def print_class(item):
    (klasse, scope) = separator(item)  # trenne input in wort (klasse) und anzahl einträge (scope)
    if scope == -1:  # wenn kein wert angegeben
        scope = 10  # standardwert 10

    if "verbs" in klasse:
        if scope == 0:  # scope = 0 -> alle verben
            scope = len(verbs)
        # printe die letzten x verben, x = scope
        if klasse == "transverbs":  # printe mit übersetzung
            print("\n".join([v + ": " + ", ".join(lex[v][0]) for v in verbs[-scope:]]))
        else:
            print("\n".join(verbs[-scope:]))  # printe die letzten x verben, x = scope
        print("Insgesamt " + str(len(verbs)) + " Verben gefunden")
    elif "nouns" in klasse:
        if scope == 0:  # scope = 0 -> alle nomen
            scope = len(nouns)
        # printe die letzten x nomen, x = scope
        if klasse == "transnouns":  # printe mit übersetzung
            print("\n".join([n + ": " + ", ".join(lex[n][0]) for n in nouns[-scope:]]))
        else:
            print("\n".join(nouns[-scope:]))
        print("Insgesamt " + str(len(nouns)) + " Nomen gefunden")
    elif "adjs" in klasse:
        if scope == 0:  # scope = 0 -> alle adjektive
            scope = len(adjs)
        # printe die letzten x adjektive, x = scope
        if klasse == "transadjs":  # printe mit übersetzung
            print("\n".join([a + ": " + ", ".join(lex[a][0]) for a in adjs[-scope:]]))
        else:
            print("\n".join(adjs[-scope:]))
        print("Insgesamt " + str(len(adjs)) + " Adjektive gefunden")
    else:
        print("Inkorrekte Eingabe")


def print_words(item):
    _, scope = separator(item)  # trenne input ('words') von gewünschter anzahl (scope)
    if scope > len(lex) or scope == 0:  # scope = 0 -> alle wörter; und catche ob input > len um errors zu vermeiden
        scope = len(lex)
    elif scope == -1:  # wenn kein wert angegeben
        scope = 10  # standardwert 10

    # erstelle liste aus x (=scope) einträgen + übersetzungen ['w1: t1, t2', 'w2: t1', ...]
    ret = [wort + ": " + ", ".join(lex[wort][0]) for wort in list(lex)[0:scope]]
    print("\n".join(ret))
    # parse letztes wort
    return list(lex)[scope - 1]


def print_related(klasse, wort):
    if klasse in "root":
        if wort in lex and not lex[wort][2][0] == ['']:
            print("Wurzel(n): {" + ", ".join(lex[wort][2][0]) + "}")
        else:
            print("Keine Wurzel gefunden")
    elif klasse in "rel":
        if wort in lex and not lex[wort][2][1] == ['']:
            print("Verwandte Wörter: {" + ", ".join(lex[wort][2][1]) + "}")
        else:
            print("Keine verwandten Wörter gefunden")
    elif klasse in "derv":
        if wort in lex and not lex[wort][2][2] == ['']:
            print("Abgeleitete Wörter: {" + ", ".join(lex[wort][2][2]) + "}")
        else:
            print("Keine abgeleiteten Wörter gefunden")


def print_syns(word):
    syn = synonyms(word)
    if syn:
        print(word + ": {" + ", ".join(syn) + "}")
    else:
        print("Keine Synonyme gefunden")


def print_pos(word):
    tags = pos(word)
    if tags:
        print("/".join(tags))
    else:
        print("Keinen POS-Tag gefunden")


def generate_words(eingabe):
    _, anzahl = separator(eingabe)  # lese anzahl wörter aus dem input heraus
    # kein wert oder wert 0 auf Standardwert 10 setzen
    if anzahl < 1:
        anzahl = 10

    gen_words = []  # liste der generierten wörter
    for z in range(anzahl):  # generiere (anzahl) wörter
        endstring = ""
        syllables = random.randrange(1, 4)  # ein wort kann 1, 2 oder 3 silben lang sein
        count = 0

        if random.randrange(10) < 7:  # chance von 70 % dass das wort mit einem konsonanten beginnt
            endstring += random.choice(consonants)

        while count < syllables:
            endstring += random.choice(vowels)
            endstring += random.choice(consonants)
            count += 1

        gen_words.append(endstring)

    print("\n".join(gen_words))


# wenn vowels=False werden û/â als u/a behandelt
def print_meta(vowels=False):
    länge, dictlet, dictstart = meta(vowels)
    # sortiere nach absteigender anzahl
    dictlet_sorted = sorted(dictlet.items(), key=lambda tup: tup[1], reverse=True)
    dictstart_sorted = sorted(dictstart.items(), key=lambda tup: tup[1], reverse=True)
    print("\nHäufigkeit Buchstaben:")
    for tupp in dictlet_sorted:
        print(tupp[0] + ": " + str(tupp[1]))
    print("\nHäufigkeit Anfangsbuchstaben:")
    for tupp in dictstart_sorted:
        print(tupp[0] + ": " + str(tupp[1]))
    print("\n" + str(länge) + " Einträge insgesamt")


# DICT MANIPULATION
def insert(item):
    if item not in lex or lex[item][0] == [""]:
        print(item)
        word = get_input("Bedeutung(en): ", "format")
        tag = get_input("POS: ").upper().split(",")
        for poz in tag:
            if poz not in POS:  # füge nur gültige pos tags hinzu
                tag.remove(poz)
        lex[item] = word, tag, [[""], [""], [""]]
        insert_poslist(tag, item)  # update verbs/nouns/adjs
    else:
        print(item)
        lex[item] = lex[item][0] + get_input("Bedeutungen: " + ", ".join(lex[item][0]) + ", ", "format"), \
            lex[item][1], lex[item][2]

    # entferne wörter aus liste unassigned, wenn sie zu wort hinzugefügt wurden
    [unassigned.remove(trans) for trans in lex[item][0] if trans in unassigned]

    print("Geänderter Eintrag:\n" + item + ": " + ", ".join(lex[item][0]) + "\n(" + "/".join(lex[item][1]) + ")")


def insert_notlist(word):
    unassigned.append(word.capitalize())


def delete(item):
    if check_antwort():
        lex.pop(item)
        print(item + " wurde gelöscht")


# bearbeite den POS Eintrag ('posb') oder überschreibe ihn ('posn')
def add_pos(item, word):
    if word in lex:
        tags = ""
        if lex[word][1] == [""]:
            print("Keinen POS Tag gefunden (" + word + ")")
            tags = get_input("new POS: ", "format")
        elif item == "posb":
            print("POS von " + word + ": " + ", ".join([tag + " (" + POS[tag] + ")" for tag in lex[word][1]]))
            tags = lex[word][1] + get_input("added POS: ", "format")
        elif item == "posn":
            print("POS von " + word + ": " + ", ".join([tag + " (" + POS[tag] + ")" for tag in lex[word][1]]))
            print("Vorsicht! Eintrag wird überschrieben. 'x' zum abbrechen")
            tags = get_input("new POS: ", "format")
            if "x" in tags:
                return
        if tags:
            lex[word] = lex[word][0], [t.upper() for t in tags if t.upper() in POS], lex[word][2]
            print("POS Tag(s): " + "/".join(lex[word][1]))
    else:
        print("Eintrag konnte nicht gefunden werden")


def edit_root(item, word):
    if word in lex:
        if lex[word][2][0] == [""]:  # wenn liste leer
            print("Keine Wurzel gefunden (" + word + ")")
            lex[word][2][0] = get_input("new root(s): ", "format")
        else:
            add_root(item, word)
        count = 1
        for wurz in lex[word][2][0]:
            if wurz in lex and word not in lex[wurz][2][2]:
                if lex[wurz][2][2] == [""]:
                    lex[wurz][2][2] = [word]  # leere einträge ersetzen
                else:
                    lex[wurz][2][2].append(word)
                count += 1

        print("Wurzel(n): " + ", ".join(lex[word][2][0]))
        print(str(count) + " Eintrag/Einträge geändert")
    else:
        print("Kein Eintrag vorhanden")


def add_root(item, word):
    print("root of " + word + ": " + ", ".join(lex[word][2][0]))
    if item == "rootb":
        # füge wurzeln hinzu, die noch nicht vorhanden sind
        lex[word][2][0] += [neu for neu in get_input("added root(s): ", "format") if neu not in lex[word][2][0]]
    elif item == "rootn":
        inpt = get_input("Vorsicht! Eintrag wird überschrieben.\nSchreibe 'x' um abzubrechen\nnew root(s): ", "format")
        if "x" not in inpt:
            # ersetze wurzeln durch input
            lex[word][2][0] = inpt


def edit_rel(item, word):
    if word in lex:
        if lex[word][2][1] == [""]:  # wenn liste leer
            print("Keine verwandten Wörter (" + word + ")")
            lex[word][2][1] = get_input("new word(s): ", "format")
        else:
            add_rel(item, word)

        count = 1
        for verw in lex[word][2][1]:
            if verw in lex and word not in lex[verw][2][1]:
                if lex[verw][2][1] == [""]:
                    lex[verw][2][1] = [word]
                else:
                    lex[verw][2][1].append(word)
                count += 1
        print("Verwandte Wörter: " + ", ".join(lex[word][2][1]))
        print(str(count) + " Eintrag/Einträge geändert")
    else:
        print("Kein Eintrag vorhanden")


def add_rel(item, word):
    print("Verwandte Wörter von '" + word + "': " + str(lex[word][2][1]))
    if item == "relb":
        # füge verwandte worte hinzu, die noch nicht vorhanden sind
        lex[word][2][1] += [neu for neu in get_input("added word(s): ", "format") if neu not in lex[word][2][1]]
    elif item == "reln":
        inpt = get_input("Vorsicht! Eintrag wird überschrieben.\nSchreibe 'x' um abzubrechen\nnew word(s): ", "format")
        if "x" not in inpt:
            # ersetze verwandte wörter durch input
            lex[word][2][1] = inpt


def edit_derv(item, word):
    if word in lex:
        if lex[word][2][2] == [""]:  # wenn liste leer
            print("Keine abgeleiteten Wörter (" + word + ")")
            lex[word][2][2] = get_input("new word(s): ", "format")
        else:
            add_derv(item, word)
        count = 1
        for derv in lex[word][2][2]:
            if derv in lex and word not in lex[derv][2][0]:
                if lex[derv][2][0] == [""]:
                    lex[derv][2][0] = [word]
                else:
                    lex[derv][2][0].append(word)
                count += 1
        print("Abgeleitete Wörter: " + ", ".join(lex[word][2][2]))
        print(str(count) + " Eintrag/Einträge geändert")
    else:
        print("Kein Eintrag gefunden")


def add_derv(item, word):
    print("Abgeleitete Wörter von '" + word + "': " + str(lex[word][2][2]))
    if item == "dervb":
        # füge abgeleitete worte hinzu, die noch nicht vorhanden sind
        lex[word][2][2] += [neu for neu in get_input("added word(s): ", "format") if neu not in lex[word][2][2]]
    elif item == "dervn":
        inpt = get_input("Vorsicht! Eintrag wird überschrieben.\nSchreibe 'x' um abzubrechen\nnew word(s): ", "format")
        if 'x' not in inpt:
            # ersetze abgeleitete wörter
            lex[word][2][2] = inpt


# GET INFO
def checkerito(item):
    if check_lex(item):
        print_entry(item)
    elif check_lex(item, unassigned):
        print("Noch kein Eintrag erstellt")
    else:
        print("Nischt jefunden!")


def search_empty():
    lex_notrans = []
    for entry in lex:
        if lex[entry][0] == [""]:  # finde einträge ohne übersetzung: wenn "liste übersetzungen" leer ist
            lex_notrans.append(entry)
    return lex_notrans


def random_entry(item):  # input: 'random[v/n/a][x], x = beliebige zahl
    (klasse, scope) = separator(item)

    if klasse[-1] == "v":  # zufälliges verb
        k = verbs
    elif klasse[-1] == "n":  # zufälliges nomen
        k = nouns
    elif klasse[-1] == "a":  # zufälliges adjektiv
        k = adjs
    else:  # zufälliges wort (liste aller keys/einträge)
        k = [entry for entry in lex.keys()]

    if scope < 1:
        scope = 1  # standardwert 1
    elif scope > len(k):
        scope = 5  # übermäßige Angaben werden auf 5 zurückgesetzt

    r = 0
    for number in range(scope):
        r = random.randrange(len(k))
        print(k[r])  # gebe zufälligen key aus der liste aus

    return k[r]


def pos(word):
    tags = []
    if word in lex and not lex[word][1] == [""]:  # wenn word und zugehörige pos tags vorhanden
        for tag in POS:
            if tag in lex[word][1]:
                tags.append(POS[tag])
    return tags


# finde synonyme
def synonyms(word):
    syn = []
    if word in lex:
        for entry in lex:
            if any(item in lex[word][0] for item in lex[entry][0]) and not word == entry:
                syn.append(entry)

    return syn


# berechne metadaten
# vowels: wenn False werden û/â als u/a behandelt
# return anzahl einträge, dict: häufigkeit buchstaben, dict: häufigkeit anfangsbuchstaben
def meta(vowels: bool):
    letter_counter = {letter: 0 for letter in alphabet}     # dict = {buchstabe: 0} für jeden buchstaben
    start_counter = {letter: 0 for letter in alphabet}      # " " "
    for entry in lex:
        if entry[0] in alphabet:
            start_counter[entry[0]] += 1    # zähle anfangsbuchstaben, ignoriere suffixe (starten mit "-")
        for char in entry:
            if char in alphabet:
                letter_counter[char] += 1   # zähle buchstaben

    # wenn vowels=False: û = u und â = a
    if not vowels:
        letter_counter["u"] += letter_counter.pop("û")
        letter_counter["a"] += letter_counter.pop("â")
        start_counter["u"] += start_counter.pop("û")
        start_counter["a"] += start_counter.pop("â")

    return len(lex), letter_counter, start_counter


# GRAMMAR
def print_grammar(gramlist, klasse):
    if gramlist == [] or klasse == "":
        print("Keine Grammatik verfügbar")
    elif klasse == "V":
        if gramlist[0]:
            print("Nominalisierung: " + gramlist[0])
        print("Imperativ: " + gramlist[1] + "! " + gramlist[2] + "!\n")
        print("Präsens:\t\tVergangenheit:\n" + gramlist[3] + "\t\t\t" + gramlist[6] + "\n" + gramlist[4] + "\t\t\t"
              + gramlist[7] + "\n" + gramlist[5] + "\t\t\t" + gramlist[8])
    elif klasse == "N":
        print("Nominativ: " + gramlist[3] + " / " + gramlist[1])
        print("Dativ: " + gramlist[4] + " / " + gramlist[5])
        print("Instrumentalis: " + gramlist[2] + " / " + gramlist[0])
    elif klasse == "PRO":
        print("Nominativ: " + gramlist[0] + "\nDativ: " + gramlist[1])
    elif klasse == "ART":
        print(", ".join(gramlist))
    elif klasse == "OTHER":
        print("/".join(gramlist))


# bilde alle grammatikalischen formen und ermittle die klasse
def grammar(word):
    table = []
    klasse = ""
    if word in lex:
        # verben
        if len(word) > 3 and "V" in lex[word][1]:
            table = grammar_verbs(word)
            klasse = "V"
        # nomen
        elif any(item in lex[word][1] for item in POS_noun):  # enthält 'liste pos' ein noun tag?
            table = grammar_nouns(word)
            klasse = "N"
        # pronomen
        elif "PRO" in lex[word][1]:
            table = [word, pronouns[word]]
            klasse = "PRO"
        # artikel
        elif word in articles:
            table = articles[word]
            klasse = "ART"
        # alles andere
        elif not lex[word][1] == [""]:
            table = pos(word)
            klasse = "OTHER"

    return table, klasse


def grammar_verbs(verb):
    # stamm ohne infinitiv-endung
    lemma = verb[:-3]
    if verb[-3] == "ð":
        lemma += "ƥ"

    # nominalisierung, imperativ, konjugation
    ret = [verbs_nominal(lemma)]
    [ret.append(imp) for imp in verbs_imp(lemma)]
    [ret.append(con) for con in verbs_conj(lemma)]
    return ret


# verben (nominalisierung)
def verbs_nominal(lemma):
    nom = ""
    if last_vowel(lemma) in ["a", "ā"]:
        if ends_in_vowel(lemma):
            nom = lemma + "'ul"
        else:
            nom = lemma + "ul"
    elif last_vowel(lemma) in ["u", "ū"]:
        if ends_in_vowel(lemma):
            nom = lemma + "'al"
        else:
            nom = lemma + "al"
    return nom


# verben (imperativ)
def verbs_imp(lemma):
    singular = lemma
    plural = lemma

    if last_vowel(lemma) in ["a", "ā", "â"]:
        if ends_in_vowel(singular):
            singular += "d"
        else:
            singular += "ad"
        plural = singular + "un"
    elif last_vowel(lemma) in ["u", "ū", "û"]:
        if ends_in_vowel(singular):
            singular += "d"
        else:
            singular += "ud"
        plural = singular + "an"
    # wörter mit einem stamm von 3 silben oder mehr wechseln den hinzugefügten vokal
    if vowel_counter(plural) >= 4:
        plural = plural[:-4] + last_vowel(plural) + plural[-3:]  # rukdān(a)dun -> rukdān(u)dun

    if lemma == "û":  # ûdar -> ud! ûdan!
        singular = "ud"

    return singular, plural


# verben (konjugation)
def verbs_conj(lemma):
    lemma = end_vowel(lemma)
    conj = [lemma + "a", lemma + "u", lemma + "ad", lemma + "ā", lemma + "ū", lemma + "ud"]
    # āXū/ā -> aXū/ā
    if last_vowel(lemma) == "ā":
        conj[3] = lemma[:-2] + "a" + lemma[-1] + "ā"
        conj[4] = lemma[:-2] + "a" + lemma[-1] + "ū"

    # ūXū/ā -> uXū/ā
    elif last_vowel(lemma) in ["ū", "û"]:
        conj[3] = lemma[:-2] + "u" + lemma[-1] + "ā"
        conj[4] = lemma[:-2] + "u" + lemma[-1] + "ū"

    # kā -> qa; kū -> qu
    elif ends_in(lemma) == "k":
        conj[3] = lemma[:-1] + "qa"
        conj[4] = lemma[:-1] + "qu"

    return conj


# nomen
def grammar_nouns(noun):
    lemma = end_vowel(noun)  # füge d hinzu, wenn auf vokal endet
    decl = []

    # instrumentalis plural, nominativ plural
    if vowel_counter(lemma) == 1 or last_vowel(lemma) in ["u", "ū", "û"]:
        # einsilbige nomen und solche die auf -u/-ū enden erhalten ein -(d)að/-(d)an
        decl = [lemma + "að", lemma + "an"]
    elif last_vowel(lemma) in ["a", "ā", "â"]:
        # nomen die auf -a/-ā enden erhalten ein -(d)uð/-(d)un
        decl = [lemma + "uð", lemma + "un"]

    # instrumentalis singular
    if noun[-1] == "d":
        # worte die auf "-ad" oder "-ād" enden, ersetzen die endung durch "-âda"
        if last_vowel(noun) in ["a", "ā"]:
            decl.append(noun[:-2] + "âda")
        # worte die auf "-ud" oder "-ūd" enden, ersetzen die endung durch "-ûda"
        elif last_vowel(noun) in ["u", "ū"]:
            decl.append(noun[:-2] + "ûda")
    else:
        # regelmäßige nomen erhalten ein "-da"
        decl.append(noun + "da")

    # nominativ, dativ, dativ plural (nom plural + dativ endung)
    if "N1" in lex[noun][1] or "PN1" in lex[noun][1]:
        decl.extend(["gu-" + noun, noun + "-gūn", decl[1] + "-gūn"])
    elif "N2" in lex[noun][1] or "PN2" in lex[noun][1]:
        decl.extend(["ga-" + noun, noun + "-gān", decl[1] + "-gān"])
    elif "N3" in lex[noun][1] or "PN3" in lex[noun][1]:
        decl.extend(["a-" + noun, noun + "-dān", decl[1] + "-dān"])

    # [inst pl, nom pl, inst sg, nom sg, dat sg, dat pl]
    return decl


# LEXIKON
def lexikon():
    print(hello)

    active = ""
    item = get_input("-> ").lower()  # erster input
    while not item == "tschö" and not item == "bye":  # beende mit befehl 'tschö' oder 'bye' die schleife (das programm)
        # füge special character ein
        item = item.replace("a|", "ā").replace("u|", "ū").replace("d|", "ð").replace("p|", "ƥ")

        if item not in operator:  # resete input nicht bei bestimmten meta befehlen
            active = item
        match item:
            case "":  # enter wird nicht gesucht, sondern übersprungen
                pass
            case "info":  # zeige mehr befehle
                print(info)
            case "infoling":  # zeige restliche befehle
                print(info_ling)
            case "all":  # zeige ganzes lexikon an
                print(lex)
            case item if "words" in item:  # zeige (x) einträge in rux
                active = print_words(item)
            case "trans":
                print_trans(active)
            case "active":
                print(active)
            case "syn":     # zeige synonyme
                active = swap(active)
                print_syns(active)
            case "len":
                print(str(len(lex)) + " Einträge!")
            case item if "verbs" in item:  # printe liste mit x einträgen von wortklasse
                print_class(item)
            case item if "nouns" in item:
                print_class(item)
            case item if "adjs" in item:
                print_class(item)
            case item if "random" in item:  # zeige x zufällige worte an ([v]erbs,[a]djectives,[n]ouns)
                active = random_entry(item)
            case "empty":  # zeige alle wörter an, die noch keine übersetzung haben
                print_empty()
            case "notlist":
                print_empty("unassigned")
            case "give d":  # um special character zu bekommen:
                print("ð")
            case "vowels":
                print("û, â, ū, ā")
            case "abc":
                print("ð ā n d r u g ƥ k a l x ū q")
            case "b":  # eintrag bearbeiten
                active = swap(active)
                insert(active)
            case "del":  # eintrag löschen (nach nachfrage)
                active = swap(active)
                delete(active)
            case "g":  # grammatik printen
                active = swap(active)
                liste, klasse = grammar(active)
                print_grammar(liste, klasse)
            case "pos":  # zeige part of speech tag
                active = swap(active)
                print_pos(active)
            case "posb" | "posn":   # bearbeite part of speech tag
                add_pos(item, active)
            case item if "root" in item:
                active = swap(active)
                if item == "root":  # 'root' zeigt den wurzeleintrag
                    print_related(item, active)
                else:  # 'rootb' fügt neue wurzeln hinzu, 'rootn' ersetzt sie
                    edit_root(item, active)
            case item if "rel" in item:
                active = swap(active)
                if item == "rel":  # 'rel' zeigt verwandte wörter
                    print_related(item, active)
                else:  # 'relb' fügt neue verwandte wörter hinzu, 'reln' ersetzt sie
                    edit_rel(item, active)
            case item if "derv" in item:
                active = swap(active)
                if item == "derv":  # 'derv' bearbeitet abgeleitete wörter
                    print_related(item, active)
                else:  # 'dervb' fügt neue abgeleitete wörter hinzu, 'dervn' ersetzt sie
                    edit_derv(item, active)
            case "add":
                insert_notlist(active)
            case "save":
                save()
            case "meta":
                print_meta()
            case "metavowels":
                print_meta(True)
            case item if "generate" in item:
                generate_words(item)
            case _:  # wenn wort noch nicht vorhanden oder ohne übersetzung ist
                checkerito(item)

        item = get_input("-> ").lower()  # neuer input

    if item == "bye":
        print("Goodbye sir!")
    else:
        print("Tschüss!")

    sleep(0.6)


if __name__ == '__main__':
    lexikon()
