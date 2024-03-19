
import wpilib
from wpilib.drive import DifferentialDrive
from magicbot import tunable, will_reset_to
import constants

class TankDrive:
    left_motor: wpilib.PWMMotorController
    right_motor: wpilib.PWMMotorController
    max_speed = tunable(1)
    __controller_command = will_reset_to((0, 0))
    __auto_command = will_reset_to((0, 0))

    def setup(self):
        """
        Appelé après l'injection
        """
        self.right_motor.setInverted(True)
        self.drivetrain = DifferentialDrive(self.left_motor, self.right_motor)

    def controller_move(self, left_speed, right_speed):
        """
        Déplace le robot
        """
        # On inverse les joystick (-1 est vers le haut)
        left_speed = -left_speed
        right_speed = -right_speed

        # On retire les petites valeurs pour que le robot ne bouge pas si on ne touche pas au joystick
        if abs(left_speed) < constants.CONTROLLER_LOWER_INPUT_THRESHOLD:
            left_speed = 0

        if abs(right_speed) < constants.CONTROLLER_LOWER_INPUT_THRESHOLD:
            right_speed = 0

        # On multiple par le facteur de vitesse
        left_speed = left_speed * self.max_speed
        right_speed = right_speed * self.max_speed

        self.__controller_command = (left_speed, right_speed)

    def auto_move(self, forward, rotate):
        """
        Déplace le robot en mode autonome
        """
        self.__auto_command = (forward, rotate)

    def execute(self):
        """
        Cette fonction est appelé à chaque itération/boucle
        C'est ici qu'on doit écrire la valeur dans nos moteurs
        """

        # Si on envoie une commande auto, on utilise arcadeDrive, sinon on utilise la manette avec tankDrive
        if self.__auto_command == (0, 0):
            self.drivetrain.tankDrive(self.__controller_command[0], self.__controller_command[1], squareInputs=True)
        else:
            self.drivetrain.arcadeDrive(self.__auto_command[0], self.__auto_command[1], squareInputs=False)

        # self.controller_command et __auto_command sont remis à (0, 0) après chaque boucle, donc empêche le robot de bouger en cas de bogue.
