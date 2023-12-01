"""Constants for the Vakio Openair integration."""
import datetime

from homeassistant.const import Platform

DOMAIN = "vakio_kiv"

# Platform
# PLATFORMS = [Platform.SENSOR, Platform.FAN]
PLATFORMS = [Platform.SELECT]

# Default consts.
DEFAULT_PORT = 1883
DEFAULT_TOPIC = "vakio"
DEFAULT_TIMEINTERVAL = datetime.timedelta(seconds=5)
DEFAULT_SMART_GATE = 4
DEFAULT_SMART_SPEED = 5
DEFAULT_SMART_EMERG_SHUNT = 10

# CONF consts.
CONF_HOST = "host"
CONF_PORT = "port"
CONF_USERNAME = "username"
CONF_PASSWORD = "password"
CONF_TOPIC = "topic"

# Errors.
ERROR_AUTH: str = "ошибка аутентификации"
ERROR_CONFIG_NO_TREADY: str = "конфигурация интеграции не готова"

CONNECTION_TIMEOUT = 5

# KIV
KIV_GATE_01 = 1
KIV_GATE_02 = 2
KIV_GATE_03 = 3
KIV_GATE_04 = 4
KIV_STATE_OFF = "off"
KIV_STATE_NAME_OFF = "Off"
KIV_STATE_ON = "on"
KIV_GATE_NAME_01 = "Gate 1"
KIV_GATE_NAME_02 = "Gate 2"
KIV_GATE_NAME_03 = "Gate 3"
KIV_GATE_NAME_04 = "Gate 4"
KIV_GATES_DICT = {
    KIV_STATE_NAME_OFF: -1,
    KIV_GATE_NAME_01: KIV_GATE_01,
    KIV_GATE_NAME_02: KIV_GATE_02,
    KIV_GATE_NAME_03: KIV_GATE_03,
    KIV_GATE_NAME_04: KIV_GATE_04,
}
