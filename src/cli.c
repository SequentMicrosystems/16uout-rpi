#include "analog.h"
#include "board.h"
#include "calib.h"
#include "cli.h"
#include "comm.h"
#include "help.h"
#include "led.h"
#include "wdt.h"
#include "button.h"
#include "rs485.h"

const CliCmdType *gCmdArray[] = {
	&CMD_HELP,
	&CMD_VERSION,
	&CMD_LIST,
	&CMD_BOARD,
	&CMD_CAL_STATUS,
	&CMD_UOUT_READ,
	&CMD_UOUT_WRITE,
	&CMD_UOUT_CAL,
	&CMD_WDT_RELOAD,
	&CMD_WDT_GET_PERIOD,
	&CMD_WDT_SET_PERIOD,
	&CMD_WDT_GET_INIT_PERIOD,
	&CMD_WDT_SET_INIT_PERIOD,
	&CMD_WDT_GET_OFF_PERIOD,
	&CMD_WDT_SET_OFF_PERIOD,
	&CMD_WDT_GET_RESET_COUNT,
	&CMD_WDT_CLR_RESET_COUNT,
	&CMD_LED_READ,
	&CMD_LED_WRITE,
	&CMD_BUTTON_READ,
	&CMD_BUTTON_LATCH_READ,
	&CMD_CFG485_READ,
	&CMD_CFG485_WRITE,
	0
};
