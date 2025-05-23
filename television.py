
class Television:
    min_volume = 0
    max_volume = 2
    min_channel = 0
    max_channel = 3

    def __init__(self):
        self.status = False
        self.muted = False
        self.volume = self.min_volume
        self.channel = self.min_channel

    def power(self):
        self.status = True

    def mute(self):
        self.muted = True

    def channel_up(self):
        if self.channel == self.max_channel:
            self.channel = self.min_channel
        else:
            self.channel += 1

    def channel_down(self):
        if self.channel == self.min_channel:
            self.channel = self.max_channel
        else:
            self.channel -= 1

    def volume_up(self):
        if self.volume == self.max_volume:
            self.volume = self.max_volume
        else:
            self.volume += 1

    def volume_down(self):
        if self.volume == self.min_volume:
            self.volume = self.min_volume
        else:
            self.volume -= 1

    def __str__(self):
        return f'Power = {self.status}, Channel = {self.channel}, Volume = {self.volume}.'