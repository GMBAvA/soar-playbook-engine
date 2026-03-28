import yaml

def load_playbook(file_path: str) -> dict:
    """Load a YAML playbook from the specified file path."""
    with open(file_path, 'r') as file:
        playbook = yaml.safe_load(file)
    return playbook