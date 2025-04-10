import random
from time import sleep

languages = ["rux", "mys"]  # available languages
#language selection
lang = input("Sprachwahl (rux, mys): ")
while not lang in languages:
    lang = input("Sprachwahl (rux, mys): ")
meta_dict = {"Einträge": "Eintrag"}

# Rux meta
rux_abc = "ð ā n d r u g ƥ k a l x ū q"
rux_vowels = ["a", "u", "ū", "ā", "û", "â"]
rux_consonants = ["x", "g", "q", "l", "r", "n", "ð", "d", "k", "ƥ"]
rux_alphabet = ["a", "u", "ū", "ā", "û", "â", "x", "g", "q", "l", "r", "n", "ð", "d", "k", "ƥ"]
rux_ipa = {"ð":"θ","ā":"ʕɐ","n":"n","d":"d","r":"r","u":"u","û":"u","g":"g","ƥ":"ɸ","k":"k","a":"ɐ","â": "ɐ",
               "l":"l","x":"ħ","ū":"ʕu","q":"q"}
rux_pronouns = {"kā": "gā", "la": "gal", "rā": "gār", "kān": "gān", "lan": "gan", "rān": "grān"}
rux_articles = {
    "gu-": ["ugu-", "gul-", "ugul-", "gur-", "āgur-"], "ga-": ["uga-", "gāl-", "gūl-", "gar-", "gār-"],
    "a-": ["ā-", "āl-", "ūl-", "ra-", "ār-"]
}
rux_POS = {
    "V": "Verb", "N1": "Nomen (Klasse 1)", "N2": "Nomen (Klasse 2)", "N3": "Nomen (Klasse 3)",
    "PN1": "Eigenname (Klasse 1)", "PN2": "Eigenname (Klasse 2)", "PN3": "Eigenname (Klasse 3)",
    "ADJ": "Adjektiv", "DET1": "Artikel (Klasse 1)", "DET2": "Artikel (Klasse 2)", "DET3": "Artikel (Klasse 3)",
    "PREP": "Präposition", "TMP": "Temporaladverb", "KNJ": "Konjunktion", "NON": "Negation", "DIM": "Diminutiv",
    "PRO": "Pronomen", "JA": "Ja", "NO": "Nein", "ZAHL": "Zahl"
}
rux_POS_noun = ["N1", "N2", "N3", "PN1", "PN2", "PN3"]
rux_POS_det = ["DET1", "DET2", "DET3"]

# Mys meta
mys_abc = "th i n t r u j f k a l y m b o s c"
mys_vowels = ["i", "u", "a", "o", "y"]
mys_consonants = ["b", "th", "k", "j", "r", "l", "n", "m", "s", "f", "c", "t"]
# incomplete!!
mys_ipa = {"a":"a","b":"b","c":"sʷ","f":"f","i":"i","j":"ʒ","k":"k","l":"l","m":"m","n":"n","o":"ɔ","r":"ɾ","s":"s"}
mys_POS = {
    "V": "Verb", "N": "Nomen","PN": "Eigenname","ADJ": "Adjektiv", "DET": "Artikel","PREP": "Präposition",
    "TMP": "Temporaladverb", "KNJ": "Konjunktion", "NON": "Negation", "DIM": "Diminutiv",
    "PRO": "Pronomen", "JA": "Ja", "NO": "Nein", "ZAHL": "Zahl"
}

hello = "Moin!\n'words' = Einträge mit Übersetzung\n'random' = zufälliges Wort\n'save' = speichern" \
        "\n'tschö' = beenden OHNE speichern\n'b' = bearbeiten\n'del' = löschen\n'g' = Grammatik\n'info' = Info"
info = "Befehle:\n'all' = Ganzes Lexikon\n'len' = Anzahl Einträge\n'active' = Zeige aktuelles Wort an" \
       "\n'empty' = Zeige alle Einträge ohne Übersetzung an" \
       "\n'random[v/n/a][zahl]' = (Anzahl) zufällige Worte [Verb/Nomen/Adjektiv] (Keine Angabe = 1)" \
       "\n'[str]words[zahl]' = Zeige [zahl] Wörter beginnend mit 'str' mit Übersetzung (Keine Angabe = 10, 0 = alle)" \
       "\n'verbs[zahl]' = Zeige [zahl] an Verben (Keine Angabe = 10, 0 = alle)" \
       "\n'nouns[zahl]' = Zeige [zahl] an Nomen (Keine Angabe = 10, 0 = alle)" \
       "\n'adjs[zahl]' = Zeige [zahl] an Adjektiven (Keine Angabe = 10, 0 = alle)" \
       "\n'save' = Speichern\n'tschö' = Beenden OHNE speichern\n'give d' = get d" \
       "\n'vowels' = print special vowels\n'abc' = ganzes Alphabet" \
       "\n'meta['vowels']' = paar zahlen [û und â aufgeführt]" \
       "\na|/u|/d|/p| = ā/ū/ð/ƥ\n+'infolab' = lab info\n+'infoling' = more info"
