// Regression tests: undefined arguments

function testAssertEqualUndefined() {
    purely.assertRaisesAssertion(function() {
        purely.assertEqual(1, undefined);
    });

    purely.assertRaisesAssertion(function() {
        purely.assertEqual(undefined, 1);
    });
}

function testAssertNotEqualUndefined() {
    purely.assertNotEqual(1, undefined);
    purely.assertNotEqual(undefined, 1);
}

function testAssertGreaterUndefined() {
    purely.assertRaisesAssertion(function() {
        purely.assertGreater(1, undefined);
    });

    purely.assertRaisesAssertion(function() {
        purely.assertGreater(undefined, 1);
    });
}

function testAssertGreaterEqualUndefined() {
    purely.assertRaisesAssertion(function() {
        purely.assertGreaterEqual(1, undefined);
    });

    purely.assertRaisesAssertion(function() {
        purely.assertGreaterEqual(undefined, 1);
    });
}

function testAssertLessUndefined() {
    purely.assertRaisesAssertion(function() {
        purely.assertLess(1, undefined);
    });

    purely.assertRaisesAssertion(function() {
        purely.assertLess(undefined, 1);
    });
}

function testAssertLessEqualUndefined() {
    purely.assertRaisesAssertion(function() {
        purely.assertLessEqual(1, undefined);
    });

    purely.assertRaisesAssertion(function() {
        purely.assertLessEqual(undefined, 1);
    });
}

function testAssertInUndefined() {
    purely.assertRaisesAssertion(function() {
        purely.assertIn(undefined, []);
    });

    purely.assertRaises("TypeError", function() {
        purely.assertIn(1, undefined);
    });
}

function testAssertNotInUndefined() {
    purely.assertNotIn(undefined, []);

    purely.assertRaises("TypeError", function() {
        purely.assertNotIn(1, undefined);
    });
}
