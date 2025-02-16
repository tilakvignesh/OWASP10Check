# OWASP10Check
Repo which consists of python scripts or documents to understand the top 10 list better.

## A01 Broken Access Control

### What?:
    - As the name suggests, user access control in not configured properly.

### Misconfigured Access Control:
    - There's a script to demonstrate this. 
#### How to run?
    - start webapp.py. run python webapp.py
    - Then run mac.py with the required params to understand this better.
### Insecure Direct Object Reference:
    - Eg: when you use non-encoded query params in code without cleansing.
#### How to run?
    - Just run the script to demo it. You can check whether the url is vuln to this or not. (Under constraints)
    - Detect IDOR

## A02 Cryptographic failures

    - Eg: using weak hashes
### How to run?

    - run python weak_hash.py -w <your word list> -x <hash val>
    - If the hash is weak, it's easy to break.
    - Hash cracker

## A03 Injections
    - Eg: SQL injection
### How to run?
    - run python -m http.server <port> where the index.html is.
    - run the backend script.
    - Enjoy! Exploit by passing in customized inputs.
    - SQL injection demo
## A04 Insecure Design
    - Same demo as A03.
    - In this case, the insecure design is not sanitizing and encoding inputs before hand wherever required.

## A05 Security misconfigurations
    - Eg: Accidentally leaving port open. 
### How to run?
    - run python exposed_ports.py -p <port> -i <host> 
    - Note: host can be a subnet
    - It'll check if a port is open or not for that host.
    - Port scanner for a subnet

## A06 Vulerable and Outdated Components
    - There's a README to explain this

## A07 Identification & Authentication failures
    - Eg: credential stuffing

### How to run?
    - run  python cred_stuffing.py -i <host> -l <user password list> -o <output on successful login> 

    - What it does?: runs login for all cred pairs and returns pairs which were successful.

    - Brute forcing login.

## A08 Software and data integrity failures
    - Eg: Not checking hashes of softwares etc. 
### How to run?
    - run  npm i 
    - run  node server.js 
    - run jwt_exploit.py and see how important integrity checks are.
    - Integrity failure demo.


## A09 Security Logging and Monitoring Failure
    - Eg: Not logging effectively. 
### How to run?
    - run  limit_trigger.py 
    - What it does? Monitors event.json and triggers when unauthorized events for an IP exceed rate limit.
    - Prevent exceeded unauthorized events.

## A10 SSRF
    - Eg: Tricking servers to visit another site
### How to run?
    - run  detect_ssrf.py 
    - What it does? It's a proxy endpoint which sets up a URL whitelist which can be visited. 
    - Detects and prevents ssrf.


## Disclaimer

This repository is intended for educational purposes only. The scripts here should **only** be used on systems you have explicit permission to test. Unauthorized access to networks, systems, or applications is illegal and unethical. Use these scripts at your own risk and responsibility.


