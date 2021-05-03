import logging

from gekitchensdk.erd.converters.abstract import ErdReadOnlyConverter
from gekitchensdk.erd.converters.primitives import *
from gekitchensdk.erd.values.laundry import ErdMachineSubCycle, MachineSubCycle, MACHINE_SUBCYCLE_MAP

_LOGGER = logging.getLogger(__name__)

class MachineSubCycleConverter(ErdReadOnlyConverter[MachineSubCycle]):
    def erd_decode(self, value: str) -> MachineSubCycle:
        """Decode the dishwasher operating state """
        try:
            om = ErdMachineSubCycle(erd_decode_int(value))
            ###_LOGGER.debug(f'raw operating mode value: {om}')
            return MACHINE_SUBCYCLE_MAP[om].value
        except (KeyError, ValueError):
            return ErdMachineSubCycle.NA
