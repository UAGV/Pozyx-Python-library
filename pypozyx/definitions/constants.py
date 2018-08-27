#!/usr/bin/env python
"""pypozyx.definitions.constants - contains all Pozyx constants, such as error definitions, delays, physical convertions."""

# Pozyx status returns
POZYX_FAILURE = 0x0
POZYX_SUCCESS = 0x1
POZYX_TIMEOUT = 0x8


class PozyxConstants:
    # Pozyx serial buffer sizes
    MAX_BUF_SIZE = 100
    MAX_SERIAL_SIZE = 28

    # Remote operations
    REMOTE_READ = 0x02
    REMOTE_WRITE = 0x04
    REMOTE_DATA = 0x06
    REMOTE_FUNCTION = 0x08

    # Pozyx delay constants
    DELAY_POLLING = 0.002
    DELAY_LOCAL_WRITE = 0.001
    DELAY_LOCAL_FUNCTION = 0.005
    DELAY_REMOTE_WRITE = 0.005
    DELAY_REMOTE_FUNCTION = 0.01
    DELAY_INTERRUPT = 0.1
    DELAY_RANGING = 0.2
    DELAY_MODE_CHANGE = 0.02
    DELAY_FLASH = 0.5

    # Pozyx timeout constants
    TIMEOUT_RANGING = 0.025
    TIMEOUT_REMOTE_RANGING = 0.1
    TIMEOUT_POSITIONING = 0.2
    TIMEOUT_REMOTE_POSITIONING = 0.4
    TIMEOUT_OPTIMAL_DISCOVERY = 0.1

    # Pozyx status returns
    STATUS_FAILURE = 0x0
    STATUS_SUCCESS = 0x1
    STATUS_TIMEOUT = 0x8

    # Pozyx interrupt pin
    INT_PIN0 = 0x0
    INT_PIN1 = 0x1

    # Pozyx led control indexes
    LED_CTRL_LED_RX = 0x10
    LED_CTRL_LED_TX = 0x20
    LED_ON = True
    LED_OFF = False

    # Pozyx device modes
    ANCHOR_MODE = 0
    TAG_MODE = 1

    # The GPIO modes
    GPIO_DIGITAL_INPUT = 0
    GPIO_PUSH_PULL = 1
    GPIO_OPEN_DRAIN = 1

    # The GPIO pull resistor configuration
    GPIO_NO_PULL = 0
    GPIO_PULL_UP = 1
    GPIO_PULL_DOWN = 2

    # anchor selection modes
    ANCHOR_SEL_MANUAL = 0
    ANCHOR_SEL_AUTO = 1

    # discovery options
    DISCOVERY_ANCHORS_ONLY = 0
    DISCOVERY_TAGS_ONLY = 1
    DISCOVERY_ALL_DEVICES = 2

    # Pozyx positioning dimensions
    DIMENSION_3D = 3
    DIMENSION_2D = 2
    DIMENSION_2_5D = 1

    # positioning algorithm options
    POSITIONING_ALGORITHM_UWB_ONLY = 0
    POSITIONING_ALGORITHM_TRACKING = 4
    POSITIONING_ALGORITHM_NONE = 2

    POSITIONING_ALGORITHMS = [POSITIONING_ALGORITHM_UWB_ONLY, POSITIONING_ALGORITHM_TRACKING]

    # ranging protocol options
    RANGE_PROTOCOL_PRECISION = 0x00
    RANGE_PROTOCOL_FAST = 0x01
    RANGE_PROTOCOL_TEST = 0x02

    # positioning filters
    FILTER_TYPE_NONE = 0
    FILTER_TYPE_FIR = 1
    FILTER_TYPE_MOVING_AVERAGE = 3
    FILTER_TYPE_MOVING_MEDIAN = 4

    # how to intercept pozyx events: by polling or by interrupts
    MODE_POLLING = 0
    MODE_INTERRUPT = 1

    # Division factors for converting the raw register values to meaningful
    # physical quantities
    POSITION_DIV_MM = 1.0
    PRESSURE_DIV_PA = 1000.0
    MAX_LINEAR_ACCELERATION_DIV_MG = 1.0
    ACCELERATION_DIV_MG = 1.0
    GYRO_DIV_DPS = 16.0
    MAGNETOMETER_DIV_UT = 16.0
    EULER_ANGLES_DIV_DEG = 16.0
    QUATERNION_DIV = 16384.0
    TEMPERATURE_DIV_CELSIUS = 1.0

    # flash configuration types
    FLASH_SAVE_REGISTERS = 1
    FLASH_SAVE_ANCHOR_IDS = 2
    FLASH_SAVE_NETWORK = 3
    FLASH_SAVE_ALL = 4

    # possible pin configuration settings
    INTERRUPT_CONFIG = 0x24
    PIN_MODE_PUSH_PULL = 0
    PIN_MODE_OPEN_DRAIN = 1

    # Possible pin activity states
    PIN_ACTIVE_LOW = 0
    PIN_ACTIVE_HIGH = 1

    # Possible UWB settings
    ALL_UWB_CHANNELS = [1, 2, 3, 4, 5, 7]
    ALL_UWB_BITRATES = [0, 1, 2]
    ALL_UWB_PRFS = [1, 2]
    ALL_UWB_PLENS = [0x04, 0x14, 0x24, 0x34, 0x08, 0x18, 0x28, 0x0C]

