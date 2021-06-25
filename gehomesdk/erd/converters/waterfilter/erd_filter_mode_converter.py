from ..abstract import ErdReadOnlyConverter
from ..primitives import *

from gehomesdk.erd.values.waterfilter import ErdWaterFilterMode

class ErdFilterModeConverter(ErdReadOnlyConverter[ErdWaterFilterMode]):
    def erd_decode(self, value) -> ErdWaterFilterMode:
        try:
            return ErdWaterFilterMode(value)
        except ValueError:
            return ErdWaterFilterMode.UNKNOWN