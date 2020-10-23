def RequestAction(Action, OBD):
    Result = "error"; 
    if Action == b"Connect":
        Result = OBD.ConnectToOBD()
    return Result