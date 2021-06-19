import socket
from IPy import IP

def scan(target, port_from, port_to):
    converted_ip = check_ip(target)
    print('\n' + '[scanning target]' + str(target))
    for loop in range(port_from, port_to):
        scan_port(converted_ip, loop)

def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)

def get_banner(s):
    return s.recv(1024)

def scan_port(ipaddress,port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            print('Port ' + str(port)+  ' is open' + ' : ' + str(banner.decode().strip('\n')))
        except:
            print('Port ' + str(port)+  ' is open')
    except:
        pass

if __name__ == "__main__":
    targets = input('Enter target/s to scan (split multiple targets with comma): ')
    port_from = int(input('Enter the range of ports that you want to scan. \n From: '))
    port_to = int(input('To: '))
    if ',' in targets:
        for loop in targets.split(','):
            scan(loop.strip(' '),port_from,port_to)
    else:
        scan(targets,port_from,port_to)