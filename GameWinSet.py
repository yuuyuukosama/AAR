import win32gui


def gameWin(FrameClass, FrameTitle):
    Handle = win32gui.FindWindow(FrameClass, FrameTitle)
    if Handle != 0:
        left, top, right, bot = win32gui.GetWindowRect(Handle)
        win32gui.MoveWindow(Handle, left, top, 1130, 723, True)
        return 1
    else:
        return 0
