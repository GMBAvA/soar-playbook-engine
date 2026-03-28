import argparse
from engine.parser import load_playbook
from engine.executor import execute_playbook
from engine.logger import get_logger

logger = get_logger("main")


def main():
    parser = argparse.ArgumentParser(
        description="SOAR Playbook Engine — automated incident response"
    )
    parser.add_argument("--playbook", required=True, help="Path to the YAML playbook")
    parser.add_argument("--ioc-score", type=float, default=0, help="IOC reputation score")
    parser.add_argument("--ioc-found", type=bool, default=False, help="Was an IOC found?")
    args = parser.parse_args()

    context = {
        "ioc_score": args.ioc_score,
        "ioc_found": args.ioc_found,
        "hash_found": True,
        "vt_score": args.ioc_score,
        "host_isolated": True,
        "ioc_valid": True,
        "reputation_score": args.ioc_score,
        "duplicate": False
    }

    playbook = load_playbook(args.playbook)
    results = execute_playbook(playbook, context)

    print("\n── Execution Report ──────────────────────")
    for r in results:
        icon = "✅" if r["status"] == "executed" else "⏭️ "
        print(f"{icon}  {r['step_id']} | {r['action']} | {r['status']}")
    print("──────────────────────────────────────────\n")


if __name__ == "__main__":
    main()