info_ling = "Weitere Befehle:\n'b' = Bearbeite den letztgesuchten Eintrag\n'del' = Lösche den letztgesuchten Eintrag" \
            "\n'g' = Bilde grammatikalische Formen des letztgesuchten Eintrags" \
            "\n'pos' = Zeige POS-Tag des letztgesuchten Eintrags" \
            "\n'trans' = Zeige Übersetzung(en)\n'syn' = Zeige Synonyme an" \
            "\n'root[b/n]' = Zeige Wurzel(n) des Wortes [bearbeiten/ersetzen]" \
            "\n'rel[b/n]' = Zeige verwandte Wörter [bearbeiten/ersetzen]" \
            "\n'der[b/n]' = Zeige abgeleitete Wörter [bearbeiten/ersetzen]" \
            "\n'generate[zahl]' = Generiere neue Worte aus dem Alphabet (keine Angabe = 10)" \
            "\na|/u|/d|/p| = ā/ū/ð/ƥ\n+'infolab' = lab info\n-'info' = Info"
info_lab = "Befehle für Label:\n'lablist' = Zeige alle Labels an" \
            "\n'lab[b/n]' = Zeige Label des Wortes [bearbeiten/ersetzen]" \
            "\n'find[lab]' = Finde alle Wörter mit Label lab\n'neulab' = Füge neues Label hinzu"
operator = ["b", "g", "pos", "posb", "posn", "root", "rel", "derv", "rootb", "relb", "dervb", "rootn", "reln", "dervn",
            "del", "trans", "active", "syn", "info", "infoling", "infolab", "save", "meta",
            "generate", "lab", "labb", "labn", "lablist", "lang", "phon", "derive"]
exceptions = {"ûdar": ["V", ["ûda", "ûdu", "ûdad"], ["udā", "udū", "ûdud"]]}

# sprachauswahl, default == rux
if lang == "mys":
    filename = "mys_lex.txt"
else:
    filename = "rux_lex.txt"
# öffne entsprechendes lexikon aus textdatei
lex_file = open(filename, "r", encoding="utf-8")
lex_cont = lex_file.readline()
lab_list = lex_file.readline()[:-1].split("\\")   # erstelle liste von labeleinträgen
lex_list = lex_cont[:-2].split("\\")  # split aber ignoriere letzten backslash und \n (sonst gibts nen leeren eintrag)
lex = {}
for x in lex_list:  # erstelle dict
    (key, val, pos, his, lab) = x.split(":")  # trenne eintrag und bedeutungen (+pos tag und verwandte wörter)
    (root, rel, der) = his.split(">")  # trenne verwandte wörter in wurzel und ableitungen
    # erstelle liste von allen bedeutungen (wort: ([bedeutungen], [pos], [[wurzel], [verwandt], [ableitungen]], [labels])
    lex[key] = val.split(","), pos.split(","), [root.split(","), rel.split(","), der.split(",")], lab.split(",")
label = {}
for x in lab_list:   # erstelle dict mit labels: erklärungen
    (key, val) = x.split(":")
    label[key] = val
lex_file.close()

if lang == "rux":
    verbs = [word for word in lex if "V" in lex[word][1]]  # erstelle liste aller verben
    # erstelle liste aller nomen (inkl eigennamen)
    nouns = [word for word in lex if any(item in lex[word][1] for item in rux_POS_noun)]
    adjs = [word for word in lex if "ADJ" in lex[word][1]]  # erstelle liste aller adjektive
else:
    verbs = [word for word in lex if "V" in lex[word][1]]  # erstelle liste aller verben
    # erstelle liste aller nome (inkl eigennamen)
    nouns = [word for word in lex if any(item in lex[word][1] for item in ["N", "PN"])]
    adjs = [word for word in lex if "ADJ" in lex[word][1]]  # erstelle liste aller adjektive


def check_lang():
    if lang == "rux":
        print("Aktive Sprache: Rux")
    elif lang == "mys":
        print("Aktive Sprache: Myzari")
    else:
        print("Keine Sprache ausgewählt")


