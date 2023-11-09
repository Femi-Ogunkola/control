from typing import List

from control.function import Function
from control.signal import Signal

class Block:

    def __init__(self, inputs: List[Signal], output: Signal) -> None:
        self.inputs: List[Signal] = inputs
        self.output: Signal = output
        self.function = Function()
