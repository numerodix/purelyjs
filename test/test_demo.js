function testEqual() {
    purely.assertEqual(1, 1);
}

function testNotEqual() {
    purely.assertNotEqual(1, 2);
}


function testGreater() {
    purely.assertGreater(2, 1);
}

function testGreaterEqual() {
    purely.assertGreaterEqual(2, 1);
    purely.assertGreaterEqual(2, 2);
}

function testLess() {
    purely.assertLess(1, 2);
}

function testLessEqual() {
    purely.assertLessEqual(1, 2);
    purely.assertLessEqual(2, 2);
}


function testIn() {
    purely.assertIn(1, [1, 2]);
}

function testNotIn() {
    purely.assertNotIn(3, [1, 2]);
}


function testRaises() {
    purely.assertRaises("ReferenceError", function() {
        x + 1;
    });
}