# save lex to file
def save():
    if lang == "rux":
        output_file = "rux_lex.txt"
    elif lang == "mys":
        output_file = "mys_lex.txt"
    else:
        output_file = "unknown_lex.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        for entry in lex:
            f.write(
                entry + ":" + ",".join(lex[entry][0]) + ":" + ",".join(lex[entry][1]) + ":" + ",".join(lex[entry][2][0])
                + ">" + ",".join(lex[entry][2][1]) + ">" + ",".join(lex[entry][2][2]) + ":"
                + ",".join(lex[entry][3]) + "\\")
        f.write("\n")
        for entry in label:
            f.write(entry + ":" + label[entry] + "\\")
    print("Lexikon gesichert:")
    print(str(len(lex)) + " Einträge")


# write contents to file for js use
def extract():
    rux_grammar = {}
    with open("rux_lex_corpus.txt", "w", encoding="utf-8") as f:
        f.write("const lex = {\n")
        for entry in lex:
            tag = pos(entry)
            if any(w in ["N1", "N2", "N3"] for w in lex[entry][1]):
                tag = ["Nomen"]
            elif any(w in ["PN1", "PN2", "PN3"] for w in lex[entry][1]):
                tag = ["Eigenname"]
            elif any(w in ["DET1", "DET2", "DET3"] for w in lex[entry][1]):
                tag = ["Artikel"]
            elif not tag:
                tag = ['']

            trans = []
            if not lex[entry][0] == [""]:
                trans = lex[entry][0]

            f.write(f'"{entry}": [{trans}, {tag}, '
                    f'[{lex[entry][2][0]}, {lex[entry][2][1]}, {lex[entry][2][2]}]], \n')

            gram, _ = grammar(entry)
            rux_grammar[entry] = gram
        f.write("}\n")
        print("lex extracted")

    with open("rux_lex_grammar.txt", "w", encoding="utf-8") as gram_f:
        gram_f.write("const gram = {\n")
        for entry in rux_grammar:
            gram = []
            if entry == "ûdar":
                gram = ['ud', 'ûdan', 'ûda', 'ûdu', 'ûdad', 'udā', 'udū', 'ûdud']
            elif len(rux_grammar[entry]) > 3:
                gram = rux_grammar[entry]
            gram_f.write(f'"{entry}": {gram}, \n')
        gram_f.write("}\n")
        print("grammar extracted")


# #HELPER FUNCTIONS
def get_input(prompt, form=""):
    if not form:
        item = input(prompt)
    else:
        item = input(prompt).replace(" ", "").replace("_", " ").replace("a|", "ā") \
            .replace("u|", "ū").replace("d|", "ð").replace("p|", "ƥ").split(",")

    return item


# entferne special vowels
def purify(word):
    return word.replace("ā", "a").replace("â", "a").replace("ū", "u").replace("û", "u")


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


# extrahiere label aus input "findxxx"
def separate_label(ipt):
    if ipt[-3:].upper() in label:
        lab = ipt[-3:].upper()
    else:
        lab = ""

    return lab


def vowel_counter(string):
    count = 0
    if lang == "rux":
        vowels = rux_vowels
    elif lang == "mys":
        vowels = mys_vowels
    else:
        vowels = ["a", "e", "i", "o", "u"]

    for letter in string:
        if letter in vowels:
            count += 1
    return count


# get last vowel oder gleiche mit check ab
def last_vowel(string, check=""):
    if lang == "rux":
        vowels = rux_vowels
    elif lang == "mys":
        vowels = mys_vowels
    else:
        vowels = ["a", "e", "i", "o", "u"]

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
    if lang == "rux":
        vowels = rux_vowels
    elif lang == "mys":
        vowels = mys_vowels
    else:
        vowels = ["a", "e", "i", "o", "u"]

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
    if lang == "rux":
        noun_pos = rux_POS_noun
    elif lang == "mys":
        noun_pos = ["N"]
    for tag in postag:
        if tag.upper() == "ADJ":
            adjs.append(word)
        elif tag.upper() in noun_pos:
            nouns.append(word)
        elif tag.upper() == "V":
            verbs.append(word)


# finde singular (z.B. Eintrag/Einträge)
def singulizer(word, num):
    if word in meta_dict and num == 1:
        return meta_dict[word]
    return word


# #PRINTERS
def print_entry(word):  # printe eintrag aus lex
    for entry in lex:
        if word == entry or word in (trans.lower() for trans in
                                     lex[entry][0]):  # item in eintrag oder in liste_bedeutungen (caseinsensitive)
            print(f"Folgenden Eintrag gefunden:\n{entry}: " + ", ".join(lex[entry][0]))


