import random

# ['Ak', 'Akamah', 'Amaka', 'Amaka (Regelwerk)', 'Attribute', 'Augling', 'Augling (Regelwerk)', 'Avzitil', 'Avztil (Regelwerk)', 'Baumgeister', 'Berethao', 'Berge von Loromoth', 'Blauer Traum', 'Blib', 'Blutborke', 'Bodengolem', 'Charakterbogen', "Cul'thur", 'Cureg', 'Drah', 'Dras und Drus', 'Dras und Drus Feldzug', 'Draske', 'Draske (Regelwerk)', 'Drasna', 'Elb', 'Elb (Regelwerk)', 'Elbenkriege', 'Entstehung der Welt', 'Feuergolem', 'Flossenbeutler', 'Fluggolem', 'Fluropilz', 'Flüche', 'Frostwein', 'Förun', 'Gebirge', 'Gegner', 'Gemüsegolem', 'Geologie', 'Gesteinsgolem', 'Gewässer', 'Giftgolem', 'Glaubenskriege', 'Gloq', 'Golem', 'Große Persönlichkeiten', 'Guqual', 'Guqual (Regelwerk)', 'Halluzinationspilz', 'Himmelserz', 'Himmelsregen', 'Ideen', 'Ideen (Tiere)', 'Illoda', 'Inseln', 'Kalender/Zeitr', 'Kampf', 'Karte', "Keil'O Renn", 'Kiesenriller-Maus', 'Kncohengolem', 'Knochendorn', 'Koberinth', 'Kuberika', 'Kwin Stalbu', 'Lachratte', 'Loromoth', 'Magie', 'Mensch', 'Menschen Vernichtung', 'Minort (Stalbu)', 'Mithadium', 'Mond', 'Namen', 'Nautrphänomene', 'Parasitkäfer', 'Pflanzengolem', 'Pilze', 'Psychogolem', 'Puletsi', 'Quork', 'Quork (Regelwerk)', "Ras'qath", 'Regeln', 'Religion', 'Religion (Regelwerk)', 'Ruryx', 'Ry', 'Sauerbaum', 'Schlafplanze (Blauer Traum)', 'Schlangenrausch', 'Schreiender Triesel', 'Schwarze Löcher', 'Segen', 'Sonne', 'Sonnensytem', 'Stalbu', 'Suru', 'Säuregolem', 'Triesel', 'Trivia Gott', 'Trollbrücke', 'Tropfbeutel', 'Tropfbeutler', 'Turninch', 'Unhabhängigkeitskriege von Puletsi', 'Vadon', 'Vadonier', 'Vadonier (Regelwerk)', 'Vaiad', 'Verfluchte Wesen', 'Verfluchter Quork', 'Versiegeltes Schloss', 'Vier Elemente', 'Waffenklassen', 'Wassergolem', 'Wichtige Daten', 'Wirinima', 'Wrethh', 'Währung', 'Xaraton', 'Zeitrechnung', 'Übernehmen (Natur)']
vowels = ["a", "u", "ū", "ā"]
consonants = ["x", "g", "q", "l", "r", "n", "ð", "d", "k"]
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
    "PRO": "Pronomen", "JA": "Ja", "NO": "Nein"
}
POS_noun = ["N1", "N2", "N3", "PN1", "PN2", "PN3"]
POS_det = ["DET1", "DET2", "DET3"]
info = "Befehle:\n'all' = Ganzes Lexikon\n'words' = Alle Einträge ohne Übersetzung\n'len' = Anzahl Einträge" \
       "\n'random[v/n/a]' = Zufälliges Wort (Verb/Nomen/Adjektiv)'\n'empty' = Zeige alle Einträge ohne Überetzung an" \
       "\n'verbs[zahl]' = Zeige [zahl] an Verben (Keine Angabe = 10, 0 = alle)" \
       "\n'nouns[zahl]' = Zeige [zahl] an Nomen (Keine Angabe = 10, 0 = alle)" \
       "\n'adj[zahl]' = Zeige [zahl] an Adjektiven (Keine Angabe = 10, 0 = alle)" \
       "\n'save' = Speichern\n'tschö' = Beenden OHNE speichern\n'give d' = get d" \
       "\n'vowels' = print special vowels\n'abc' = ganzes Alphabet" \
       "\na|/u|/d| = ā/ū/ð\n+'infoling' = more info"
