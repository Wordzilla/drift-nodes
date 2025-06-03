# Node 5: Serializes and exports echo drift into digest format

import json

def export_drift_log(mapped_echo, path="drift_output.json"):
    with open(path, 'w') as f:
        json.dump(mapped_echo, f)
    return path