def print_empty(inpt):
    (liste, scope) = separator(inpt)
    if scope == 0:  # wird eine 0 angegeben, wird scope auf standard gesetzt (alle einträge)
        scope = -1

    if liste == "empty":  # worte ohne übersetzung
        cont = search_empty(scope)
    else:
        print("Inkorrekte Eingabe")
        return

    if not cont or cont == [""]:
        print("Keine Worte vorhanden")
    else:
        print("\n".join(cont))
        print(f"{len(cont)} {singulizer('Einträge', len(cont))} gefunden")


def print_lab_list():
    lab_list = [lab + ": " + label[lab] for lab in label]
    if lab_list:
        print('\n'.join(lab_list))
    else:
        print("Keine Labels gefunden")


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
        print(f"Insgesamt {len(verbs)} Verben gefunden")
    elif "nouns" in klasse:
        if scope == 0:  # scope = 0 -> alle nomen
            scope = len(nouns)
        # printe die letzten x nomen, x = scope
        if klasse == "transnouns":  # printe mit übersetzung
            print("\n".join([n + ": " + ", ".join(lex[n][0]) for n in nouns[-scope:]]))
        else:
            print("\n".join(nouns[-scope:]))
        print(f"Insgesamt {len(nouns)} Nomen gefunden")
    elif "adjs" in klasse:
        if scope == 0:  # scope = 0 -> alle adjektive
            scope = len(adjs)
        # printe die letzten x adjektive, x = scope
        if klasse == "transadjs":  # printe mit übersetzung
            print("\n".join([a + ": " + ", ".join(lex[a][0]) for a in adjs[-scope:]]))
        else:
            print("\n".join(adjs[-scope:]))
        print(f"Insgesamt {len(adjs)} Adjektive gefunden")
    else:
        print("Inkorrekte Eingabe")


def print_words(item):
    inpt, scope = separator(item)  # trenne input ('words') von gewünschter anzahl (scope)
    if scope > len(lex) or scope == 0:  # scope = 0 -> alle wörter; und catche ob input > len um errors zu vermeiden
        scope = len(lex)
    elif scope == -1:  # wenn kein wert angegeben
        scope = 10  # standardwert 10

    if inpt.startswith("words"):
        # erstelle liste aus x (=scope) einträgen + übersetzungen ['w1: t1, t2', 'w2: t1', ...]
        ret = [wort + ": " + ", ".join(lex[wort][0]) for wort in list(lex)[0:scope]]
        print("\n".join(ret))
        # parse letztes wort als 'active'
        return list(lex)[scope - 1]
    else:
        # extracte gewünschte anfangsbuchstaben/string ("awords" -> anfang = "a"; "guwords" -> anfang = "gu")
        anfang = inpt.partition("words")[0]
        if anfang:
            ret = [wort + ": " + ", ".join(lex[wort][0]) for wort in list(lex) if wort.startswith(anfang)]
            if not ret:
                print(f"Keine Worte gefunden, die mit '{anfang}' beginnen")
            else:
                print("\n".join(ret[0:scope]))
                print(f"Insgesamt {len(ret)} Worte gefunden")


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
        print(f"{word}: {{" + ", ".join(syn) + "}")
    else:
        print("Keine Synonyme gefunden")


def print_pos(word):
    tags = pos(word)
    if tags:
        print("/".join(tags))
    else:
        print("Keinen POS-Tag gefunden")


# print phonemic representation
def print_phon(word):
    if lang == "rux":
        phon = phonemizer(word)
        ipa = "/" + phon + "/"
        print(ipa)
    else:
        print("Keine phonemische Representation möglich")

def print_lab(word):
    if word in lex and not lex[word][3] == [""]:
        print("Label: {" + ", ".join(lex[word][3]) + "}")
    else:
        print("Keine Label gefunden")


def print_labwords(item):
    lab, words = find_label(item)
    if words:
        print(f"Folgende Worte mit Label '{lab}' gefunden: ")
        print("\n".join(words))
    else:
        print(f"Keine Worte mit Label '{lab}' gefunden")


def print_abc():
    if lang == "rux":
        print(rux_abc)
    elif lang == "mys":
        print(mys_abc)


# wenn vowels=False werden û/â als u/a behandelt
def print_meta(vowels=False):
    lang, dictlet, dictstart = meta(vowels)
    # sortiere nach absteigender anzahl
    dictlet_sorted = sorted(dictlet.items(), key=lambda tup: tup[1], reverse=True)
    dictstart_sorted = sorted(dictstart.items(), key=lambda tup: tup[1], reverse=True)
    print("\nHäufigkeit Buchstaben:")
    for tupp in dictlet_sorted:
        print(f"{tupp[0]}: {tupp[1]}")
    print("\nHäufigkeit Anfangsbuchstaben:")
    for tupp in dictstart_sorted:
        print(f"{tupp[0]}: {tupp[1]}")
    print(f"\n{lang} Einträge insgesamt")


