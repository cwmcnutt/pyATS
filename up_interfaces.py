from genie.testbed import load
testbed = load('working-tb.yaml')

device = testbed.devices['nx-osv-1']
device.connect()

parsed_output = device.parse('show interface')

for interface in parsed_output:
    state = parsed_output[interface]['admin_state']
  
    if state == 'up':
	    print('Interaface {intf} is {state}'.format(intf=interface, state=state))