info_ling = "Weitere Befehle:\n'b' = Bearbeite den letztgesuchten Eintrag\n'del' = Lösche den letztgesuchten Eintrag" \
            "\n'g' = Bilde grammatikalische Formen des letztgesuchten Eintrags" \
            "\n'pos' = Zeige POS-Tag des letztgesuchten Eintrags" \
            "\n'root'/'rootb' = Zeige/bearbeite Wurzel(n) des Wortes" \
            "\n'rel'/'relb' = Zeige/bearbeite verwandte Wörter" \
            "\n'derv'/'dervb' = Zeige/bearbeite abgeleitete Wörter\na|/u|/d| = ā/ū/ð\n-'info' = Info"
operator = ["b", "g", "pos", "root", "rel", "derv", "rootb", "relb", "dervb", "del", "trans", "info", "infoling"]
# import dict from file
lex_file = open("rux_lex", "r", encoding="utf-8")
lex_cont = lex_file.read()
lex_list = lex_cont[:-1].split(".")  # split aber ignoriere letzten punkt (sonst gibts nen leeren eintrag)
lex = {}
for x in lex_list:  # erstelle dict
    (key, val, pos, his) = x.split(":")  # trenne eintrag und bedeutungen (+pos tag und verwandte wörter)
    (root, rel, der) = his.split(">")  # trenne verwandte wörter in wurzel und ableitungen
    # erstelle liste von allen bedeutungen   (wort: ([bedeutungen], [pos], [[wurzel], [verwandt], [ableitungen]])
    lex[key] = val.split(","), pos.split(","), [root.split(","), rel.split(","), der.split(",")]
lex_file.close()

verbs = [word for word in lex if "V" in lex[word][1]]  # erstelle liste aller verben
nouns = [word for word in lex if any(item in lex[word][1] for item in POS_noun)]  # erstelle liste aller nomen
adj = [word for word in lex if "ADJ" in lex[word][1]]  # erstelle liste aller adjektive


def save():
    with open("rux_lex", "w", encoding="utf-8") as f:
        for entry in lex:
            f.write(
                entry + ":" + ",".join(lex[entry][0]) + ":" + ",".join(lex[entry][1]) + ":" + ",".join(lex[entry][2][0])
                + ">" + ",".join(lex[entry][2][1]) + ">" + ",".join(lex[entry][2][2]) + ".")
    print("Lexikon gesichert:")
    print(str(len(lex)) + " Einträge")


def get_input(prompt, form=""):
    if not form:
        item = input(prompt)
    else:
        item = input(prompt).replace(" ", "").replace("_", " ").replace("a|", "ā") \
            .replace("u|", "ū").replace("d|", "ð").split(",")
    return item


# helper function, um input in buchstaben/zahlen zu trennen
def separator(text):
    dig = "0123456789"  # definiere ziffern
    string = ""  # buchstaben in input
    number = ""  # zahlen in input
    for char in text:
        if char in dig:  # wenn char eine zahl, füge zu 'number' hinzu, sonst zu 'string'
            number += char
        else:
            string += char
    if not number:  # wenn keine zahl vorhanden, number = -1
        number = -1
    else:
        number = int(number)  # konvertiere number zu integer
    return string, number


def check_lex(item):
    check = False
    for entry in lex:
        if item == entry or item in (trans.lower() for trans in
                                     lex[entry][0]):  # item in eintrag oder in liste_bedeutungen (caseinsensitive)
            print("Folgenden Eintrag gefunden:\n" + entry + ": " + ", ".join(lex[entry][0]))
            check = True
    return check


