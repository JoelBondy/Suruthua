const dict = {
    "Amaka": 112,
    "Guqual": 101,
    "Avzitil": 94,
    "Vadonier": 87,
    "Elb": 81,
    "Augling": 75,
    "Quork": 73,
    "Draske": 70
};

function getValue(id) {
    let input = Number(id.value);

    if (input > 20) {
        input = 20
        id.value = input
    }
    else if (input < 0) {
        input = 1
        id.value = input
    }

}