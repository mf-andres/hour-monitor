import json
from datetime import date


class DayEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, date):
            return o.__str__()
        return json.JSONEncoder.default(self, o)
