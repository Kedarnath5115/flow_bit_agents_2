# json_agent.py
def process_json(json_data):
    required_fields = ["id", "intent", "amount"]
    missing = [field for field in required_fields if field not in json_data]
    if missing:
        return {"status": "error", "missing_fields": missing}
    
    # Reformat or extract
    return {"status": "success", "data": json_data}