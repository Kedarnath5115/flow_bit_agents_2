# classifier_agent.py
from memory import store_data

def classify_input(input_data):
    if isinstance(input_data, dict):
        format_type = "JSON"
        intent = input_data.get("intent", "unknown")
    elif isinstance(input_data, str) and "@example.com" in input_data:
        format_type = "Email"
        intent = "complaint" if "issue" in input_data else "inquiry"
    else:
        format_type = "PDF"
        intent = "invoice"

    store_data("format", format_type)
    store_data("intent", intent)

    return format_type, intent