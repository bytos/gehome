import logging

from gekitchensdk.erd.converters.abstract import ErdReadOnlyConverter
from gekitchensdk.erd.converters.primitives import *
from gekitchensdk.erd.values.laundry import ErdSoilLevel, SoilLevel, SOIL_LEVEL_MAP

_LOGGER = logging.getLogger(__name__)

class SoilLevelConverter(ErdReadOnlyConverter[SoilLevel]):
    def erd_decode(self, value: str) -> SoilLevel:
        """Decode the dishwasher operating state """
        try:
            om = ErdSoilLevel(erd_decode_int(value))
            ###_LOGGER.debug(f'raw operating mode value: {om}')
            return SOIL_LEVEL_MAP[om].value
        except (KeyError, ValueError):
            return ErdSoilLevel.NA
