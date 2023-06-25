import random

# ['Ak', 'Akamah', 'Amaka', 'Amaka (Regelwerk)', 'Attribute', 'Augling', 'Augling (Regelwerk)', 'Avzitil', 'Avztil (Regelwerk)', 'Baumgeister', 'Berethao', 'Berge von Loromoth', 'Blauer Traum', 'Blib', 'Blutborke', 'Bodengolem', 'Charakterbogen', "Cul'thur", 'Cureg', 'Drah', 'Dras und Drus', 'Dras und Drus Feldzug', 'Draske', 'Draske (Regelwerk)', 'Drasna', 'Elb', 'Elb (Regelwerk)', 'Elbenkriege', 'Entstehung der Welt', 'Feuergolem', 'Flossenbeutler', 'Fluggolem', 'Fluropilz', 'Flüche', 'Frostwein', 'Förun', 'Gebirge', 'Gegner', 'Gemüsegolem', 'Geologie', 'Gesteinsgolem', 'Gewässer', 'Giftgolem', 'Glaubenskriege', 'Gloq', 'Golem', 'Große Persönlichkeiten', 'Guqual', 'Guqual (Regelwerk)', 'Halluzinationspilz', 'Himmelserz', 'Himmelsregen', 'Ideen', 'Ideen (Tiere)', 'Illoda', 'Inseln', 'Kalender/Zeitr', 'Kampf', 'Karte', "Keil'O Renn", 'Kiesenriller-Maus', 'Kncohengolem', 'Knochendorn', 'Koberinth', 'Kuberika', 'Kwin Stalbu', 'Lachratte', 'Loromoth', 'Magie', 'Mensch', 'Menschen Vernichtung', 'Minort (Stalbu)', 'Mithadium', 'Mond', 'Namen', 'Nautrphänomene', 'Parasitkäfer', 'Pflanzengolem', 'Pilze', 'Psychogolem', 'Puletsi', 'Quork', 'Quork (Regelwerk)', "Ras'qath", 'Regeln', 'Religion', 'Religion (Regelwerk)', 'Ruryx', 'Ry', 'Sauerbaum', 'Schlafplanze (Blauer Traum)', 'Schlangenrausch', 'Schreiender Triesel', 'Schwarze Löcher', 'Segen', 'Sonne', 'Sonnensytem', 'Stalbu', 'Suru', 'Säuregolem', 'Triesel', 'Trivia Gott', 'Trollbrücke', 'Tropfbeutel', 'Tropfbeutler', 'Turninch', 'Unhabhängigkeitskriege von Puletsi', 'Vadon', 'Vadonier', 'Vadonier (Regelwerk)', 'Vaiad', 'Verfluchte Wesen', 'Verfluchter Quork', 'Versiegeltes Schloss', 'Vier Elemente', 'Waffenklassen', 'Wassergolem', 'Wichtige Daten', 'Wirinima', 'Wrethh', 'Währung', 'Xaraton', 'Zeitrechnung', 'Übernehmen (Natur)']
vowels = ["a", "u", "ū", "ā", "û", "â"]
consonants = ["x", "g", "q", "l", "r", "n", "ð", "d", "k", "ƥ"]
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
hello = "Moin!\n'words' = Einträge mit Übersetzung\n'random' = zufälliges Wort\n'save' = speichern" \
        "\n'tschö' = beenden OHNE speichern\n'b' = bearbeiten\n'del' = löschen\n'g' = Grammatik\n'info' = Info"
info = "Befehle:\n'all' = Ganzes Lexikon\n'len' = Anzahl Einträge\n'active' = Zeige aktuelles Wort an" \
       "\n'empty' = Zeige alle Einträge ohne Übersetzung an" \
       "\n'notlist = Zeige alle Übersetzungen ohne Eintrag an" \
       "\n'random[v/n/a][zahl]' = (Anzahl) zufällige Worte [Verb/Nomen/Adjektiv] (Keine Angabe = 1)" \
       "\n'words[zahl]' = Zeige [zahl] Wörter mit Übersetzung (Keine Angabe = 10, 0 = alle)" \
       "\n'verbs[zahl]' = Zeige [zahl] an Verben (Keine Angabe = 10, 0 = alle)" \
       "\n'nouns[zahl]' = Zeige [zahl] an Nomen (Keine Angabe = 10, 0 = alle)" \
       "\n'adj[zahl]' = Zeige [zahl] an Adjektiven (Keine Angabe = 10, 0 = alle)" \
       "\n'save' = Speichern\n'tschö' = Beenden OHNE speichern\n'give d' = get d" \
       "\n'vowels' = print special vowels\n'abc' = ganzes Alphabet" \
       "\na|/u|/d| = ā/ū/ð\n+'infoling' = more info"
