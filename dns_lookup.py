import dns.resolver
from datetime import datetime

domain = input("Enter a domain name: ")

record_types = ["A", "AAAA", "CNAME", "MX", "NS", "TXT"]

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
filename = f"dns_report_{timestamp}.txt"

for record in record_types:
    try:
        answers = dns.resolver.resolve(domain, record)
        print(f"\n🔹 {record} records for {domain}:")
        file.write(f"\n🔹 {record} records for {domain}:\n")

        for rdata in answers:
            if record == "MX":
                print(f" - Mail Server: {rdata.exchange} (Priority: {rdata.preference})")
            else:
                print(f" - {rdata}")

    except dns.resolver.NoAnswer:
        print(f"\nNo {record} records found for {domain}.")
    except dns.resolver.NXDOMAIN:
        print(f"\nThe domain {domain} does not exist.")
        break
    except Exception as e:
        print(f"\nError looking up {record}: {e}")