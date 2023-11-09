from typing import List
from control.signal import Signal
class Takeoff:

    def __init__(self) -> None:
        self.input: Signal = None
        self.outputs: List[Signal] = []
