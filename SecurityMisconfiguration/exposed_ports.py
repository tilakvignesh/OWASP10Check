# Port scanner checking for exposed public port. 

"""
NOTE: When ports like 22 are publicly open it's a security misonfiguration.
Or any port for that matter which provides more information than necessary.

"""

import socket
import argparse
import ipaddress
def check_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((str(host), int(port)))
    ans = ''
    if result == 0:
        ans = f'port {port} on {host} is open'
    else:
        ans = 'closed port'
    sock.close()
    return ans

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description = 'Take IP and port as input')
    parser.add_argument('-p', '--port', help = 'Port number', required = True)
    parser.add_argument('-i', '--host', help = 'Host IP', required = True)
    args = parser.parse_args()
    host = args.host
    port = args.port
    ips = ipaddress.ip_network(host)
    for ip in ips:
        result = check_port(ip, port)
        if result != 'closed port':
            print(result)