# Pozyx firmware identifiers
POZYX_FW_MAJOR = 0xF0
POZYX_FW_MINOR = 0xF

# Pozyx device identifier for hardware
POZYX_ANCHOR = 0x00
POZYX_TAG = 0x20

# Pozyx serial buffer sizes
MAX_BUF_SIZE = 100
MAX_SERIAL_SIZE = 28

# Pozyx delay constants
POZYX_DELAY_POLLING = 0.001
POZYX_DELAY_LOCAL_WRITE = 0.001
POZYX_DELAY_LOCAL_FUNCTION = 0.005
POZYX_DELAY_REMOTE_WRITE = 0.005
POZYX_DELAY_REMOTE_FUNCTION = 0.01
POZYX_DELAY_INTERRUPT = 0.1
POZYX_DELAY_CALIBRATION = 1
POZYX_DELAY_MODE_CHANGE = 0.02
POZYX_DELAY_RANGING = 0.025
POZYX_DELAY_REMOTE_RANGING = 0.1
POZYX_DELAY_POSITIONING = 0.2
POZYX_DELAY_REMOTE_POSITIONING = 0.4
POZYX_DELAY_FLASH = 0.5

# Pozyx positioning dimensions
POZYX_3D = 3
POZYX_2D = 2
POZYX_2_5D = 1

# Pozyx interrupt pin
POZYX_INT_PIN0 = 0x0
POZYX_INT_PIN1 = 0x1

# Pozyx led control indexes
POZYX_LED_CTRL_LEDRX = 0x10
POZYX_LED_CTRL_LEDTX = 0x20
POZYX_LED_ON = True
POZYX_LED_OFF = False

# Pozyx device modes
POZYX_ANCHOR_MODE = 0
POZYX_TAG_MODE = 1

# The GPIO modes
POZYX_GPIO_DIGITAL_INPUT = 0
POZYX_GPIO_PUSHPULL = 1
POZYX_GPIO_OPENDRAIN = 1

# The GPIO pull resistor configuration
POZYX_GPIO_NOPULL = 0
POZYX_GPIO_PULLUP = 1
POZYX_GPIO_PULLDOWN = 2

# anchor selection modes
POZYX_ANCHOR_SEL_MANUAL = 0
POZYX_ANCHOR_SEL_AUTO = 1

# discovery options
POZYX_DISCOVERY_ANCHORS_ONLY = 0
POZYX_DISCOVERY_TAGS_ONLY = 1
POZYX_DISCOVERY_ALL_DEVICES = 2

# positioning algorithm options
POZYX_POS_ALG_UWB_ONLY = 0
POZYX_POS_ALG_TRACKING = 4

# ranging protocol options
POZYX_RANGE_PROTOCOL_PRECISION = 0x00
POZYX_RANGE_PROTOCOL_FAST = 0x01
POZYX_RANGE_PROTOCOL_TEST = 0x02

# positioning filters
FILTER_TYPE_NONE = 0
FILTER_TYPE_FIR = 1
FILTER_TYPE_MOVINGAVERAGE = 3
FILTER_TYPE_MOVINGMEDIAN = 4

# how to intercept pozyx events: by polling or by interrupts
MODE_POLLING = 0
MODE_INTERRUPT = 1

