from engine.decision_tree import evaluate_condition
from engine.logger import get_logger

logger = get_logger(__name__)


def execute_playbook(playbook: dict, context: dict) -> list:
    """
    Execute a playbook against a given context.
    Returns a list of results for each step.
    """
    logger.info(f"Starting playbook: {playbook['name']}")
    results = []

    for step in playbook["steps"]:
        condition = step.get("condition", "")
        should_execute = evaluate_condition(condition, context)

        if should_execute:
            status = "executed"
        else:
            status = "skipped"

        logger.info(f"Step {step['id']} → {status}")

        results.append(
            {
                "step_id": step["id"],
                "action": step["action"],
                "status": status,
                "condition": condition or "none",
            }
        )

    logger.info(
        f"Playbook {playbook['name']} completed — {len(results)} steps processed"
    )
    return results
