import pyads

# Define the target ADS address of the PLC
plc_address = '192.168.200.10.1.1'

# Connect to the ADS port of the PLC
with pyads.Connection(plc_address, pyads.PORT_TC3PLC1) as plc:
    
    # Read the value of the parameters
    my_bool = plc.read_by_name('MAIN.my_bool', pyads.PLCTYPE_BOOL)
    my_name = plc.read_by_name('MAIN.my_name', pyads.PLCTYPE_STRING)
    my_age = plc.read_by_name('MAIN.my_age', pyads.PLCTYPE_INT)
    my_master_score = plc.read_by_name('MAIN.my_master_score', pyads.PLCTYPE_REAL)

    # Print the value of the parameter
    print(f'The value of the parameter "my_bool" is: {my_bool}')
    print(f'The value of the parameter "my_name" is: {my_name}')
    print(f'The value of the parameter "my_age" is: {my_age}')
    print(f'The value of the parameter "my_master_score" is: {my_master_score}')