# #GENERATOR
cluster = ["kr", "dr"]  # zulässige cons cluster in rux


# random vokal
def random_vow(mode="all"):
    if mode == "base":
        return random.choices(["a", "u", "ū", "ā"], weights=(35, 35, 15, 15))[0]
    return random.choices(rux_vowels, weights=(35, 35, 10, 10, 5, 5))[0]


# random konsonant
def random_cons():
    return random.choices(rux_consonants, weights=(5, 7.5, 7.5, 20, 25, 15, 7.5, 20, 10, 5))[0]


# CC
def random_cluster():
    return random.choice(cluster)


def vow_check(syl):
    if syl in rux_vowels:     # wenn vow dann entweder wort = V oder wort = VC
        random.choice(["", random_cons()])   # [kein con, random con]
        return syl


# random silbe
def rand_syl():
    start = random.choices([rux_vowels, rux_consonants, cluster], weights=(45, 45, 10))[0]
    if start == rux_vowels:
        syl = random_vow() + random.choice(["", random_cons()])   # [kein con, random con]
        return syl  # Entweder V oder VC
    elif start == cluster:
        syl = random_cluster()
    else:
        syl = random_cons()

    syl += random_vow("base")
    syl += random.choices(["", random_cons()],weights=(65, 35))[0]
    return syl


# random silbe die mit einem cons beginnt
def rand_con_syl():
    # add random C or random cluster (CC)
    start = random.choices([rux_consonants, cluster], weights=(95, 5))[0]  # add random C or random cluster (CC)
    if start == cluster:
        syl = random_cluster()
    else:
        syl = random_cons()

    syl += random_vow()
    syl += random.choice(["", random_cons()])
    return syl


def generate(eingabe):
    _, anzahl = separator(eingabe)  # lese anzahl wörter aus dem input heraus
    # kein wert oder wert 0 auf Standardwert 10 setzen
    if anzahl < 1:
        anzahl = 10

    gen_words = []
    for x in range(anzahl):
        wort = rand_syl()   # wort ist mind 1 silbe lang
        # mandatory second syllable for one-letter one-vowel words
        if wort in rux_vowels:
            one_syl_weight = 0
        else:
            one_syl_weight = 30

        # füge 0-2 silben hinzu, max insg: 3 Silben
        for x in range(random.choices([0, 1, 2], weights=(one_syl_weight, 50, 20))[0]):
            # Beginne nächste Silbe mit cons, wenn letzte auf vow endet
            if wort[-1] in rux_vowels:
                wort += rand_con_syl()
            else:
                wort += rand_syl()

        gen_words.append(wort)

    print("\n".join(gen_words))

# altes generate
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
            endstring += random.choice(rux_consonants)

        while count < syllables:
            endstring += random.choice(rux_vowels)
            endstring += random.choice(rux_consonants)
            count += 1

        gen_words.append(endstring)

    print("\n".join(gen_words))


def     derive(word):
    word = swap(word)
    if lang == "rux":

        derv = ""
        ind = 0
        while ind < len(word):
            char = word[ind]
            # dr = der, gr = ger usw.
            if char in ["d","ð","g","k","ƥ", "j"] and ind+1<len(word) and word[ind+1] in ["r"]:
                char += "e"
            elif char == "d":
                # da/dâ/dā -> t'X und d am Wortende = t'
                if ind+1 == len(word) or word[ind+1] in ["a" , "â", "ā", "ū"]:
                    char = "t'"
            # n am Wortanfang = m
            elif ind == 0 and char == "n":
                char = "m"
            # ð = th außer:
            elif char == "ð":
                # ðu am Wortanfang = su und ð am Wortende = s
                if (ind == 0 and char == "ð" and word[ind+1] in ["u", "û"]) or (ind+1 == len(word) and char == "ð"):
                    char = "s"
                # ðū = ðu
                elif ind+1 < len(word) and word[ind+1] == "ū":
                    char = "ðu"
                    ind+=1
                # ðā = ðe, sonst ð = th
                elif not (ind+1 < len(word) and word[ind+1] == "ā"):
                    char = "th"
            # xk = k, x = q
            elif char == "x":
                if ind+1 < len(word) and word[ind+1] == "k":
                    char = "k"
                    ind+=1
                else:
                    char = "ö"  # Platzhalter damit q nicht am Ende durch k' ersetzt wird
            # a'ul = ul
            elif char == "a" and ind+2 < len(word) and word[ind+1:ind+2] == "'":
                char = "u"
                ind+=2
            # u'al
            elif char == "u" and ind+2 < len(word) and word[ind+1:ind+2] == "'":
                # qu'al/gu'al = k'al/jal
                if word[ind-1] in ["g", "q"]:
                    char = "a"
                    ind+=2
                # u'al = ual
                else:
                    char = "ua"
                    ind+=2
            # āk = ek'
            elif char == "ā" and ind+1 < len(word) and word[ind+1] == "k":
                char = "āk'"
                ind+=1
            # ūk = ük'
            elif char == "ū" and ind+1 < len(word) and word[ind+1] == "k":
                char = "ūk'"
                ind+=1
            # kū/kā = k'ü/k'e
            elif char == "k" and ind+1 < len(word) and word[+1] in ["ū","ā"]:
                char = "k'"
            # g = j
            elif char == "g":
                # am Wortende g = k
                if ind+1 == len(word):
                    char = "k"
                else:
                    char = "j"
            # r fällt am Wortende weg
            elif char == "r":
                if ind+1 == len(word):
                    char = ""
            derv+=char
            ind+=1
        derv = (derv.replace("q", "k'").replace("ā", "e")
                .replace("ƥ", "f").replace("ū", "ü").replace("ö","q")
                .replace("â","a").replace("û","o"))
        print(derv)
    else:
        print("Ableiten nur für rux möglich")

