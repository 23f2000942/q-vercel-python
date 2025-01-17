import json
from http.server import BaseHTTPRequestHandler

# Mock data
marks_json = [{"name": "Alice", "marks": 90}, {"name": "Bob", "marks": 80}, {"name": "Charlie", "marks": 85}]

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse the query parameters
        query_params = self.parse_query_params()
        names = query_params.get('name', [])
        
        # Fetch marks for the provided names
        marks = [self.get_marks(name) for name in names]
        
        # Send the response
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = {"marks": marks}
        self.wfile.write(json.dumps(response).encode('utf-8'))

    def parse_query_params(self):
        """Utility method to parse query parameters."""
        query = self.path.split('?')[-1]
        params = query.split('&')
        parsed_params = {}
        
        for param in params:
            key, value = param.split('=')
            if key in parsed_params:
                parsed_params[key].append(value)
            else:
                parsed_params[key] = [value]
                
        return parsed_params

    def get_marks(self, name):
        """Helper method to get the marks for a given name."""
        for student in marks_json:
            if student['name'] == name:
                return student['marks']
        return "Not Found"
