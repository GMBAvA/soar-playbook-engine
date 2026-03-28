from engine.parser import load_playbook

def test_load_playbook_is_callable():
    assert callable(load_playbook)