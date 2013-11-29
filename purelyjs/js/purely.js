var purely = {
    throwAssertionError: function(msg) {
        // throws TypeError as there isn't a built-in assertion error type
        throw TypeError('AssertionError: ' + msg);

        /*
            // Safer alternative?
            throw {
                name: 'TypeError',
                message: 'AssertionError: ' + x.toString() + ' === ' + y.toString()
            };
        */
    },

    contains: function(item, arr) {
        var found = false;

        for (var i = 0; i < arr.length; i++) {
            if (arr[i] == item) {
                found = true;
                break;
            }
        }

        return found;
    },


    assertEqual: function(x, y) {
        if (!(x === y)) {
            purely.throwAssertionError(x.toString() + ' === ' + y.toString());
        }
    },

    assertNotEqual: function(x, y) {
        if (!(x !== y)) {
            purely.throwAssertionError(x.toString() + ' !== ' + y.toString());
        }
    },


    assertGreater: function(x, y) {
        if (!(x > y)) {
            purely.throwAssertionError(x.toString() + ' > ' + y.toString());
        }
    },

    assertGreaterEqual: function(x, y) {
        if (!(x >= y)) {
            purely.throwAssertionError(x.toString() + ' >= ' + y.toString());
        }
    },

    assertLess: function(x, y) {
        if (!(x < y)) {
            purely.throwAssertionError(x.toString() + ' < ' + y.toString());
        }
    },

    assertLessEqual: function(x, y) {
        if (!(x <= y)) {
            purely.throwAssertionError(x.toString() + ' <= ' + y.toString());
        }
    },


    assertIn: function(item, arr) {
        var found = purely.contains(item, arr);

        if (!found) {
            purely.throwAssertionError(item.toString() + ' not in ' + arr.toString());
        }
    },

    assertNotIn: function(item, arr) {
        var found = purely.contains(item, arr);

        if (found) {
            purely.throwAssertionError(item.toString() + ' in ' + arr.toString());
        }
    }
}
