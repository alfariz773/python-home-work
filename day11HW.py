from tracker import record
from datetime import datetime
import json

records = [
    record("Maldives", "15-05-2022"),
    record("Egypt", "20-06-2022"),
    record("Switzerland", "01-12-2023")
]

for rec in records:
    date_obj = datetime.strptime(rec["date"], "%d-%m-%Y")
    rec["date"] = date_obj.strftime("%B %d, %Y")

records_json = json.dumps(records, indent=2)
print("JSON Output:\n", records_json)

parsed_records = json.loads(records_json)

print("\nParsed Records:")
for rec in parsed_records:  
    print(rec)
 