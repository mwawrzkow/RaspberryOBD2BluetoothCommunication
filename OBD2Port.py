import obd
from obd import OBDStatus
class OBDInterpreter(object):
    """
    docstring
    """
    def ConnectToOBD(self):
        self.Connection = obd.OBD()
        return OBDStatus == OBDStatus.CAR_CONNECTED if "Samochod jest podlaczony" else "Samochod nie jest podlaczony"
    pass