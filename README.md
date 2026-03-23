# DNS Lookup Script (Python)

## 📌 Description

This is a simple Python script that performs DNS lookups for a given domain.
It retrieves different types of DNS records like IP addresses, mail servers, and more.

---

## 🚀 Features

* Get multiple DNS records:

  * A (IPv4)
  * AAAA (IPv6)
  * CNAME
  * MX (Mail servers)
  * NS (Name servers)
  * TXT
* Handles errors for invalid or missing domains
* Easy to use

---

## 🛠️ Requirements

* Python 3
* dnspython library

Install dependency:

```id="p7e1m2"
pip install dnspython
```

---

## ▶️ How to Run

```id="m2x8l1"
python dns_lookup.py
```

Enter a domain name when asked:

```id="k9d2q0"
example.com
```

---

## 📊 Example Output

```id="w1v7c3"
A records:
 - 93.184.216.34

MX records:
 - mail.example.com (Priority: 10)
```

---

## 📄 Notes

This project is good for beginners learning:

* Understanding DNS record types
* Python networking-(Working with external Python libraries)
* Error handling

📄 License

This project is open-source and free to use.