def check_antwort(prompt="Bist du sicher? j/n\n"):
    ant = get_input(prompt)
    while not ant == "j" and not ant == "n":
        ant = get_input("j/n?: ")
    if ant == "j":
        return True
    else:
        return False


def print_trans(word):
    if not lex[word][0] == [""]:  # checke, ob übersetzungen vorhanden sind
        print(", ".join(lex[word][0]))
    else:
        print("Keine Übersetzung gefunden")


def insert(item):
    if item not in lex or lex[item][0] == [""]:
        print(item)
        word = get_input("Bedeutung(en): ", "format")
        tag = get_input("POS: ").upper().split(",")
        for poz in tag:
            if poz not in POS:  # füge nur gültige pos tags hinzu
                tag.remove(poz)
        lex[item] = word, tag, [[""], [""], [""]]
    else:
        print(item)
        lex[item] = lex[item][0] + get_input("Bedeutungen: " + ", ".join(lex[item][0]) + ", ", "format"), \
            lex[item][1], lex[item][2]
    print("Geänderter Eintrag:\n" + item + ": " + ", ".join(lex[item][0]) + ", " + "/".join(lex[item][1]))


def delete(item):
    if check_antwort():
        lex.pop(item)
        print(item + " wurde gelöscht")


def edit_root(word):
    if lex[word][2][0] == [""]:  # wenn liste leer
        print("Keine Wurzel gefunden (" + word + ")")
        lex[word][2][0] = get_input("new root(s): ", "format")
    else:
        print("root of " + word + ": " + ", ".join(lex[word][2][0]))
        lex[word][2][0] += get_input("added root(s): ", "format")
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


def edit_rel(word):
    if lex[word][2][1] == [""]:  # wenn liste leer
        print("Keine verwandten Wörter (" + word + ")")
        lex[word][2][1] = get_input("new word(s): ", "format")
    else:
        print("Verwandte Wörter von '" + word + "': " + str(lex[word][2][1]))
        lex[word][2][1] += get_input("added word(s): ", "format")
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


def edit_derv(word):
    if lex[word][2][2] == [""]:  # wenn liste leer
        print("Keine abgeleiteten Wörter (" + word + ")")
        lex[word][2][2] = get_input("new word(s): ", "format")
    else:
        print("Abgeleitete Wörter von '" + word + "': " + str(lex[word][2][2]))
        lex[word][2][2] += get_input("added word(s): ", "format")
    count = 1
    for derv in lex[word][2][2]:
        if derv in lex and word not in lex[derv][2][0]:
            if lex[derv][2][0] == [""]:
                lex[derv][2][0] = word
            else:
                lex[derv][2][0].append(word)
            count += 1
    print("Abgeleitete Wörter: " + ", ".join(lex[word][2][2]))
    print(str(count) + " Eintrag/Einträge geändert")


# print liste an einträgen. item = input (bestimmt wortart)
def print_entry(item):
    (klasse, scope) = separator(item)  # trenne input in wort (klasse) und anzahl einträge (scope)
    if scope == -1:  # wenn kein wert angegeben
        scope = 10  # standardwert 10

    if klasse == "verbs":
        if scope == 0:  # scope = 0 -> alle verben
            scope = len(verbs)
        print("\n".join(verbs[-scope:]))  # printe die letzten x verben, x = scope
        print(str(len(verbs)) + " Verben gefunden")
    elif klasse == "nouns":
        if scope == 0:  # scope = 0 -> alle nomen
            scope = len(nouns)
        print("\n".join(nouns[-scope:]))  # printe die letzten x nomen, x = scope
        print(str(len(nouns)) + " Nomen gefunden")
    elif klasse == "adj":
        if scope == 0:  # scope = 0 -> alle adjektive
            scope = len(adj)
        print("\n".join(adj[-scope:]))  # printe die letzten x adjektive, x = scope
        print(str(len(adj)) + " Adjektive gefunden")


def search_empty():
    lex_notrans = []
    for entry in lex:
        if lex[entry][0] == [""]:  # finde einträge ohne übersetzung: wenn "liste übersetzungen" leer ist
            lex_notrans.append(entry)
    return lex_notrans


