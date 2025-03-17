"""Constants for Dynamic Energy Cost."""
# Base component constants
NAME = "Dynamic Energy Cost"
DOMAIN = "dynamic_energy_cost"
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = "0.0.0"

ATTRIBUTION = "Data provided by http://jsonplaceholder.typicode.com/"
ISSUE_URL = "https://github.com/martinarva/dynamic_energy_cost/issues"

# Icons
ICON = "mdi:format-quote-close"

# Device classes
BINARY_SENSOR_DEVICE_CLASS = "connectivity"

# Platforms
SENSOR = "sensor"
PLATFORMS = [SENSOR]


# Configuration and options
ELECTRICITY_PRICE_SENSOR = "electricity_price_sensor"
POWER_SENSOR = "power_sensor"
ENERGY_SENSOR = "energy_sensor"
SERVICE_RESET_COST = "reset_cost"

HOURLY = "hourly"
DAILY = "daily"
WEEKLY = "weekly"
MONTHLY = "monthly"
YEARLY = "yearly"
MANUAL = "manual"

# Defaults
DEFAULT_NAME = DOMAIN


STARTUP_MESSAGE = f"""
-------------------------------------------------------------------
{NAME}
Version: {VERSION}
This is a custom integration!
If you have any issues with this you need to open an issue here:
{ISSUE_URL}
-------------------------------------------------------------------
"""
