ALLOWED_OPERATORS = [">", "<", "==", "!=", ">=", "<="]


def evaluate_condition(condition: str, context: dict) -> bool:
    """
    Evaluate a condition string against a context dictionary.
    Example: evaluate_condition("ioc_score > 50", {"ioc_score": 75}) → True
    """
    if not condition:
        return True

    for operator in ALLOWED_OPERATORS:
        if operator in condition:
            parts = condition.split(operator)
            key = parts[0].strip()
            value = parts[1].strip()

            if key not in context:
                return False

            context_value = context[key]

            if isinstance(context_value, bool):
                expected = value == "True"
                if operator == "==":
                    return context_value == expected
                if operator == "!=":
                    return context_value != expected

            context_value = float(context_value)
            value = float(value)

            if operator == ">":  return context_value > value
            if operator == "<":  return context_value < value
            if operator == "==": return context_value == value
            if operator == "!=": return context_value != value
            if operator == ">=": return context_value >= value
            if operator == "<=": return context_value <= value

    return False