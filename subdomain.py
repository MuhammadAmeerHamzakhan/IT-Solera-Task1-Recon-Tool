import requests


# crt.sh -> get certificate logs
def crtsh_api(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    subdom = set()  # using set to avoid duplicates

    try:
        response = requests.get(url, timeout=20)  # send GET request
        data = response.json()  # parse response for data

        for log in data:
            name = log.get("name_value", "")
            for sub in name.split('\n'):  # split if multiple logs in data
                if sub.endswith(domain):  # filter subdomains
                    subdom.add(sub.strip())  # add subdomain in set
    except Exception as e:
        print("crt.sh enumeration failed! {e}")

    return list(subdom)  # return list of discovered subdomains


# alienVault -> get DNS data
def alienvault_api(domain):
    url = f"https://otx.alienvault.com/api/v1/indicators/domain/{domain}/passive_dns"
    subdom = set()

    try:
        response = requests.get(url, timeout=20)
        data = response.json()

        for log in data.get("passive_dns", []):
            hostname = log.get("hostname", "")
            if hostname.endswith(domain):
                subdom.add(hostname.strip())
    except Exception as e:
        print("AlienVault enumeration failed! {e}")

    return list(subdom)


def getSubdomains(domain) -> list:
    # get subdomains from APIs
    crtshDomains = crtsh_api(domain)
    alienDomains = alienvault_api(domain)

    # merge subdomains
    TotalSubs = set(crtshDomains + alienDomains)

    return sorted(TotalSubs)  # return all subdomains

