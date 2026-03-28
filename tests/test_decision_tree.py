from engine.decision_tree import evaluate_condition


def test_no_condition_returns_true():
    assert evaluate_condition("", {}) == True


def test_ioc_score_above_threshold():
    assert evaluate_condition("ioc_score > 50", {"ioc_score": 75}) == True


def test_ioc_score_below_threshold():
    assert evaluate_condition("ioc_score > 50", {"ioc_score": 30}) == False


def test_boolean_condition_true():
    assert evaluate_condition("ioc_found == True", {"ioc_found": True}) == True


def test_boolean_condition_false():
    assert evaluate_condition("ioc_found == True", {"ioc_found": False}) == False


def test_missing_key_returns_false():
    assert evaluate_condition("ioc_score > 50", {}) == False