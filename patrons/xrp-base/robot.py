#!/usr/bin/env python3

"""
Patron pour un robot XRP
Lancez le code avec `robotpy sim --xrp`
"""

import wpilib
from magicbot import MagicRobot
import xrp
from components import drive_base

import os
os.environ["HALSIMXRP_HOST"] = "192.168.42.1"
os.environ["HALSIMWS_PORT"] = "5000"


class MyRobot(MagicRobot):
    drivetrain: drive_base.DriveBase

    def createObjects(self):
        """
        C'est ici que les composants sont vraiment créé avec le signe =.
        Les composants avec un préfix connu tel que "intake_" vont être injectés.
        """
        self.xrp_io = xrp.XRPOnBoardIO()

        # General
        self.gamepad = wpilib.XboxController(0)

    def disabledPeriodic(self):
        """Mets à jours le dashboard, même quand le robot est désactivé"""
        pass

    def autonomousInit(self):
        """Cette fonction est appelée une seule fois lorsque le robot entre en mode autonome."""
        pass

    def autonomous(self):
        """Pour les modes auto de MagicBot, voir le dossier ./autonomous"""
        super().autonomous()

    def teleopInit(self):
        """Cette fonction est appelée une seule fois lorsque le robot en mode téléopéré."""
        pass

    def teleopPeriodic(self):
        """Cette fonction est appelée de façon périodique lors du mode téléopéré."""

        self.drivetrain.drive(
            self.gamepad.getLeftY(),
            self.gamepad.getRightX()
        )

        print(self.xrp_io.getUserButtonPressed())