# LABEL
def create_lab():
    new_lab = get_input("What label shall be added?: ")
    if len(new_lab) == 3:
        new_name = get_input("What does it stand for?: ")
        label[new_lab.upper()] = new_name
        print(f"Label '{new_lab}' has been added with the meaning '{new_name}'!")
    else:
        print("Ungültige Eingabe")


def find_label(item):
    lab = separate_label(item)  # separiere das label von input "findxxx"
    words = []
    # wenn lab gefunden wurde
    print(f"Label: {lab}")
    if lab:
        # erstelle liste [eintrag: übersetzung1, übersetzung2, eintrag2 usw.] mit worten mit bestimmtem label
        words = [entry + ": " + ", ".join(lex[entry][0]) for entry in lex if lex[entry][3][0] == lab]
    return lab, words


# #DICT MANIPULATION
def insert(item):
    if lang == "rux":
        pos_list = rux_POS
    elif lang == "mys":
        pos_list = mys_POS

    if item not in lex or lex[item][0] == [""]:
        print(item)
        word = get_input("Bedeutung(en): ", "format")
        tag = get_input("POS: ").upper().split(",")
        for poz in tag:
            if poz not in pos_list:  # füge nur gültige pos tags hinzu
                tag.remove(poz)
        lex[item] = word, tag, [[""], [""], [""]], lab
        insert_poslist(tag, item)  # update verbs/nouns/adjs
    else:
        print(item)
        lex[item] = lex[item][0] + get_input("Bedeutungen: " + ", ".join(lex[item][0]) + ", ", "format"), \
            lex[item][1], lex[item][2], lex[item][3]

    print(f"Geänderter Eintrag:\n{item}: " + ", ".join(lex[item][0]) + "\n(" + "/".join(lex[item][1]) + ")")


def delete(item):
    if check_antwort():
        lex.pop(item)
        print(f"{item} wurde gelöscht")


# bearbeite die Label ('labb') oder überschreibe sie ('labn')
def add_label(item, word):
    if word in lex:
        labs = ""
        if lex[word][3] == [""] or lex[word][3] == []:
            print(f"Kein Label gefunden ({word})")
            labs = get_input("new label: ", "format")
        elif item == "labb":
            print(f"Label darf kein 'x' enthalten")
            print(f"Label von {word}: " + ", ".join([f"{lab} ({label[lab]})" for lab in lex[word][3]]))
            ###fehler
            labs = lex[word][3][0] + get_input("added label(s): ", "format")
        elif item == "labn":
            print(f"Label von {word}: " + ", ".join([f"{lab} ({label[lab]}" for lab in lex[word][3]]))
            print("Vorsicht! Eintrag wird überschrieben. 'x' zum abbrechen")
            labs = get_input("new label(s): ", "format")
            if "x" in labs:
                return
        if labs:
            lex[word] = lex[word][0], lex[word][1], lex[word][2], [t.upper() for t in labs if t.upper() in label]
            print("Label(s): " + "/".join(lex[word][3]))
    else:
        print("Eintrag konnte nicht gefunden werden")


