from genie.testbed import load
testbed = load('working-tb.yaml')

device = testbed.devices['nx-osv-1']
device.connect()
parsed_output = device.parse('show interface')
for interface in parsed_output:
    crc_error = parsed_output[interface].get('counters', {}).get('in_crc_errors')

    if crc_error and crc_error > 0:
        print('Interface {intf} has crc_error of value {crc_error}'.format(intf=interface, crc_error=crc_error))