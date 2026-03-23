import dns.resolver

domain = input("Enter a domain name: ")

record_types = ["A", "AAAA", "CNAME", "MX", "NS", "TXT"]

for record in record_types:
    try:
        answers = dns.resolver.resolve(domain, record)
        print(f"\n🔹 {record} records for {domain}:")

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