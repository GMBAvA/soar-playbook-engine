from engine.utils import extract_iocs, calculate_risk_score, normalize_alert


def test_extract_ip():
    result = extract_iocs("Suspicious traffic from 192.168.1.1")
    assert "192.168.1.1" in result["ips"]


def test_extract_url():
    result = extract_iocs("Phishing link: https://evil.com/malware")
    assert "https://evil.com/malware" in result["urls"]


def test_extract_hash():
    result = extract_iocs("File hash: d41d8cd98f00b204e9800998ecf8427e")
    assert "d41d8cd98f00b204e9800998ecf8427e" in result["hashes"]


def test_risk_score_increases_with_iocs():
    data = {"ips": ["1.1.1.1"], "urls": ["http://evil.com"], "hashes": []}
    assert calculate_risk_score(data) == 30.0


def test_risk_score_capped_at_100():
    data = {"ips": ["1.1.1.1"] * 10, "urls": ["http://x.com"] * 10, "hashes": []}
    assert calculate_risk_score(data) == 100.0


def test_normalize_alert():
    raw = {"id": "ALT-001", "type": "phishing", "severity": "high"}
    result = normalize_alert(raw)
    assert result["severity"] == "HIGH"
    assert result["id"] == "ALT-001"