# bearbeite den POS Eintrag ('posb') oder überschreibe ihn ('posn')
def add_pos(item, word):
    if lang == "rux":
        pos = rux_POS
    elif lang == "mys":
        pos = mys_POS

    if word in lex:
        ptags = ""
        if lex[word][1] == [""]:
            print(f"Keinen POS Tag gefunden ({word})")
            ptags = get_input("new POS: ", "format")
        elif item == "posb":
            print(f"POS von {word}: " + ", ".join([f"{ptag} ({pos[ptag]})" for ptag in lex[word][1]]))
            ptags = lex[word][1] + get_input("added POS: ", "format")
        elif item == "posn":
            print(f"POS von {word}: " + ", ".join([f"{ptag} ({pos[ptag]}" for ptag in lex[word][1]]))
            print("Vorsicht! Eintrag wird überschrieben. 'x' zum abbrechen")
            ptags = get_input("new POS: ", "format")
            if "x" in ptags:
                return
        if ptags:
            lex[word] = lex[word][0], [t.upper() for t in ptags if t.upper() in pos], lex[word][2], lex[word][3]
            print("POS Tag(s): " + "/".join(lex[word][1]))
    else:
        print("Eintrag konnte nicht gefunden werden")


def edit_root(item, word):
    if word in lex:
        if lex[word][2][0] == [""]:  # wenn liste leer
            print(f"Keine Wurzel gefunden ({word})")
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
        print(f"{count} {singulizer('Einträge', count)} geändert")
    else:
        print("Kein Eintrag vorhanden")


def add_root(item, word):
    print(f"root of {word}: " + ", ".join(lex[word][2][0]))
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
            print(f"Keine verwandten Wörter ({word})")
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
        print(f"{count} {singulizer('Einträge', count)} geändert")
    else:
        print("Kein Eintrag vorhanden")


def add_rel(item, word):
    print(f"Verwandte Wörter von '{word}': {lex[word][2][1]}")
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
            print(f"Keine abgeleiteten Wörter ({word})")
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
        print(f"{count} {singulizer('Einträge', count)} geändert")
    else:
        print("Kein Eintrag gefunden")


def add_derv(item, word):
    print(f"Abgeleitete Wörter von '{word}': {lex[word][2][2]}")
    if item == "dervb":
        # füge abgeleitete worte hinzu, die noch nicht vorhanden sind
        lex[word][2][2] += [neu for neu in get_input("added word(s): ", "format") if neu not in lex[word][2][2]]
    elif item == "dervn":
        inpt = get_input("Vorsicht! Eintrag wird überschrieben.\nSchreibe 'x' um abzubrechen\nnew word(s): ", "format")
        if 'x' not in inpt:
            # ersetze abgeleitete wörter
            lex[word][2][2] = inpt


# #GET INFO
def checkerito(item):
    if check_lex(item):
        print_entry(item)
    else:
        print("Nischt jefunden!")


# finde anzahl {scope} worte in lex, die noch keine übersetzung haben
def search_empty(scope):
    lex_notrans = []
    for entry in lex:
        if lex[entry][0] == [""]:  # finde einträge ohne übersetzung: wenn "liste übersetzungen" leer ist
            lex_notrans.append(entry)
        if len(lex_notrans) == scope:   # wenn scope erreicht, beende loop
            break

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
    if lang == "rux":
        pos_list = rux_POS
    elif lang == "mys":
        pos_list = mys_POS
    else:   #default rux
        pos_list = rux_POS

    tags = []
    if word in lex and not lex[word][1] == [""]:  # wenn word und zugehörige pos tags vorhanden
        for tag in pos_list:
            if tag in lex[word][1]:
                tags.append(pos_list[tag])
    return tags


# finde synonyme
def synonyms(word):
    syn = []
    if word in lex:
        for entry in lex:
            if any(item in lex[word][0] for item in lex[entry][0]) and not word == entry:
                syn.append(entry)

    return syn


# get phonemic representation
def phonemizer(word):
    word = swap(word)
    ipa = ""
    for char in word:
        if char in rux_ipa:
            ipa += rux_ipa[char]
    return ipa

# berechne metadaten
# vowels: wenn False werden û/â wie u/a behandelt
# return anzahl einträge, dict: häufigkeit buchstaben, dict: häufigkeit anfangsbuchstaben
def meta(vowels: bool):
    letter_counter = {letter: 0 for letter in rux_alphabet}  # dict = {buchstabe: 0} für jeden buchstaben
    start_counter = {letter: 0 for letter in rux_alphabet}  # " " "
    for entry in lex:
        if entry[0] in rux_alphabet:
            start_counter[entry[0]] += 1  # zähle anfangsbuchstaben, ignoriere suffixe (starten mit "-")
        for char in entry:
            if char in rux_alphabet:
                letter_counter[char] += 1  # zähle buchstaben

    # wenn vowels=False: û = u und â = a
    if not vowels:
        letter_counter["u"] += letter_counter.pop("û")
        letter_counter["a"] += letter_counter.pop("â")
        start_counter["u"] += start_counter.pop("û")
        start_counter["a"] += start_counter.pop("â")

    return len(lex), letter_counter, start_counter


