import json
from http.server import BaseHTTPRequestHandler

# Sample marks data
marks_json=[{"name":"LUrtFZcK9U","marks":18},{"name":"P","marks":92},{"name":"9m2VB6k","marks":80},{"name":"Wd","marks":68},{"name":"bLh","marks":25},{"name":"d","marks":79},{"name":"yw","marks":83},{"name":"onI37pi73","marks":85},{"name":"AC5k","marks":11},{"name":"Q","marks":55},{"name":"RFQ9xQsS","marks":87},{"name":"un","marks":81},{"name":"eJvK5","marks":33},{"name":"sJImV5HKqG","marks":16},{"name":"qzKTuD4hUg","marks":4},{"name":"VSO4","marks":69},{"name":"KgFMZ8E","marks":22},{"name":"xHBA","marks":48},{"name":"vDK","marks":48},{"name":"L","marks":42},{"name":"Ed6SLou","marks":45},{"name":"Hnn","marks":75},{"name":"reISJD","marks":96},{"name":"mASiUL5","marks":48},{"name":"hdJO1Y6t1B","marks":68},{"name":"8QcYS","marks":88},{"name":"6TXl2g","marks":53},{"name":"okbVlA","marks":0},{"name":"Ix","marks":43},{"name":"BS","marks":99},{"name":"oXYr8Hqh","marks":66},{"name":"et8SEo7BZV","marks":18},{"name":"uKGa","marks":99},{"name":"zjj69L","marks":93},{"name":"7cdow","marks":3},{"name":"kSm1RkSyvD","marks":3},{"name":"qKNZr3","marks":87},{"name":"P0","marks":97},{"name":"3","marks":17},{"name":"576","marks":16},{"name":"BS","marks":62},{"name":"PcCqnh","marks":58},{"name":"fxfG","marks":71},{"name":"6npD6nD","marks":85},{"name":"IVnF","marks":95},{"name":"dQhB","marks":79},{"name":"Eli0oK5","marks":52},{"name":"k","marks":28},{"name":"jOz80M8k","marks":92},{"name":"s593V1K7","marks":86},{"name":"eHaKF8","marks":12},{"name":"YEHK1CqtL","marks":8},{"name":"oCvUFDE","marks":79},{"name":"0W9gJq","marks":76},{"name":"7x9","marks":18},{"name":"Dh","marks":99},{"name":"LIo","marks":70},{"name":"mxyS6U","marks":43},{"name":"Hnecu","marks":19},{"name":"HmbGmnPRC6","marks":86},{"name":"Nv605w3","marks":68},{"name":"YT1EXaQA","marks":68},{"name":"UrOuhvgDSZ","marks":32},{"name":"ZZOTtPG","marks":10},{"name":"fFgBB","marks":81},{"name":"3y1rW7G","marks":11},{"name":"NsU","marks":40},{"name":"RcK","marks":58},{"name":"g","marks":74},{"name":"HVwA","marks":83},{"name":"3fhjsd","marks":5},{"name":"d","marks":15},{"name":"4aPFiU","marks":88},{"name":"aNN6i1","marks":23},{"name":"4gbZfYPX3","marks":56},{"name":"h4bCuvW","marks":17},{"name":"NdJT","marks":1},{"name":"FEb46ym0v","marks":60},{"name":"vnjc","marks":35},{"name":"h7Qad","marks":42},{"name":"oV8Jm1","marks":26},{"name":"7","marks":97},{"name":"wB","marks":82},{"name":"Sbma","marks":75},{"name":"sz5q6S","marks":27},{"name":"tvT","marks":65},{"name":"wyTfdLsTk","marks":34},{"name":"IuES","marks":48},{"name":"i28sZy","marks":24},{"name":"3hlB40s3","marks":19},{"name":"E6p4BtG","marks":20},{"name":"lY5Uy4uxYv","marks":85},{"name":"HOd1","marks":19},{"name":"2G6","marks":15},{"name":"Ue2","marks":89},{"name":"3","marks":95},{"name":"OfV0a3","marks":85},{"name":"YJNx","marks":46},{"name":"x5e8","marks":86},{"name":"lYGXvQ","marks":6}]


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse query parameters (e.g., ?name=Alice&name=Bob)
        query_params = self.parse_query_params()
        names = query_params.get('name', [])
        
        # Fetch marks for the provided names
        marks = [self.get_marks(name) for name in names]
        
        # Send the response as JSON
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
        """Helper method to get the marks for a given name (case-insensitive)."""
        name = name.lower()  # Convert the query name to lowercase
        for student in marks_json:
            if student['name'].lower() == name:  # Convert student name to lowercase
                return student['marks']
        return "Not Found"
