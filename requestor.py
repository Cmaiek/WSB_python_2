import requests
import json

srv = "https://services.odata.org/v4/TripPinServiceRW/People('russellwhyte')"
result = requests.get(srv)
js = result.json()

print("Status {0}".format(result.status_code))
#print("Result: {0}".format(js))

pretty = json.dumps(js, indent=4, sort_keys=True)
print(pretty)
