# email_agent.py
from email_validator import validate_email, EmailNotValidError

def process_email(email_text):
    sender = "unknown@example.com"
    urgency = "low"
    intent = "unknown"

    if "urgent" in email_text.lower():
        urgency = "high"
    if "invoice" in email_text.lower():
        intent = "invoice"

    return {"sender": sender, "intent": intent, "urgency": urgency}