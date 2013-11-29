function throwAssertionError(msg) {
    // throws TypeError as there isn't a built-in assertion error type
    throw TypeError('AssertionError: ' + msg);

    /*
        // Safer alternative?
        throw {
            name: 'TypeError',
            message: 'AssertionError: ' + x.toString() + ' === ' + y.toString()
        };
    */
};

function contains(item, arr) {
    var found = false;

    for (var i = 0; i < arr.length; i++) {
        if (arr[i] == item) {
            found = true;
            break;
        }
    }

    return found;
}


function assertEqual(x, y) {
    if (!(x === y)) {
        throwAssertionError(x.toString() + ' === ' + y.toString());
    }
}

function assertNotEqual(x, y) {
    if (!(x !== y)) {
        throwAssertionError(x.toString() + ' !== ' + y.toString());
    }
}


function assertGreater(x, y) {
    if (!(x > y)) {
        throwAssertionError(x.toString() + ' > ' + y.toString());
    }
}

function assertGreaterEqual(x, y) {
    if (!(x >= y)) {
        throwAssertionError(x.toString() + ' >= ' + y.toString());
    }
}

function assertLess(x, y) {
    if (!(x < y)) {
        throwAssertionError(x.toString() + ' < ' + y.toString());
    }
}

function assertLessEqual(x, y) {
    if (!(x <= y)) {
        throwAssertionError(x.toString() + ' <= ' + y.toString());
    }
}


function assertIn(item, arr) {
    var found = contains(item, arr);

    if (!found) {
        throwAssertionError(item.toString() + ' not in ' + arr.toString());
    }
}

function assertNotIn(item, arr) {
    var found = contains(item, arr);

    if (found) {
        throwAssertionError(item.toString() + ' in ' + arr.toString());
    }
}
