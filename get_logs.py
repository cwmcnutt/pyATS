import netmiko

csr1kv1 = '10.254.0.1'
csr1kv2 = '10.254.0.2'
csr1kv3 = '10.254.0.3'

username = 'cisco'
password = 'cisco'
device_type = 'cisco_ios'
port = '22'

def get_log(ip):
    net_connect = netmiko.ConnectHandler(ip=ip, device_type=device_type,
        username=username, password=password, port=port)
    return net_connect.send_command('show log')

csr1kv1_log = get_log(csr1kv1)
csr1kv2_log = get_log(csr1kv2)
csr1kv3_log = get_log(csr1kv3)

print(csr1kv1_log)
print(csr1kv2_log)
print(csr1kv3_log)


