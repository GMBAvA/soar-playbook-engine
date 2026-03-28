import re


def extract_iocs(text: str) -> dict:
    """Extract IPs, URLs and MD5 hashes from a text string."""
    ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
    url_pattern = r"https?://[^\s]+"
    hash_pattern = r"\b[a-fA-F0-9]{32}\b"

    return {
        "ips": re.findall(ip_pattern, text),
        "urls": re.findall(url_pattern, text),
        "hashes": re.findall(hash_pattern, text),
    }


def calculate_risk_score(ioc_data: dict) -> float:
    """Calculate a risk score based on IOC data."""
    score = 0.0
    score += len(ioc_data.get("ips", [])) * 10
    score += len(ioc_data.get("urls", [])) * 20
    score += len(ioc_data.get("hashes", [])) * 30
    return min(score, 100.0)


def normalize_alert(raw_alert: dict) -> dict:
    """Normalize a raw alert into a standard format."""
    return {
        "id": raw_alert.get("id", "unknown"),
        "type": raw_alert.get("type", "unknown"),
        "severity": raw_alert.get("severity", "low").upper(),
        "source": raw_alert.get("source", "unknown"),
        "description": raw_alert.get("description", ""),
    }
