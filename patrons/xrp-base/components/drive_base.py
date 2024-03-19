
from wpilib.drive import DifferentialDrive
from magicbot import tunable, will_reset_to
import xrp
import constants

class DriveBase:
    max_speed = tunable(1)
    __controller_speed = will_reset_to((0, 0))

    def setup(self):
        self.left_motor = xrp.XRPMotor(constants.LEFT_MOTOR)
        self.right_motor = xrp.XRPMotor(constants.RIGHT_MOTOR)
        self.robot_drive = DifferentialDrive(self.left_motor, self.right_motor)

    def drive(self, forward, rotate):
        forward_speed = -forward * self.max_speed
        rotate_speed = -rotate
        self.__controller_speed = (forward_speed, rotate_speed)

    def execute(self):
        self.robot_drive.arcadeDrive(self.__controller_speed[0], self.__controller_speed[1], squareInputs=True)
