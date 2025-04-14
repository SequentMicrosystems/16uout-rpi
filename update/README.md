# update

This is the [Sequent Microsystems](https://www.sequentmicrosystems.com) Sixteen 0-10V Analog Outputs 8-Layer Stackable HAT for Raspberry Pi firmware update tool.

## Usage

```bash
~$ git clone https://github.com/SequentMicrosystems/16uout-rpi.git
~$ cd 16uout-rpi/update/
~/16uout-rpi/update$ ./update 0
```
For 64-bit OS use the ```update64```.

If you clone the repository already, skip the first step. 
The command will download the newest firmware version from our server and write it to the board.
The stack level of the board must be provided as a parameter. 

During firmware updates, we strongly recommend to:
 - disconnecting all outputs from the board since they can change state unpredictably.
 - Stop any script/program/Node-RED flow that accesses the I2C port
