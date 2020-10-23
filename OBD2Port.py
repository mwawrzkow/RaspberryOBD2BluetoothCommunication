import obd
from obd import OBDStatus
class OBDInterpreter(object):
    """
    docstring
    """
    def ConnectToOBD(self):
        self.Connection = obd.OBD()
        return OBDStatus == OBDStatus.CAR_CONNECTED ? b"Samochód jest podłączony" : b"Samochód nie jest podłączony"
    pass