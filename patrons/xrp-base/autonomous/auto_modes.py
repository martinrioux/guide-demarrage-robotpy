from .base_auto import BaseAuto
from magicbot.state_machine import timed_state
from components import drive_base


class ForwardAndReverse(BaseAuto):
    MODE_NAME = "ForwardAndReverse"
    DEFAULT = True

    # Injection
    drivetrain: drive_base.DriveBase

    @timed_state(duration=1, next_state="reverse", first=True)
    def forward(self):
        # Avance 1 seconde et arrête
        self.drivetrain.drive(1, 0)


    @timed_state(duration=1, next_state="finish")
    def reverse(self):
        # Recule 1 seconde et arrête
        self.drivetrain.drive(-1, 0)
