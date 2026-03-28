from engine.parser import load_playbook
from engine.executor import execute_playbook


def test_all_steps_executed_when_conditions_met():
    playbook = load_playbook("playbooks/phishing.yaml")
    context = {"ioc_found": True, "ioc_score": 75}
    results = execute_playbook(playbook, context)
    assert len(results) == 4


def test_step_skipped_when_condition_not_met():
    playbook = load_playbook("playbooks/phishing.yaml")
    context = {"ioc_found": True, "ioc_score": 10}
    results = execute_playbook(playbook, context)
    skipped = [r for r in results if r["status"] == "skipped"]
    assert len(skipped) >= 1


def test_result_contains_expected_fields():
    playbook = load_playbook("playbooks/phishing.yaml")
    context = {"ioc_found": True, "ioc_score": 75}
    results = execute_playbook(playbook, context)
    for result in results:
        assert "step_id" in result
        assert "action" in result
        assert "status" in result