# Division factors for converting the raw register values to meaningful
# physical quantities
POZYX_POS_DIV_MM = 1.0
POZYX_PRESS_DIV_PA = 1000.0
POZYX_MAX_LIN_ACCEL_DIV_MG = 1.0
POZYX_ACCEL_DIV_MG = 1.0
POZYX_GYRO_DIV_DPS = 16.0
POZYX_MAG_DIV_UT = 16.0
POZYX_EULER_DIV_DEG = 16.0
POZYX_QUAT_DIV = 16384.0
POZYX_TEMP_DIV_CELSIUS = 1.0

# flash configuration types
POZYX_FLASH_REGS = 1
POZYX_FLASH_ANCHOR_IDS = 2
POZYX_FLASH_NETWORK = 3
POZYX_FLASH_ALL = 4

# possible pin configuration settings
POZYX_INT_CONFIG = 0x24
PIN_MODE_PUSHPULL = 0
PIN_MODE_OPENDRAIN = 1

PIN_ACTIVE_LOW = 0
PIN_ACTIVE_HIGH = 1

POZYX_ALL_CHANNELS = [1, 2, 3, 4, 5, 7]
POZYX_ALL_BITRATES = [0, 1, 2]
POZYX_ALL_PRFS = [1, 2]
POZYX_ALL_PLENS = [0x04, 0x14, 0x24, 0x34, 0x08, 0x18, 0x28, 0x0C]

class PozyxErrorCodes:
    POZYX_ERROR_NONE = 0x00
    POZYX_ERROR_I2C_WRITE = 0x01
    POZYX_ERROR_I2C_CMDFULL = 0x02
    POZYX_ERROR_ANCHOR_ADD = 0x03
    POZYX_ERROR_COMM_QUEUE_FULL = 0x04
    POZYX_ERROR_I2C_READ = 0x05
    POZYX_ERROR_UWB_CONFIG = 0x06
    POZYX_ERROR_OPERATION_QUEUE_FULL = 0x07
    POZYX_ERROR_TDMA = 0xA0
    POZYX_ERROR_STARTUP_BUSFAULT = 0x08
    POZYX_ERROR_FLASH_INVALID = 0x09
    POZYX_ERROR_NOT_ENOUGH_ANCHORS = 0x0A
    POZYX_ERROR_DISCOVERY = 0X0B
    POZYX_ERROR_CALIBRATION = 0x0C
    POZYX_ERROR_FUNC_PARAM = 0x0D
    POZYX_ERROR_ANCHOR_NOT_FOUND = 0x0E
    POZYX_ERROR_FLASH = 0x0F
    POZYX_ERROR_MEMORY = 0x10
    POZYX_ERROR_RANGING = 0x11
    POZYX_ERROR_RTIMEOUT1 = 0x12
    POZYX_ERROR_RTIMEOUT2 = 0x13
    POZYX_ERROR_TXLATE = 0x14
    POZYX_ERROR_UWB_BUSY = 0x15
    POZYX_ERROR_POSALG = 0x16
    POZYX_ERROR_NOACK = 0x17
    POZYX_ERROR_SNIFF_OVERFLOW = 0xE0
    POZYX_ERROR_NO_PPS = 0xF0
    POZYX_ERROR_NEW_TASK = 0xF1
    POZYX_ERROR_UNRECDEV = 0xFE
    POZYX_ERROR_GENERAL = 0xFF

# error-code definitions
POZYX_ERROR_NONE = 0x00
POZYX_ERROR_I2C_WRITE = 0x01
POZYX_ERROR_I2C_CMDFULL = 0x02
POZYX_ERROR_ANCHOR_ADD = 0x03
POZYX_ERROR_COMM_QUEUE_FULL = 0x04
POZYX_ERROR_I2C_READ = 0x05
POZYX_ERROR_UWB_CONFIG = 0x06
POZYX_ERROR_OPERATION_QUEUE_FULL = 0x07
POZYX_ERROR_TDMA = 0xA0
POZYX_ERROR_STARTUP_BUSFAULT = 0x08
POZYX_ERROR_FLASH_INVALID = 0x09
POZYX_ERROR_NOT_ENOUGH_ANCHORS = 0x0A
POZYX_ERROR_DISCOVERY = 0X0B
POZYX_ERROR_CALIBRATION = 0x0C
POZYX_ERROR_FUNC_PARAM = 0x0D
POZYX_ERROR_ANCHOR_NOT_FOUND = 0x0E
POZYX_ERROR_FLASH = 0x0F
POZYX_ERROR_MEMORY = 0x10
POZYX_ERROR_RANGING = 0x11
POZYX_ERROR_RTIMEOUT1 = 0x12
POZYX_ERROR_RTIMEOUT2 = 0x13
POZYX_ERROR_TXLATE = 0x14
POZYX_ERROR_UWB_BUSY = 0x15
POZYX_ERROR_POSALG = 0x16
POZYX_ERROR_NOACK = 0x17
POZYX_ERROR_SNIFF_OVERFLOW = 0xE0
POZYX_ERROR_NO_PPS = 0xF0
POZYX_ERROR_NEW_TASK = 0xF1
POZYX_ERROR_UNRECDEV = 0xFE
POZYX_ERROR_GENERAL = 0xFF

