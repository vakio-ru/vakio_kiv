"""Платформа для изменения положения заслонки устройств серии Vakio Kiv"""
from __future__ import annotations
from datetime import datetime, timedelta, timezone

from homeassistant.components.select import SelectEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import DEVICE_DEFAULT_NAME
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType
from homeassistant.helpers.event import async_track_time_interval

from .vakio import Coordinator
from .const import DOMAIN, KIV_GATES_DICT, KIV_STATE_NAME_OFF


async def async_setup_platform(
    hass: HomeAssistant,
    conf: ConfigType,
    async_add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    """Set up the demo Select entity."""
    kiv = VakioSelect(
        hass,
        conf.entry_id,
        unique_id="kiv",
        name="Vakio Kiv",
        icon="mdi:hvac",
        current_option="gate",
        options=list(KIV_GATES_DICT.keys()),
        translation_key="gate",
    )
    async_add_entities(
        [
            kiv,
        ]
    )
    coordinator: Coordinator = hass.data[DOMAIN][conf.entry_id]
    await coordinator.async_login()
    async_track_time_interval(
        hass,
        coordinator._async_update,  # pylint: disable=protected-access
        timedelta(seconds=1),
    )
    async_track_time_interval(
        hass,
        kiv._async_update,  # pylint: disable=protected-access
        timedelta(seconds=1),
    )


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the Demo config entry."""
    await async_setup_platform(hass, config_entry, async_add_entities)


class VakioSelect(SelectEntity):
    """Representation of a vakio select entity."""

    _attr_should_poll = False

    def __init__(
        self,
        hass: HomeAssistant,
        entry_id: str,
        unique_id: str,
        name: str,
        icon: str,
        current_option: str | None,
        options: list[str],
        translation_key: str,
    ) -> None:
        """Initialize the Demo select entity."""
        self.hass = hass

        self._attr_unique_id = unique_id
        self._attr_name = name or DEVICE_DEFAULT_NAME
        self._attr_current_option = current_option
        self._attr_icon = icon
        self._attr_options = options
        self._attr_translation_key = translation_key
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, unique_id)},
            name=name,
        )

        self.coordinator: Coordinator = hass.data[DOMAIN][entry_id]

    async def async_select_option(self, option: str) -> None:
        """Update the current selected option."""
        if option == KIV_STATE_NAME_OFF:
            await self.coordinator.turn_off()
        else:
            if not self.coordinator.is_on():
                await self.coordinator.turn_on()
            self._attr_current_option = option
            await self.coordinator.gate(KIV_GATES_DICT[option])
        # self.async_write_ha_state()

    async def _async_update(self, now: datetime):
        """
        Функция вызывается по таймеру.
        Выполняется сравнение параметров состояния устройства с параметрами записанными в классе.
        Если выявляется разница, тогда параметры класса обновляются.
        """
        current_gate = self.coordinator.get_gate()
        is_on = self.coordinator.is_on()
        if not is_on and self._attr_current_option != KIV_STATE_NAME_OFF:
            self._attr_current_option != KIV_STATE_NAME_OFF
            self.async_write_ha_state()
        if (
            self._attr_current_option not in KIV_GATES_DICT.keys()
            or KIV_GATES_DICT[self._attr_current_option] != current_gate
        ):
            for key, val in KIV_GATES_DICT.items():
                if val == current_gate:
                    new_key = key
            self._attr_current_option = new_key
            self.async_write_ha_state()
