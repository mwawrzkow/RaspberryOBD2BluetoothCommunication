import obd
from obd import OBDStatus
class OBDInterpreter(object):
    """
    docstring
    """
    def ConnectToOBD(self):
        self.Connection = obd.OBD()
        if OBDStatus == OBDStatus.CAR_CONNECTED:
            return "Samochod jest podlaczony" 
        else:
            return "Samochod nie jest podlaczony"
    pass