def random_entry(item):
    if item[-1] == "v":  # zufälliges verb
        r = random.randrange(len(verbs))
        k = verbs
    elif item[-1] == "n":  # zufälliges nomen
        r = random.randrange(len(nouns))
        k = nouns
    elif item[-1] == "a":  # zufälliges adjektiv
        r = random.randrange(len(adj))
        k = adj
    else:
        r = random.randrange(len(lex))  # zufällige zahl in range(0, anzahl_einträge)
        k = [entr for entr in lex.keys()]  # liste aller keys (einträge)
    print(k[r])  # gebe zufälligen key aus der liste aus
    return k[r]


def swap(active):  # wenn active eine übersetzung und kein eintrag ist, setze active auf entsprechenden eintrag
    for entry in lex:  # checken, ob der zuvor gesuchte eintrag existiert als übersetzung
        if active in (trans.lower() for trans in lex[entry][0]):
            active = entry  # setze active auf das wort des eintrages, wenn übersetzung gefunden
    return active


def pos(word):
    if word in lex and not lex[word][1] == [""]:  # wenn word und zugehörige pos tags vorhanden
        tags = []
        for tag in POS:
            if tag in lex[word][1]:
                tags.append(POS[tag])
        return tags
    else:
        return "Keinen POS-Tag gefunden"


# print alle grammatikalischen formen
def grammar(word):
    # verben
    if len(word) > 3 and "V" in lex[word][1]:
        grammar_verbs(word)
    # nomen
    elif any(item in lex[word][1] for item in POS_noun):  # enthält 'liste pos' ein noun tag?
        grammar_nouns(word)
    # pronomen
    elif "PRO" in lex[word][1]:
        grammar_pronouns(word)
    # artikel
    elif word in articles:
        print(", ".join(articles[word]))
    # alles andere
    elif not lex[word][1] == [""]:
        print(word)
        print(pos(word))
    else:
        print("Keine Grammatik verfügbar")


def grammar_verbs(word):
    lemma = word[:-3]
    # nominalisierung
    if lemma[-1] == "a" or lemma[-1] == "ā":
        print("Nominalisierung: " + lemma + "'ul\n")
    elif lemma[-2] == "a" or lemma[-2] == "ā":
        print("Nominalisierung: " + lemma + "ul\n")
    elif lemma[-1] == "u" or lemma[-1] == "ū":
        print("Nominalisierung: " + lemma + "'al\n")
    elif lemma[-2] == "u" or lemma[-2] == "ū":
        print("Nominalisierung: " + lemma + "al\n")
    lemma = ends_in_vowel(lemma)
    if lemma[-2] == "ā":
        print("Präsens:\tVergangenheit:\n" + lemma + "a\t\t" + lemma[:-2] + "â" + lemma[-1] + "ā\n"
              + lemma + "u\t\t" + lemma[:-2] + "â" + lemma[-1] + "ū\n"
              + lemma + "ad\t\t" + lemma + "ud")
    elif lemma[-2] == "ū":
        print("Präsens:\tVergangenheit:\n" + lemma + "a\t\t" + lemma[:-2] + "û" + lemma[-1] + "ā\n"
              + lemma + "u\t\t" + lemma[:-2] + "û" + lemma[-1] + "ū\n"
              + lemma + "ad\t\t" + lemma + "ud")
    else:
        print("Präsens:\tVergangenheit:\n" + lemma + "a\t\t" + lemma + "ā\n" + lemma + "u\t\t"
              + lemma + "ū\n" + lemma + "ad\t\t" + lemma + "ud")