info_ling = "Weitere Befehle:\n'b' = Bearbeite den letztgesuchten Eintrag\n'del' = Lösche den letztgesuchten Eintrag" \
            "\n'g' = Bilde grammatikalische Formen des letztgesuchten Eintrags" \
            "\n'pos' = Zeige POS-Tag des letztgesuchten Eintrags" \
            "\n'trans' = Zeige Übersetzung(en)\n'syn' = Zeige Synonyme an" \
            "\n'root'/'rootb' = Zeige/bearbeite Wurzel(n) des Wortes" \
            "\n'rel'/'relb' = Zeige/bearbeite verwandte Wörter" \
            "\n'derv'/'dervb' = Zeige/bearbeite abgeleitete Wörter\na|/u|/d| = ā/ū/ð\n-'info' = Info"
operator = ["b", "g", "pos", "root", "rel", "derv", "rootb", "relb", "dervb", "del", "trans", "active", "syn",
            "info", "infoling", "save"]
exceptions = {"ûdar": ["V", ["ûda", "ûdu", "ûdad"], ["udā", "udū", "ûdud"]]}
# import dict from file
lex_file = open("rux_lex", "r", encoding="utf-8")
lex_cont = lex_file.readline()
unassigned = lex_file.readline()[:-1].split("\\")   # erstelle liste von übersetzungen ohne eintrag
lex_list = lex_cont[:-2].split("\\")     # split aber ignoriere letzten punkt und \n (sonst gibts nen leeren eintrag)
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
            .replace("u|", "ū").replace("d|", "ð").split(",")
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


# get last vowel
def last_vowel(string):
    vowel = ""
    for letter in reversed(string):
        if letter in vowels:
            vowel = letter
            break
    return vowel


def end_vowel(word):
    if ends_in_vowel(word):  # worte die auf einen vokal enden, fügen ein d- zum suffix hinzu
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


# PRINTERS
def print_entry(word):  # printe eintrag aus lex
    for entry in lex:
        if word == entry or word in (trans.lower() for trans in
                                     lex[entry][0]):  # item in eintrag oder in liste_bedeutungen (caseinsensitive)
            print("Folgenden Eintrag gefunden:\n" + entry + ": " + ", ".join(lex[entry][0]))


def print_empty(liste="empty"):
    if liste == "empty":    # worte ohne übersetzung
        cont = search_empty()
    elif liste == "unassigned":     # übersetzung ohne eintrag
        cont = unassigned
    else:
        return

    print("\n".join(cont))


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
    else:
        print("Inkorrekte Eingabe")


def print_words(item):
    _, scope = separator(item)  # trenne input ('words') von gewünschter anzahl (scope)
    if scope > len(lex) or scope == 0:     # scope = 0 -> alle wörter; und catche ob input > len um errors zu vermeiden
        scope = len(lex)
    elif scope == -1:   # wenn kein wert angegeben
        scope = 10      # standardwert 10

    # erstelle liste aus x (=scope) einträgen + übersetzungen ['w1: t1, t2', 'w2: t1', ...]
    ret = [wort+": "+", ".join(lex[wort][0]) for wort in list(lex)[0:scope]]
    print("\n".join(ret))
    # parse letztes wort
    return list(lex)[scope-1]


def print_related(klasse, wort):
    if klasse in "root":
        if wort in lex and not lex[wort][2][0] == ['']:
            print("Wurzel(n): {"+", ".join(lex[wort][2][0])+"}")
        else:
            print("Keine Wurzel gefunden")
    elif klasse in "rel":
        if wort in lex and not lex[wort][2][1] == ['']:
            print("Verwandte Wörter: {"+", ".join(lex[wort][2][1])+"}")
        else:
            print("Keine verwandten Wörter gefunden")
    elif klasse in "derv":
        if wort in lex and not lex[wort][2][2] == ['']:
            print("Abgeleitete Wörter: {"+", ".join(lex[wort][2][2])+"}")
        else:
            print("Keine abgeleiteten Wörter gefunden")


