import re

def extract_key_values(body):
    """
    Extracts all key=value pairs from the message.
    Returns a dictionary.
    """
    try:
        matches = re.findall(r"(\w+)=([\w\.\-\s%]+)", body)
        return dict(matches) if matches else {}
    except Exception as e:
        print(f"Parsing error: {e}")
        return {}