def grammar_nouns(word):
    lemma = ends_in_vowel(word)  # füge d hinzu, wenn auf vokal endet
    if "N1" in lex[word][1] or "PN1" in lex[word][1]:
        print("Nominativ: gu-" + word + "\nDativ: " + word + "-gūn")
    elif "N2" in lex[word][1] or "PN2" in lex[word][1]:
        print("Nominativ: ga-" + word + "\nDativ: " + word + "-gān")
    elif "N3" in lex[word][1] or "PN3" in lex[word][1]:
        print("Nominativ: a-" + word + "\nDativ: " + word + "-dān")

    if lemma[-2] == "a" or lemma[-2] == "ā":
        print("Plural: " + lemma + "un")
    elif lemma[-2] == "u" or lemma[-2] == "ū":
        print("Plural: " + lemma + "an")


def grammar_pronouns(word):
    print("Dativ: " + pronouns[word])


def ends_in_vowel(word):
    if word[-1] in vowels:  # worte die auf einen vokal enden, fügen ein d- zum suffix hinzu
        word = word + "d"
    return word


def lexikon():
    print("Moin!\n'words' = Alle Einträge\n'save' = speichern\n'tschö' = beenden OHNE speichern"
          "\n'b' = bearbeiten\n'del' = löschen\n'g' = Grammatik\n'info' = Info")

    active = ""
    item = get_input("-> ").lower()  # erster input
    while not item == "tschö" and not item == "bye":  # beende mit befehl 'tschö' oder 'bye' die schleife (das programm)
        item = item.replace("a|", "ā").replace("u|", "ū").replace("d|", "ð")  # füge special character ein

        if item not in operator:  # resete input nicht bei bestimmten befehlen
            active = item
        if item == "":  # enter wird nicht gesucht, sondern übersprungen
            pass
        elif item == "info":  # zeige alle befehle
            print(info)
        elif item == "infoling":
            print(info_ling)
        elif item == "all":  # zeige ganzes lexikon an
            print(lex)
        elif item == "words":  # zeige alle einträge in rux
            for word in lex:
                print(word)
            print(str(len(lex)) + " words")
        elif item == "trans":
            print_trans(active)
        elif item == "len":
            print(str(len(lex)) + " Einträge!")
        elif "verbs" in item or "nouns" in item or "adj" in item:  # printe liste mit x einträgen von wortklasse
            print_entry(item)
        elif "random" in item:  # zeige zufälliges wort
            active = random_entry(item)
        elif item == "empty":  # zeige alle wörter an, die noch keine übersetzung haben
            print(search_empty())
        elif item == "give d":  # um special character zu bekommen:
            print("ð")
        elif item == "vowels":
            print("û, â, ū, ā")
        elif item == "abc":
            print("ð ā n d r u g k a l x ū q")
        elif item == "b":  # eintrag bearbeiten
            active = swap(active)
            insert(active)
        elif item == "del":  # eintrag löschen (nach nachfrage)
            active = swap(active)
            delete(active)
        elif item == "g":  # grammatik printen
            active = swap(active)
            grammar(active)
        elif item == "pos":  # part of speech tag
            active = swap(active)
            print(pos(active))
        elif item in "rootb":
            if item[-1] == "b":  # 'rootb' bearbeitet den wurzeleintrag
                active = swap(active)
                edit_root(active)
            else:  # 'root' zeigt die wurzel an
                active = swap(active)
                print(lex[active][2][0])
        elif item in "relb":
            if item[-1] == "b":  # 'relb' bearbeitet verwandte wörter
                active = swap(active)
                edit_rel(active)
            else:  # 'rel' zeigt verwandte wörter an
                active = swap(active)
                print(lex[active][2][1])
        elif item in "dervb":
            if item[-1] == "b":  # 'dervb' bearbeitet abgeleitete wörter
                active = swap(active)
                edit_derv(active)
            else:  # 'derv' zeigt abgeleitete wörter an
                active = swap(active)
                print(lex[active][2][2])
        elif item == "save":
            save()
        else:  # wenn wort noch nicht vorhanden oder ohne übersetzung ist
            if not check_lex(item):
                print("Nischt jefunden")

        item = get_input("-> ").lower()  # neuer input

    if item == "bye":
        print("Goodbye sir!")
    else:
        print("Tschüss!")


if __name__ == '__main__':
    lexikon()