def print_syns(word):
    syn = synonyms(word)
    if syn:
        print(word + ": {" + ", ".join(syn) + "}")
    else:
        print("Keine Synonyme gefunden")


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
    else:
        print(item)
        lex[item] = lex[item][0] + get_input("Bedeutungen: " + ", ".join(lex[item][0]) + ", ", "format"), \
            lex[item][1], lex[item][2]
    print("Geänderter Eintrag:\n" + item + ": " + ", ".join(lex[item][0]) + "\n(" + "/".join(lex[item][1])+")")


def insert_notlist(word):
    unassigned.append(word.capitalize())


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
                lex[derv][2][0] = [word]
            else:
                lex[derv][2][0].append(word)
            count += 1
    print("Abgeleitete Wörter: " + ", ".join(lex[word][2][2]))
    print(str(count) + " Eintrag/Einträge geändert")


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


def random_entry(item):     # input: 'random[v/n/a][x], x = beliebige zahl
    (klasse, scope) = separator(item)

    if klasse[-1] == "v":  # zufälliges verb
        k = verbs
    elif klasse[-1] == "n":  # zufälliges nomen
        k = nouns
    elif klasse[-1] == "a":  # zufälliges adjektiv
        k = adj
    else:                   # zufälliges wort (liste aller keys/einträge)
        k = [entry for entry in lex.keys()]

    if scope < 1:
        scope = 1   # standardwert 1
    elif scope > len(k):
        scope = 5   # übermäßige Angaben werden auf 5 zurückgesetzt

    r = 0
    for number in range(scope):
        r = random.randrange(len(k))
        print(k[r])  # gebe zufälligen key aus der liste aus

    return k[r]


def pos(word):
    if word in lex and not lex[word][1] == [""]:  # wenn word und zugehörige pos tags vorhanden
        tags = []
        for tag in POS:
            if tag in lex[word][1]:
                tags.append(POS[tag])
        return tags
    else:
        return "Keinen POS-Tag gefunden"


# finde synonyme
def synonyms(word):
    syn = []
    for entry in lex:
        if any(item in lex[word][0] for item in lex[entry][0]) and not word == entry:
            syn.append(entry)

    return syn

# GRAMMAR

# print alle grammatikalischen formen
def grammar(word):
    if word not in lex:
        print("Keine Grammatik verfügbar")
    # verben
    elif len(word) > 3 and "V" in lex[word][1]:
        grammar_verbs(word)
    # nomen
    elif any(item in lex[word][1] for item in POS_noun):  # enthält 'liste pos' ein noun tag?
        grammar_nouns(word)
    # pronomen
    elif "PRO" in lex[word][1]:
        grammar_pronouns(word)
    # artikel
    elif word in articles:
        grammar_articles(word)
    # alles andere
    elif not lex[word][1] == [""]:
        print(word)
        print(pos(word))


def grammar_verbs(verb):
    lemma = verb[:-3]
    # nominalisierung
    if last_vowel(lemma) in ["a", "ā"]:
        if ends_in_vowel(lemma):
            print("Nominalisierung: " + lemma + "'ul\n")
        else:
            print("Nominalisierung: " + lemma + "ul\n")
    elif last_vowel(lemma) in ["u", "ū"]:
        if ends_in_vowel(lemma):
            print("Nominalisierung: " + lemma + "'al\n")
        else:
            print("Nominalisierung: " + lemma + "al\n")

    lemma = end_vowel(lemma)
    conj = [lemma + "a", lemma + "u", lemma + "ad", lemma + "ā", lemma + "ū", lemma + "ud"]
    # āXū/ā -> âXū/ā
    if last_vowel(lemma) == "ā":
        if vowel_counter(lemma) == 1:   # one syllable words lose the guttural
            conj[3] = lemma[:-2] + "a" + lemma[-1] + "ā"
            conj[4] = lemma[:-2] + "a" + lemma[-1] + "ū"
        else:
            conj[3] = lemma[:-2] + "â" + lemma[-1] + "ā"
            conj[4] = lemma[:-2] + "â" + lemma[-1] + "ū"
    # ūXū/ā -> ûXū/ā
    elif last_vowel(lemma) in ["ū", "û"]:
        if vowel_counter(lemma) == 1:   # one syllable words lose the guttural
            conj[3] = lemma[:-2] + "u" + lemma[-1] + "ā"
            conj[4] = lemma[:-2] + "u" + lemma[-1] + "ū"
        else:
            conj[3] = lemma[:-2] + "û" + lemma[-1] + "ā"
            conj[4] = lemma[:-2] + "û" + lemma[-1] + "ū"
    # kā -> qa; kū -> qu
    elif ends_in(lemma) == "k":
        conj[3] = lemma[:-1] + "qa"
        conj[4] = lemma[:-1] + "qu"

    print("Präsens:\t\tVergangenheit:\n" + conj[0] + "\t\t\t" + conj[3] + "\n" + conj[1] + "\t\t\t"
          + conj[4] + "\n" + conj[2] + "\t\t\t" + conj[5])


