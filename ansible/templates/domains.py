import requests
import json

import subprocess
from datetime import datetime, timezone

# hard coded assumptions
DOMAINS = ["hearty.cooking", "saelzler.org", "vincentsaelzler.com"] # this could possibly be dynamic in the future
BASE_URL = "https://api.godaddy.com/v1"
headers = {
    # secret is injected by ansible
    "Authorization": "sso-key {{ godaddy_key_and_secret }}",
    "Content-Type": "application/json",
}


def get_public_ip():
    dig_output = subprocess.run(
        ["dig", "+short", "myip.opendns.com", "@resolver1.opendns.com"],
        capture_output=True,
        text=True,
    )
    return str.strip(dig_output.stdout)


def get_root_host_record(root_host_record_endpoint):
    # https://developer.godaddy.com/doc/endpoint/domains#/v1/recordGet
    get_response = requests.get(root_host_record_endpoint, headers=headers)
    root_host_records = json.loads(get_response.text)

    if len(root_host_records) != 1:
        raise IndexError("expecting exactly one host record for the domain root")

    return root_host_records[0]


def put_root_host_record(root_host_record_endpoint, root_host_record):
    # returns a blank 200 response whether or not changes occur
    # https://developer.godaddy.com/doc/endpoint/domains#/v1/recordReplaceTypeName
    root_host_records = json.dumps([root_host_record])  # api requires an array
    put_response = requests.put(
        root_host_record_endpoint,
        data=root_host_records,
        headers=headers,
    )


for domain in DOMAINS:
    root_host_record_endpoint = f"{BASE_URL}/domains/{domain}/records/A/@"

    public_ip = get_public_ip()
    root_host_record = get_root_host_record(root_host_record_endpoint)
    current_ip = root_host_record["data"]

    if current_ip != public_ip:
        root_host_record["data"] = public_ip
        put_root_host_record(root_host_record_endpoint, root_host_record)

    output = str.join(',',[datetime.now(timezone.utc).isoformat(), domain, current_ip, public_ip])

    with open("log.csv", "a") as log_file:
        log_file.write(output)
        log_file.write("\n")
