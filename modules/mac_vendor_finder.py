import json

f = open('mac-vendors-export.json', encoding="utf-8")
data = json.load(f)
f.close()

def searchByVendor(mac_address):
    mac_prefix = mac_address[:8].upper()
    matching_records = filter(lambda vendor: vendor['macPrefix'] == mac_prefix, data)
    return f"({list(matching_records)[0]['vendorName']})"

