import visa

visa_dll = 'c:/windows/system32/visa32.dll'
tcp_addr = 'TCPIP::192.168.1.1::inst0::INSTR'
gpib_addr = "GPIB0::12::INSTR"

# Create an object of visa_dll
rm = visa.ResourceManager(visa_dll)

# Create an instance of certain interface(GPIB and TCPIP)
tcp_inst = rm.open_resource(tcp_addr)
gpib_inst = rm.open_resource(gpib_addr)

# Command '*IDN?' can fetch instrument info
# Using write()/read()/query() function to make communication with device
# according to the command type
print(tcp_inst.query('*IDN?'))
print(gpib_inst.query('*IDN?'))
