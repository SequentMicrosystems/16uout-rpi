

# Modbus

The [Sixteen 0-10V Analog Outputs 8-Layer Stackable HAT for Raspberry Pi](https://sequentmicrosystems.com/products/sixteen-0-10v-analog-outputs) can be accessed through the Modbus RTU protocol over the RS-485 port.
You can set up the RS-485 port with the **16uout** command.

Example:
```bash
~$ 16uout 0 cfg485wr 1 1 9600 1 0
```
Set Modbus RTU, slave address offset = 1, baud rate 9600bps, one stop bit, parity none
```bash
~$ 16uout -h cfg485wr
```
display the full set of options

## Slave Address
The slave address is added with the "stack level" dipswitches. For example, the dipswitches configuration for stack level 1  (one switch in position ID0 is ON) slave address offset to 1 corresponds to Modbus slave address 2.

## Modbus object types
All Modbus RTU object types with standard addresses are implemented: Coils, Discrete Inputs, Input registers, and Holding registers.

### Coils

Access level Read/Write, Size 1 bit

| Device function | Register Address | Modbus Address |
| --- | --- | --- |
| COIL_LED1 | 0001 | 0x00 |
| COIL_LED2 | 0002 | 0x01 |
| COIL_LED3 | 0003 | 0x02 |
| COIL_LED4 | 0004 | 0x03 |
| COIL_LED5 | 0005 | 0x04 |
| COIL_LED6 | 0006 | 0x05 |
| COIL_LED7 | 0007 | 0x06 |
| COIL_LED8 | 0008 | 0x07 |
| COIL_LED9 | 0009 | 0x08 |
| COIL_LED10 | 0010 | 0x09 |
| COIL_LED11 | 0011 | 0x0a |
| COIL_LED12 | 0012 | 0x0b |
| COIL_LED13 | 0013 | 0x0c |
| COIL_LED14 | 0014 | 0x0d |
| COIL_LED15 | 0015 | 0x0e |
| COIL_LED16 | 0016 | 0x0f |

### Discrete Inputs

Access level Read Only, Size 1 bit

| Device function | Register Address | Modbus Address |
| --- | --- | --- |
| | | |


### Input registers

Access level Read Only, Size 16 bits

| Device function | Register Address | Modbus Address| Description | Measurement Unit |
| --- | --- | --- | --- | --- |
| | | | | |


### Holding registers

Access level Read/Write, Size 16 bits

| Device function | Register Address | Modbus Address | Range | Description | Measurement Unit |
| --- | --- | --- | --- | --- | --- |
| HR_0_10V_OUT1 | 40001 | 0x00 | 0..10000 | Voltage output for CH1 | mV |
| HR_0_10V_OUT2 | 40002 | 0x01 | 0..10000 | Voltage output for CH2 | mV |
| HR_0_10V_OUT3 | 40003 | 0x02 | 0..10000 | Voltage output for CH3 | mV |
| HR_0_10V_OUT4 | 40004 | 0x03 | 0..10000 | Voltage output for CH4 | mV |
| HR_0_10V_OUT5 | 40005 | 0x04 | 0..10000 | Voltage output for CH5 | mV |
| HR_0_10V_OUT6 | 40006 | 0x05 | 0..10000 | Voltage output for CH6 | mV |
| HR_0_10V_OUT7 | 40007 | 0x06 | 0..10000 | Voltage output for CH7 | mV |
| HR_0_10V_OUT8 | 40008 | 0x07 | 0..10000 | Voltage output for CH8 | mV |
| HR_0_10V_OUT9 | 40009 | 0x08 | 0..10000 | Voltage output for CH9 | mV |
| HR_0_10V_OUT10 | 40010 | 0x09 | 0..10000 | Voltage output for CH10 | mV |
| HR_0_10V_OUT11 | 40011 | 0x0a | 0..10000 | Voltage output for CH11 | mV |
| HR_0_10V_OUT12 | 40012 | 0x0b | 0..10000 | Voltage output for CH12 | mV |
| HR_0_10V_OUT13 | 40013 | 0x0c | 0..10000 | Voltage output for CH13 | mV |
| HR_0_10V_OUT14 | 40014 | 0x0d | 0..10000 | Voltage output for CH14 | mV |
| HR_0_10V_OUT15 | 40015 | 0x0e | 0..10000 | Voltage output for CH15 | mV |
| HR_0_10V_OUT16 | 40016 | 0x0f | 0..10000 | Voltage output for CH16 | mV |




## Function codes implemented

* Read Coils (0x01)
* Read Discrete Inputs (0x02)
* Read Holding Registers (0x03)
* Read Input Registers (0x04)
* Write Single Coil (0x05)
* Write Single Register (0x06)
* Write Multiple Coils (0x0f)
* Write Multiple registers (0x10)

