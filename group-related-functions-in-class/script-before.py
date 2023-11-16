api_config = {
    "api_url": "https://example.com/api",
    "api_key": "1234567890abcdef",
}

def setup_connection(api_url, api_key, user_id, session_token):
    print(f"Setting up connection to {api_url} with API key {api_key}, for user {user_id} with session {session_token}")

def fetch_data(user_id, session_token):
    setup_connection(api_config['api_url'], api_config['api_key'], user_id, session_token)
    print(f"Fetching data for user {user_id} with session {session_token}")

def process_data(user_id, session_token, data):
    setup_connection(api_config['api_url'], api_config['api_key'], user_id, session_token)
    print(f"Processing data {data} for user {user_id} with session {session_token}")

def save_data(user_id, session_token, data):
    setup_connection(api_config['api_url'], api_config['api_key'], user_id, session_token)
    print(f"Saving data {data} for user {user_id} with session {session_token}")