# #GRAMMAR
def print_grammar(gramlist, klasse):
    if gramlist == [] or klasse == "":
        print("Keine Grammatik verfügbar")
    elif klasse == "V":
        if gramlist[0]:
            print(f"Nominalisierung: {gramlist[0]}")
        print(f"Imperativ: {gramlist[1]}! {gramlist[2]}!\n")
        print(f"Präsens: \t\tVergangenheit: \n{gramlist[3]}\t\t\t{gramlist[6]}\n{gramlist[4]}\t\t\t"
              f"{gramlist[7]}\n{gramlist[5]}\t\t\t{gramlist[8]}")
    elif klasse == "N":
        print(f"Nominativ: {gramlist[3]} / {gramlist[1]}")
        print(f"Dativ: {gramlist[4]} / {gramlist[5]}")
        print(f"Instrumentalis: {gramlist[2]} / {gramlist[0]}")
    elif klasse == "PRO":
        print(f"Nominativ: {gramlist[0]}\nDativ: {gramlist[1]}")
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
        if "V" in lex[word][1]:
            if word == "dar":
                table = special_verb(word)
                klasse = "V"
            else:
                table = grammar_verbs(word)
                klasse = "V"
        # nomen
        elif any(item in lex[word][1] for item in rux_POS_noun):  # enthält 'liste pos' ein noun tag?
            table = grammar_nouns(word)
            klasse = "N"
        # pronomen
        elif "PRO" in lex[word][1]:
            table = [word, rux_pronouns[word]]
            klasse = "PRO"
        # artikel
        elif word in rux_articles:
            table = rux_articles[word]
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


def special_verb(verb):
    if verb == "dar":
        return ["da'ul", "dad", "dadun", "da", "du", "dad", "dā", "dū", "dud"]


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
    # kā -> qa; kū -> qu
    if ends_in(lemma) == "k":
        conj[3] = lemma[:-1] + "qa"
        conj[4] = lemma[:-1] + "qu"

    # āXū/ā -> aXū/ā
    elif last_vowel(lemma) == "ā":
        conj[3] = lemma.replace("ā", "a") + "ā"
        conj[4] = lemma.replace("ā", "a") + "ū"

    # ūXū/ā -> uXū/ā
    elif last_vowel(lemma) == "ū":
        conj[3] = lemma.replace("ū", "u") + "ā"
        conj[4] = lemma.replace("ū", "u") + "ū"
    # ûXū/ā -> uXū/ā
    elif last_vowel(lemma) == "û":
        conj[3] = lemma.replace("û", "u") + "ā"
        conj[4] = lemma.replace("û", "u") + "ū"

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

        if lang == "rux":
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
            case "infolab":
                print(info_lab) # zeige lab befehle an
            case "all":  # zeige ganzes lexikon an
                print(lex)
            case "lang":
                check_lang()
            case item if "words" in item:  # zeige (x) einträge in rux
                active = print_words(item)
            case "trans":
                print_trans(active)
            case "active":
                print(active)
            case "syn":  # zeige synonyme
                active = swap(active)
                print_syns(active)
            case "phon":    # printe phonemische darstellung
                print_phon(active)
            case "len":
                print(f"{len(lex)} Einträge!")
            case item if "verbs" in item:  # printe liste mit x einträgen von wortklasse
                print_class(item)
            case item if "nouns" in item:
                print_class(item)
            case item if "adjs" in item:
                print_class(item)
            case item if "random" in item:  # zeige x zufällige worte an ([v]erbs,[a]djectives,[n]ouns)
                active = random_entry(item)
            case item if "empty" in item:  # zeige alle wörter an, die noch keine übersetzung haben
                print_empty(item)
            case "give d":  # um special character zu bekommen:
                print("ð ƥ")
            case "vowels":
                print("û, â, ū, ā")
            case "abc":
                print_abc()
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
            case "posb" | "posn":  # bearbeite part of speech tag
                active = swap(active)
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
            case item if "lab" in item:
                active = swap(active)
                if item == "lablist":
                    print_lab_list()
                elif item == "lab":
                    print_lab(active)
                elif item == "neulab":
                    create_lab()
                else:
                    add_label(item, active)
            case item if item.startswith("find"):
                print_labwords(item)
            case "save":
                save()
            case "meta":
                print_meta()
            case "metavowels":
                print_meta(True)
            case item if "generate" in item:
                generate(item)
            case "derive":
                derive(active)
            case "extract":
                extract()
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
