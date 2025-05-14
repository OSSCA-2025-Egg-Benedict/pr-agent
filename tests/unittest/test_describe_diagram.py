def main():
    user = get_user()
    data = fetch_data(user)
    result = process(data)
    save_result(result)

def get_user():
    return "user_123"

def fetch_data(user_id):
    return {"value": 42}

def process(data):
    return data["value"] * 2

def save_result(result):
    print(f"Result: {result}")
