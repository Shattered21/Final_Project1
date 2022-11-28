from view import *
from PyQt5.QtWidgets import *


QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    CHANNEL_0 = ('NO SIGNAL')
    CHANNEL_1 = ('NICKELODEON')
    CHANNEL_2 = (f'DISNEY\nCHANNEL')
    CHANNEL_3 = ('ABC FAMILY')

    def __init__(self, *args, **kwargs):

        '''
        Method constructs
        Method sets up all actions for gui buttons
        '''
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.__status = False
        self.__muted = False
        self.__volume = Controller.MIN_VOLUME
        self.__channel = Controller.MIN_CHANNEL

        self.power_but.clicked.connect(lambda: self.power())

        self.chal_up_but.clicked.connect(lambda: self.channel_up())
        self.chal_down_but.clicked.connect(lambda: self.channel_down())

        self.vol_up_but.clicked.connect(lambda: self.volume_up())
        self.vol_down_but.clicked.connect(lambda: self.volume_down())

        self.mute_but.clicked.connect(lambda: self.mute())

        self.select_1.clicked.connect(lambda: self.select_channel1())
        self.select_2.clicked.connect(lambda: self.select_channel2())
        self.select_3.clicked.connect(lambda: self.select_channel3())



    def power(self):
        '''
        Method checks if power button is on or off.
        Method also resumes tv actions when last turned off
        '''

        if self.__status == False:
            self.__status = True
            if self.__channel == 0:
                self.channel_label.setText('CH.0')
                self.screen_label.setText(Controller.CHANNEL_0)
            elif self.__channel == 1:
                self.channel_label.setText('CH.1')
                self.screen_label.setText(Controller.CHANNEL_1)
            elif self.__channel == 2:
                self.channel_label.setText('CH.2')
                self.screen_label.setText(Controller.CHANNEL_2)
            else:
                self.channel_label.setText('CH.3')
                self.screen_label.setText(Controller.CHANNEL_3)


        else:
            self.__status = False
            self.channel_label.setText(None)
            self.screen_label.setText(None)
            self.vol_label.setText(None)
            self.muted_label.setText(None)

    def mute(self):
        '''
        Method checks if mute button is on or off
        '''
        if self.__status:
            if self.__muted == False:
                self.__muted = True
                self.muted_label.setText('MUTED')
                self.vol_label.setText(f'VOL. {Controller.MIN_VOLUME}')


            else:
                self.__muted = False
                self.muted_label.setText(None)
                self.vol_label.setText(f'VOL. {self.__volume}')

    def channel_up(self):
        '''
        Method increases channel or starts channels over based on current location
        '''
        if self.__status:
            if self.__channel < Controller.MAX_CHANNEL:
                self.__channel += 1
                self.channel_label.setText(f'CH. {self.__channel}')

            else:
                self.__channel = Controller.MIN_CHANNEL
                self.channel_label.setText(f'CH. {self.__channel}')
            if self.__channel == 0:
                self.screen_label.setText(f'{Controller.CHANNEL_0}')
            elif self.__channel == 1:
                self.screen_label.setText(f'{Controller.CHANNEL_1}')
            elif self.__channel == 2:
                self.screen_label.setText(f'{Controller.CHANNEL_2}')
            else:
                self.screen_label.setText(f'{Controller.CHANNEL_3}')

    def channel_down(self):
        '''
        Method decreases channel or starts channels over based on current location
        '''
        if self.__status:
            if self.__channel > Controller.MIN_CHANNEL:
                self.__channel -= 1
                self.channel_label.setText(f'CH. {self.__channel}')
            else:
                self.__channel = Controller.MAX_CHANNEL
                self.channel_label.setText(f'CH. {self.__channel}')
            if self.__channel == 0:
                self.screen_label.setText(f'{Controller.CHANNEL_0}')
            elif self.__channel == 1:
                self.screen_label.setText(f'{Controller.CHANNEL_1}')
            elif self.__channel == 2:
                self.screen_label.setText(f'{Controller.CHANNEL_2}')
            else:
                self.screen_label.setText(f'{Controller.CHANNEL_3}')

    def volume_up(self):
        '''
        Method increases volume or starts volume over based on current location
        Method also unmutes volume if increased when muted
        '''
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.muted_label.setText(None)
            if self.__volume < Controller.MAX_VOLUME:
                self.__volume += 1
                self.vol_label.setText(f'VOL. {self.__volume}')

            else:
                self.__volume = Controller.MAX_VOLUME
                self.vol_label.setText(f'VOL. {self.__volume}')

    def volume_down(self):
        '''
        Method decreases volume or starts volume over based on current location
        Method also unmutes volume if decreased when muted
        '''
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.muted_label.setText(None)
            if self.__volume > Controller.MIN_VOLUME:
                self.__volume -= 1
                self.vol_label.setText(f'VOL. {self.__volume}')
            else:
                self.__volume = Controller.MIN_VOLUME
                self.vol_label.setText(f'VOL. {self.__volume}')


    def select_channel1(self):
        '''
        Method allows the user to use the pushbutton to go to channel 1
        '''
        if self.__status:
            if self.__channel != 1:
                self.__channel = 1
                self.screen_label.setText(f'{Controller.CHANNEL_1}')
                self.channel_label.setText(f'CH. {self.__channel}')

    def select_channel2(self):
        '''
        Method allows the user to use the pushbutton to go to channel 2
        '''
        if self.__status:
            if self.__channel != 2:
                self.__channel = 2
                self.screen_label.setText(f'{Controller.CHANNEL_2}')
                self.channel_label.setText(f'CH. {self.__channel}')

    def select_channel3(self):
        '''
        Method allows the user to use the pushbutton to go to channel 3
        '''
        if self.__status:
            if self.__channel != 3:
                self.__channel = 3
                self.screen_label.setText(f'{Controller.CHANNEL_3}')
                self.channel_label.setText(f'CH. {self.__channel}')

