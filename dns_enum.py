import dns.resolver

def get_dns_records(url):
    record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'CNAME']
    for record_type in record_types:
        try:
            answers = dns.resolver.resolve(url, record_type)
            print(f"\n[{record_type} Records]")
            for rdata in answers:
                print(rdata.to_text())
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.NoNameservers):
            print(f"\n[{record_type} Records] Not found.")
        except Exception as e:
            print(f"\nError fetching {record_type} record: {e}")