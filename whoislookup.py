import whois

def target_whois(url):
    #domain_name = extract_domain(websiteToScan)

    try:

        whois_info = whois.whois(url)

        # Remove 'status' from the output
        whois_info.pop('status', None)
        whois_info.pop('None', None)
       # formatted_info = {}
        # print("\nWhois Information:")
        for key, value in whois_info.items():
            if isinstance(value, list):
                print(f"  {key.capitalize()}: {', '.join(map(str, value))}")
            else:
                print(f"  {key.capitalize()}: {value}")
        #    formatted_info[key] = value

       # return formatted_info

    except whois.parser.PywhoisError as e:
        print(f'Error during whois lookup: {e}')
        #return None




