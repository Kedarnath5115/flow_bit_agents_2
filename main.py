# main.py
import json
from pdf_agent import process_pdf
from classifier_agent import classify_input
from json_agent import process_json
from email_agent import process_email
from memory import shared_memory

def run_agent(input_data):
    format_type, intent = classify_input(input_data)
    
    print(f"\n[Classifier Agent] Format: {format_type}, Intent: {intent}")

    if format_type == "JSON":
        result = process_json(input_data)
        print(f"[JSON Agent] Result: {result}")

    elif format_type == "Email":
        result = process_email(input_data)
        print(f"[Email Agent] Result: {result}")

    elif format_type == "PDF":
        result = process_pdf(input_data)
        print(f"[PDF Agent] Result: {result}")

    else:
        print(f"[Error] Unsupported input type: {format_type}")

    print(f"[Shared Memory] {shared_memory}")

# Sample JSON
sample_json = {
    "id": 123,
    "intent": "invoice",
    "amount": 1000
}

# Sample Email
sample_email = "Hello, I have an issue with the invoice. Please fix it urgently. Regards, user@example.com"

# Run tests
run_agent(sample_json)
run_agent(sample_email)
run_agent("file.pdf")
