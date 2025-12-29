# tv.py file
# class definition
class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels_list = []
        self.volume = 0

    def increaseVolume(self, amount):
        self.volume += amount
        if self.volume > 10:
            self.volume = 10

    def decreaseVolume(self, amount):
        self.volume -= amount
        if self.volume < 0:
            self.volume = 0

    def turn_off(self):
        self.is_on = False
        print("telewizor zostal wylaczony")

    def turn_on(self):
        self.is_on = True
        print("telewizor zostal wlaczony")

    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no

    def set_channels(self, channels_list):
        self.channels_list = channels_list

    def show_channels(self):
        if len(self.channels_list) > 0:
            print(f"Lista dostępnych kanałów: ")
            for index, value in enumerate(self.channels_list):
                print(f"{index + 1 }. {value}")
        else:
            print("Brak dostępnych kanłów")

    def show_status(self):
        if self.is_on:
            for index, value in enumerate(self.channels_list):
                if (index + 1) == self.channel_no:
                    print(
                        f"telewizor jest wlaczony, oraz jest na kanale: {index + 1} - {value} głośność: {self.volume}")
        else:
            print("telewizor jest wylaczony")
