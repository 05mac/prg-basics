# tv.py file
# class definition
class TV:
    def __init__(self):
      self.is_on = False
      self.channel = 1
      self.channel_list = []
    def set_channel(self,new_channel_no):
       self.channel = new_channel_no
    def show_channels(self):
       
    def set_channels(self,channel_list):
       
    def turn_off(self):
      self.is_on = False
    def turn_on (self):
      self.is_on = True
    def show_status(self):
        if self.is_on:
            print(f"TV is on, channel {self.channel}")
        else:
            print("TV is off")

# Do dokonczenia 