def grammar_nouns(noun):
    lemma = end_vowel(noun)  # füge d hinzu, wenn auf vokal endet
    # nominativ und dativ
    if "N1" in lex[noun][1] or "PN1" in lex[noun][1]:
        print("Nominativ: gu-" + noun + "\nDativ: " + noun + "-gūn")
    elif "N2" in lex[noun][1] or "PN2" in lex[noun][1]:
        print("Nominativ: ga-" + noun + "\nDativ: " + noun + "-gān")
    elif "N3" in lex[noun][1] or "PN3" in lex[noun][1]:
        print("Nominativ: a-" + noun + "\nDativ: " + noun + "-dān")
    # plural
    if vowel_counter(lemma) == 1 or last_vowel(lemma) in ["u", "ū", "û"]:
        print("Plural: " + lemma + "an")    # einsilbige nomen und solche die auf -u/-ū enden erhalten ein -(d)an
    elif last_vowel(lemma) in ["a", "ā", "â"]:
        print("Plural: " + lemma + "un")    # nomen die auf -a/-ā enden erhalten ein -(d)un


def grammar_pronouns(pronoun):
    print("Dativ: " + pronouns[pronoun])


def grammar_articles(article):
    print(", ".join(articles[article]))


def lexikon():
    print(hello)

    active = ""
    item = get_input("-> ").lower()  # erster input
    while not item == "tschö" and not item == "bye":  # beende mit befehl 'tschö' oder 'bye' die schleife (das programm)
        # füge special character ein
        item = item.replace("a|", "ā").replace("u|", "ū").replace("d|", "ð").replace("p|", "ƥ")

        if item not in operator:  # resete input nicht bei bestimmten meta befehlen
            active = item
        if item == "":  # enter wird nicht gesucht, sondern übersprungen
            pass
        elif item == "info":  # zeige mehr befehle
            print(info)
        elif item == "infoling":    # zeige restliche befehle
            print(info_ling)
        elif item == "all":  # zeige ganzes lexikon an
            print(lex)
        elif "words" in item:  # zeige (x) einträge in rux
            active = print_words(item)
        elif item == "trans":
            print_trans(active)
        elif item == "active":
            print(active)
        elif item == "syn":
            active = swap(active)
            print_syns(active)
        elif item == "len":
            print(str(len(lex)) + " Einträge!")
        elif "verbs" in item or "nouns" in item or "adj" in item:  # printe liste mit x einträgen von wortklasse
            print_class(item)
        elif "random" in item:  # zeige x zufällige worte an ([v]erbs,[a]djectives,[n]ouns)
            active = random_entry(item)
        elif item == "empty":  # zeige alle wörter an, die noch keine übersetzung haben
            print_empty()
        elif item == "notlist":
            print_empty("unassigned")
        elif item == "give d":  # um special character zu bekommen:
            print("ð")
        elif item == "vowels":
            print("û, â, ū, ā")
        elif item == "abc":
            print("ð ā n d r u g ƥ k a l x ū q")
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
        elif item in ["root", "rootb"]:
            active = swap(active)
            if item[-1] == "b":  # 'rootb' bearbeitet den wurzeleintrag
                edit_root(active)
            else:  # 'root' zeigt die wurzel an
                print_related(item, active)
        elif item in ["rel", "relb"]:
            active = swap(active)
            if item[-1] == "b":  # 'relb' bearbeitet verwandte wörter
                edit_rel(active)
            else:  # 'rel' zeigt verwandte wörter an
                print_related(item, active)
        elif item in ["derv", "dervb"]:
            active = swap(active)
            if item[-1] == "b":  # 'dervb' bearbeitet abgeleitete wörter
                edit_derv(active)
            else:  # 'derv' zeigt abgeleitete wörter an
                print_related(item, active)
        elif item == "add":
            insert_notlist(active)
        elif item == "save":
            save()
        else:  # wenn wort noch nicht vorhanden oder ohne übersetzung ist
            checkerito(item)

        item = get_input("-> ").lower()  # neuer input

    if item == "bye":
        print("Goodbye sir!")
    else:
        print("Tschüss!")


if __name__ == '__main__':
    lexikon()