ERROR_CODES = {
    PozyxErrorCodes.POZYX_ERROR_NONE: "NO ERROR",
    PozyxErrorCodes.POZYX_ERROR_I2C_WRITE: "ERROR 0x01: Error writing to a register through the I2C bus",
    PozyxErrorCodes.POZYX_ERROR_I2C_CMDFULL: "ERROR 0x02: Pozyx cannot handle all the I2C commands at once",
    PozyxErrorCodes.POZYX_ERROR_ANCHOR_ADD: "ERROR 0x03: Cannot add anchor to the internal device list",
    PozyxErrorCodes.POZYX_ERROR_COMM_QUEUE_FULL: "ERROR 0x04: Communication queue is full, too many UWB messages",
    PozyxErrorCodes.POZYX_ERROR_I2C_READ: "ERROR 0x05: Error reading from a register from the I2C bus",
    PozyxErrorCodes.POZYX_ERROR_UWB_CONFIG: "ERROR 0x06: Cannot change the UWB configuration",
    PozyxErrorCodes.POZYX_ERROR_OPERATION_QUEUE_FULL: "ERROR 0x07: Pozyx cannot handle all the operations at once",
    PozyxErrorCodes.POZYX_ERROR_STARTUP_BUSFAULT: "ERROR 0x08: Internal bus error",
    PozyxErrorCodes.POZYX_ERROR_FLASH_INVALID: "ERROR 0x09: Flash memory is corrupted or invalid",
    PozyxErrorCodes.POZYX_ERROR_NOT_ENOUGH_ANCHORS: "ERROR 0x0A: Not enough anchors available for positioning",
    PozyxErrorCodes.POZYX_ERROR_DISCOVERY: "ERROR 0x0B: Error during the Discovery process",
    PozyxErrorCodes.POZYX_ERROR_CALIBRATION: "ERROR 0x0C: Error during the auto calibration process",
    PozyxErrorCodes.POZYX_ERROR_FUNC_PARAM: "ERROR 0x0D: Invalid function parameters for the register function",
    PozyxErrorCodes.POZYX_ERROR_ANCHOR_NOT_FOUND: "ERROR 0x0E: The coordinates of an anchor are not found",
    PozyxErrorCodes.POZYX_ERROR_FLASH: "ERROR 0x0F: Flash error",
    PozyxErrorCodes.POZYX_ERROR_MEMORY: "ERROR 0x10: Memory error",
    PozyxErrorCodes.POZYX_ERROR_RANGING: "ERROR 0x11: Ranging failed",
    PozyxErrorCodes.POZYX_ERROR_RTIMEOUT1: "ERROR 0x12: Ranging timeout",
    PozyxErrorCodes.POZYX_ERROR_RTIMEOUT2: "ERROR 0x13: Ranging timeout",
    PozyxErrorCodes.POZYX_ERROR_TXLATE: "ERROR 0x14: Tx was late",
    PozyxErrorCodes.POZYX_ERROR_UWB_BUSY: "ERROR 0x15: UWB is busy",
    PozyxErrorCodes.POZYX_ERROR_POSALG: "ERROR 0x16: Positioning failed",
    PozyxErrorCodes.POZYX_ERROR_NOACK: "ERROR 0x17: No Acknowledge received",
    PozyxErrorCodes.POZYX_ERROR_NEW_TASK: "ERROR 0xF1: Cannot create task",
    PozyxErrorCodes.POZYX_ERROR_UNRECDEV: "ERROR 0xFE: Hardware not recognized. Please contact support@pozyx.io",
    PozyxErrorCodes.POZYX_ERROR_GENERAL: "ERROR 0xFF: General error",
}

ERROR_MESSAGES = ERROR_CODES
