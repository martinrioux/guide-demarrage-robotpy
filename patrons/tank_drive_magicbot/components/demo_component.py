
import wpilib
import constants
from magicbot import tunable, will_reset_to


class DemoComponent:
    max_speed = tunable(1)
    __target_speed = will_reset_to(0)

    def setup(self):
        """
        Appelé après l'injection
        """
        self.motor = wpilib.PWMMotorController("DemoMotor", constants.PWM_DEMOMOTOR)

    def set_speed(self, speed):
        """
        Fait tourner le moteur à la vitesse spécifiée
        """
        # S'assure que la vitesse maximale ne peut pas être dépassée
        self.__target_speed = max(min(speed, self.max_speed), -self.max_speed)

    def execute(self):
        """
        Cette fonction est appelé à chaque itération/boucle
        C'est ici qu'on doit écrire la valeur dans nos moteurs
        """
        self.motor.set(self.__target_speed)
