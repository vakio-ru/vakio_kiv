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
CONF_PREFIX = "topic"

# Errors.
ERROR_AUTH: str = "ошибка аутентификации"
ERROR_CONFIG_NO_TREADY: str = "конфигурация интеграции не готова"

CONNECTION_TIMEOUT = 5

STATE_ENDPOINT = "state"
GATE_ENDPOINT = "gate"
TEMP_ENDPOINT = "temp"
HUD_ENDPOINT = "hud"
ENDPOINTS = [
    STATE_ENDPOINT,
    GATE_ENDPOINT,
    TEMP_ENDPOINT,
    HUD_ENDPOINT,
]

# OPT consts
OPT_EMERG_SHUNT = "emerg_shunt"
OPT_SMART_SPEED = "smart_speed"
OPT_SMART_GATE = "gate"
OPT_SMART_TOPIC_PREFIX = "server"

KIV_STATE_ON = "on"
KIV_STATE_OFF = "off"
KIV_WORKMODE_MANUAL = "manual"
KIV_WORKMODE_SUPERAUTO = "super_auto"
KIV_SPEED_00 = 0
KIV_SPEED_LIST = [
    KIV_SPEED_00,
]
KIV_GATE_01 = 1
KIV_GATE_02 = 2
KIV_GATE_03 = 3
KIV_GATE_04 = 4
KIV_GATE_LIST = [
    KIV_GATE_01,
    KIV_GATE_02,
    KIV_GATE_03,
    KIV_GATE_04,
]

SPEED_ENDPOINT = "speed"
GATE_ENDPOINT = "gate"
STATE_ENDPOINT = "state"
WORKMODE_ENDPOINT = "workmode"
TEMP_ENDPOINT = "temp"
HUD_ENDPOINT = "hud"
ENDPOINTS = [
    SPEED_ENDPOINT,
    GATE_ENDPOINT,
    STATE_ENDPOINT,
    WORKMODE_ENDPOINT,
    TEMP_ENDPOINT,
    HUD_ENDPOINT,
]

DEFAULT_PREFIX = "vakio"
