# SOAR Playbook Engine 🛡️

A lightweight Python-based SOAR (Security Orchestration, Automation and Response) engine
that executes YAML-defined playbooks for automated incident response.

Built as a personal cybersecurity project to demonstrate SOC automation skills,
Python development and software quality practices.
Powered by Claude Sonnet 4.6 Thinking

---

## Features

- **YAML Playbook Parser** — load and validate structured playbooks
- **Conditional Decision Engine** — evaluate dynamic conditions per step
- **Workflow Executor** — run playbooks step by step with skip logic
- **Structured JSON Logging** — output readable by Splunk and SIEMs
- **CLI Interface** — run any playbook directly from the terminal
- **12 Unit Tests** — full coverage with pytest

---

## Project Structure
soar-playbook-engine/
├── engine/
│ ├── parser.py # YAML playbook loader
│ ├── decision_tree.py # Condition evaluator
│ ├── executor.py # Workflow execution engine
│ └── logger.py # Structured JSON logger
├── playbooks/
│ ├── phishing.yaml
│ ├── malware.yaml
│ ├── ransomware.yaml
│ ├── threat_intel.yaml
│ └── ioc_blocking.yaml
├── tests/
│ ├── test_parser.py
│ ├── test_decision_tree.py
│ └── test_executor.py
└── main.py

text

---

## Getting Started

**1. Clone the repository**
```bash
git clone https://github.com/GMBAvA/soar-playbook-engine
cd soar-playbook-engine
```

**2. Create virtual environment**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

---

## Usage

Run any playbook with a context:

```bash
python main.py --playbook playbooks/phishing.yaml --ioc-score 75 --ioc-found True
```

Example output:
── Execution Report ──────────────────────
✅ step_1 | extract_ioc | executed
✅ step_2 | enrich_ioc | executed
✅ step_3 | block_sender | executed
✅ step_4 | notify_soc | executed
──────────────────────────────────────────

text

---

## Available Playbooks

| Playbook | Trigger | Steps |
|---|---|---|
| phishing.yaml | phishing_detected | Extract IOC → Enrich → Block → Notify |
| malware.yaml | malware_detected | Hash → VirusTotal → Quarantine → Notify |
| ransomware.yaml | ransomware_detected | Isolate → Snapshot → Escalate P1 → Notify |
| threat_intel.yaml | ioc_submitted | Normalize → Enrich → Update SIEM → Report |
| ioc_blocking.yaml | ioc_confirmed_malicious | Check duplicates → Firewall → Log → Notify |

---

## Running Tests

```bash
pytest tests/ -v
```

Expected: **12 passed**

---

## Tech Stack

- Python 3.13.12
- PyYAML
- pytest
- JSON structured logging (Splunk-compatible)

---

## Author

Alexandre Berthoumieu — Cybersecurity student
[LinkedIn](https://www.linkedin.com/in/aberthoumieu/)