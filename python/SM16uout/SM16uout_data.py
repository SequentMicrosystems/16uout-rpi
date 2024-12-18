CARD_NAME = "SM16uout"
VERSION = "1.0.0"

SLAVE_OWN_ADDRESS_BASE = 0x72
STACK_LEVEL_MAX = 7

CALIBRATION_KEY = 0xaa
RESET_CALIBRATION_KEY  = 0x55
WDT_RESET_SIGNATURE     = 0xca
WDT_RESET_COUNT_SIGNATURE    = 0xbe

VOLT_TO_MILIVOLT = 1000
MILIAMPER_TO_MICROAMPER = 1000

U_OUT_CH_NO = 16
LED_CH_SIZE = 16

ANALOG_VAL_SIZE = 2

# i2c memory addresses
class I2C_MEM:
	LEDS = 0
	LED_SET = 2
	LED_CLR = 3
	
	U_OUT = 4
	U0_10_OUT_VAL_END = 4 + U_OUT_CH_NO * ANALOG_VAL_SIZE

	CALIB_VALUE = 37
	CALIB_CHANNEL = 41
	CALIB_KEY = 42
	CALIB_STATUS = 43
	MODBUS_SETINGS_ADD = 44
	MBS1 = 45
	MBS2 = 46
	MBS3 = 47
	MODBUS_ID_OFFSET_ADD = 48
	WDT_RESET_ADD = 49
	WDT_INTERVAL_SET_ADD = 50
	WDT_INTERVAL_GET_ADD = 52
	WDT_INIT_INTERVAL_SET_ADD = 54
	WDT_INIT_INTERVAL_GET_ADD = 56
	WDT_RESET_COUNT_ADD = 58
	WDT_CLEAR_RESET_COUNT_ADD = 60
	WDT_POWER_OFF_INTERVAL_SET_ADD = 61
	WDT_POWER_OFF_INTERVAL_GET_ADD = 65
	DIAG_TEMPERATURE_ADD = 69
	DIAG_24V_MEM_ADD = 70
	DIAG_24V_MEM_ADD1 = 71
	DIAG_5V_MEM_ADD = 72
	DIAG_5V_MEM_ADD1 = 73
	CAN_REC_MPS_MEM_ADD = 74

	DIAG_12V_MEM_ADD = 75
	DIAG_12V_MEM_ADD1 = 76
	BUTTON = 77


	REVISION_HW_MAJOR_ADD = 250
	REVISION_HW_MINOR_ADD = 251
	REVISION_MAJOR_ADD = 252
	REVISION_MINOR_ADD = 253

	SLAVE_BUFF_SIZE = 255

class CALIB:
    IN_PROGRESS = 0
    DONE = 1
    ERROR = 2
    NOTHING = 0
    U_OUT_CH1 = 1
    LAST_CH = 16

CHANNEL_NO = {
    "u_out": 16,
    "led": 16,
}
