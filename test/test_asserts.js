function testAssertEqual() {
    purely.assertEqual(1, 1);

    purely.assertRaisesAssertion(function() {
        purely.assertEqual(1, 2);
    });
}

function testAssertNotEqual() {
    purely.assertNotEqual(1, 2);

    purely.assertRaisesAssertion(function() {
        purely.assertNotEqual(2, 2);
    });
}


function testAssertGreater() {
    purely.assertGreater(2, 1);

    purely.assertRaisesAssertion(function() {
        purely.assertGreater(2, 2);
    });
}

function testAssertGreaterEqual() {
    purely.assertGreaterEqual(2, 1);
    purely.assertGreaterEqual(2, 2);

    purely.assertRaisesAssertion(function() {
        purely.assertGreaterEqual(1, 2);
    });
}

function testAssertLess() {
    purely.assertLess(1, 2);

    purely.assertRaisesAssertion(function() {
        purely.assertLess(2, 2);
    });
}

function testAssertLessEqual() {
    purely.assertLessEqual(1, 2);
    purely.assertLessEqual(2, 2);

    purely.assertRaisesAssertion(function() {
        purely.assertLessEqual(2, 1);
    });
}


function testAssertIn() {
    purely.assertIn(1, [1, 2]);

    purely.assertRaisesAssertion(function() {
        purely.assertIn(1, [2, 3]);
    });
}

function testAssertNotIn() {
    purely.assertNotIn(3, [1, 2]);

    purely.assertRaisesAssertion(function() {
        purely.assertNotIn(1, [1, 2]);
    });
}


function testAssertRaises() {
    purely.assertRaises("ReferenceError", function() {
        var y = x + 1;
    });
}

function testAssertRaisesAssertion() {
    purely.assertRaisesAssertion(function() {
        purely.assertEqual(1, 2);
    });
}
