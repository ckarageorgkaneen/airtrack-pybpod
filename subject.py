"""Interface for the Airtrack subject (mouse)"""
import logging

from camera import AirtrackCamera
from camera import AirtrackCameraError
from camera_objects import AirtrackCameraObjects

# logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class AirtrackSubjectError(Exception):
    """AirtrackCamera error"""


def err(message):
    logger.debug(message)
    raise AirtrackSubjectError(message)


class AirtrackSubject:
    def __init__(self):
        self._camera = AirtrackCamera()

    def is_inside_lane(self):
        try:
            is_inside_lane = self._camera.detect_object(
                AirtrackCameraObjects.MOUSE)
        except AirtrackCameraError as e:
            err(str(e))
        return is_inside_lane
