#!/usr/bin/env python3
"""
Droit réservé (c) pour la FIRST et autres contributeurs WPILib.
Logiciel à source libre; vous pouvez modifier et/ou partager ce dernier
selon les termes de la licence BSD de WPILib.
"""


# Placez les importations des librairies nécessaires ici.
import wpilib
import wpilib.drive

# Par exemple, pour rajouter la librairie de CTRE, ajouter:
# import ctre


class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        """
        Cette fonction est appelée au démarrage du logiciel
        et ne devrait seulement servir qu'à initialiser le code.
        """
        self.moteurGauche = wpilib.PWMSparkMax(0)
        self.moteurDroite = wpilib.PWMSparkMax(1)
        self.robotDrive = wpilib.drive.DifferentialDrive(
            self.moteurGauche, self.moteurDroite
        )
        self.controller = wpilib.XboxController(0)
        self.timer = wpilib.Timer()

        # Nous devons inverser un moteur sur la base pilotable pour que
        # la base aille vers l'avant. Dépendement de votre base, vous devrez
        # peut-être inverser le côté gauche à la place.
        self.moteurDroite.setInverted(True)

    def disabledPeriodic(self):
        """Cette fonction est appelée, même quand le robot est désactivé"""
        pass

    def autonomousInit(self):
        """Cette fonction est appelée une seule fois lorsque le robot entre en mode autonome."""
        self.timer.restart()

    def autonomousPeriodic(self):
        """Cette fonction est appelée de façon périodique lors du mode autonome."""

        # Avance pour 2 seconde et arrête
        if self.timer.get() < 2.0:
            # On avance à la moitiée de la vitesse, n'oubliez pas de désactiver
            # le mode `square input` pour une meilleure réponse lors de l'automatisation
            self.robotDrive.arcadeDrive(0.5, 0, squareInputs=False)
        else:
            self.robotDrive.stopMotor()  # Arrête le robot

    def teleopInit(self):
        """Cette fonction est appelée une seule fois lorsque le robot entre en mode téléopéré."""

    def teleopPeriodic(self):
        """Cette fonction est appelée de façon périodique lors du mode téléopéré."""
        self.robotDrive.arcadeDrive(
            -self.controller.getLeftY(), -self.controller.getRightX()
        )

    def testInit(self):
        """Cette fonction est appelée une seule fois lorsque le robot entre en mode de test."""

    def testPeriodic(self):
        """Cette fonction est appelée de façon périodique lors du mode test."""
