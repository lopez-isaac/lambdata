"""
Class that represnts a cellphone
"""


class Cellphone:

    """
    Basic features for a cellphone
    """
    def __init__(self):
        self.internet = "wifi and mobile data"
        self.back_camera = "10 mega pixal back camera"
        self.other_features = "bluetooth"
    """
    Displays all the features of the cellphone
    """
    def Features(self):
        print(f"Cellphone features {self.internet},{self.back_camera},{self.other_features}")

"""
Cellphone subclass for smartphone
"""


class smartphone(Cellphone):
    def __init__(self):
        Cellphone.__init__(self)
        self.interface = "Touch screen display"
        self.front_camera = "12 mega pixal front camera"

    def Smart_features(self):
        print(f" Additional smartphone features,{self.interface} and {self.front_camera} ")
