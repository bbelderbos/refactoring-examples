class ApiClient:

    def __init__(self, config, user_id, session_token):
        self.api_url = config['api_url']
        self.api_key = config['api_key']
        self.user_id = user_id
        self.session_token = session_token
        self._setup_connection()

    def _setup_connection(self):
        print(f"Setting up connection to {self.api_url} with API key {self.api_key}, for user {self.user_id} with session {self.session_token}")

    def fetch_data(self):
        print(f"Fetching data for user {self.user_id} with session {self.session_token}")

    def process_data(self, data):
        print(f"Processing data {data} for user {self.user_id} with session {self.session_token}")

    def save_data(self, data):
        print(f"Saving data {data} for user {self.user_id} with session {self.session_token}")

api_config = {
    "api_url": "https://example.com/api",
    "api_key": "1234567890abcdef",
}
client = ApiClient(api_config, 123, "abc")
client.fetch_data()
client.process_data("some data")
client.save_data("some other data")
