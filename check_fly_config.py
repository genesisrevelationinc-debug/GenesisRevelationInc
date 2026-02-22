import requests
import json
import os

app_name = "genesisrevelationinc"
# Use the full compound token provided in the logs
token = "FlyV1 fm2_lJPECAAAAAAAEduexBBCQU4l8AAIk8RPL5c3vJ9CwrVodHRwczovL2FwaS5mbHkuaW8vdjGWAJLOABbVdx8Lk7lodHRwczovL2FwaS5mbHkuaW8vYWFhL3YxxDzdya4oZG7F3kdidxm9D0GyirVwtWydPhxajCzkQwsdWCp/FK9bvEkJAha7HGkgH60WCdeRZ/czG8by7F7ETj/unZx8bpL594a2KbNvwksD7ub+pSkrnIEDm+MlGwt1VosjY72Rb1z+wIZCYoGyGeOijL1LrVyl5t9RDm5vTlJcotG+KuPEy6yVrm4FYA2SlAORgc4A11TJHwWRgqdidWlsZGVyH6J3Zx8BxCBLOKIXGkp4hSZ49JnwYC+XxR2j0Fq3YpFyThrFItbVJg==,fm2_lJPETj/unZx8bpL594a2KbNvwksD7ub+pSkrnIEDm+MlGwt1VosjY72Rb1z+wIZCYoGyGeOijL1LrVyl5t9RDm5vTlJcotG+KuPEy6yVrm4FYMQQE603Jj0nwY/V3rvht2x2ysO5aHR0cHM6Ly9hcGkuZmx5LmlvL2FhYS92MZgEks5pmu1czwAAAAElkwt6F84AFecFCpHOABXnBQzEEIy9GgZM2JPqegsPuXyBCPrEIOyrwL+ozLnrUF7qLSfT8+U3TPfDh61pEP3QL4TkfeAT"
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

def check_machines():
    print(f"--- Monitoring Fly Sentinel: {app_name} ---")
    # Using public API endpoint as per documentation
    url = f"https://api.machines.dev/v1/apps/{app_name}/machines"
    try:
        res = requests.get(url, headers=headers, timeout=10)
        if res.status_code == 200:
            machines = res.json()
            for m in machines:
                print(f"Machine {m['id']} ({m['name']})")
                print(f"  State: {m['state']}")
                print(f"  Region: {m['region']}")
                print(f"  Private IP (6PN): {m.get('private_ip')}")
                
                # Check for shared IP in config
                services = m.get('config', {}).get('services', [])
                has_http = any(s.get('protocol') == 'tcp' for s in services)
                print(f"  HTTP Configured: {has_http}")
                
                # Check events for provisioning completion
                events = m.get('events', [])
                if events:
                    last_event = events[0]
                    print(f"  Last Event: {last_event['type']} at {last_event['timestamp']}")
        else:
            print(f"Failed to fetch machine data: HTTP {res.status_code}")
    except Exception as e:
        print(f"API Error: {str(e)}")

def check_ips():
    print(f"\n--- Checking IP Allocations ---")
    # GraphQL is often more reliable for IP broad view
    query = """
    query {
        app(name: "genesisrevelationinc") {
            ipAddresses {
                nodes {
                    address
                    type
                }
            }
        }
    }
    """
    try:
        res = requests.post("https://api.fly.io/graphql", json={'query': query}, headers=headers, timeout=10)
        if res.status_code == 200:
            data = res.json()
            ips = data.get('data', {}).get('app', {}).get('ipAddresses', {}).get('nodes', [])
            if not ips:
                print("  Zero IPs allocated.")
            for ip in ips:
                print(f"  Allocated {ip['type']}: {ip['address']}")
            
            has_v4 = any(ip['type'] == 'v4' for ip in ips)
            if not has_v4:
                print("  [ALERT] Shared IPv4 missing. Bridge required.")
        else:
            print(f"GraphQL Failed: HTTP {res.status_code}")
    except Exception as e:
        print(f"GraphQL Error: {str(e)}")

if __name__ == "__main__":
    check_machines()
    check_ips()
