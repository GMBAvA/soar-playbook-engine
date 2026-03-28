from engine.parser import load_playbook


def test_load_playbook_is_callable():
    assert callable(load_playbook)


def test_load_phishing_playbook():
    playbook = load_playbook("playbooks/phishing.yaml")
    assert playbook["name"] == "phishing_response"
    assert "steps" in playbook
    assert len(playbook["steps"]) == 4


def test_playbook_steps_have_required_fields():
    playbook = load_playbook("playbooks/phishing.yaml")
    for step in playbook["steps"]:
        assert "id" in step
        assert "action" in step