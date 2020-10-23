import obd
from obd import OBDStatus
class OBDInterpreter(object):
    """
    docstring
    """
    def ConnectToOBD(self):
        self.Connection = obd.OBD()
        return OBDStatus == OBDStatus.CAR_CONNECTED if b"Samochod jest podlaczony" else b"Samochod nie jest podlaczony"
    pass