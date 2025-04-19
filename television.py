
class Television:
    min_volume = 0
    max_volume = 2
    min_channel = 0
    max_channel = 3

    def __init__(self):
        """
        Method that sets default values to television object
        """
        self.status = False
        self.muted = False
        self.volume = self.min_volume
        self.channel = self.min_channel

    def power(self):
        """
        Turns the TV on
        :return: status to True
        """
        self.status = True

    def mute(self):
        """
        Mutes the TV
        :return: muted to True
        """
        self.muted = True

    def channel_up(self):
        """
        Turns the channel up
        :return: channel plus one or if channel is at max, will go back to minimum
        """
        if self.channel == self.max_channel:
            self.channel = self.min_channel
        else:
            self.channel += 1

    def channel_down(self):
        """
        Turns the channel down
        :return: channel minus one or if channel is at minimum, will go up to max
        """
        if self.channel == self.min_channel:
            self.channel = self.max_channel
        else:
            self.channel -= 1

    def volume_up(self):
        """
        Turns the volume up
        :return: volume plus one or remains at maximum if already is at maximum
        """
        if self.volume == self.max_volume:
            self.volume = self.max_volume
        else:
            self.volume += 1

    def volume_down(self):
        """
        Turns the volume down
        :return: volume minus one or remains at minimum if already at minimum
        """
        if self.volume == self.min_volume:
            self.volume = self.min_volume
        else:
            self.volume -= 1

    def __str__(self):
        """
        Prints the current values of status, channel, and volume
        :return: strings of current values of status, channel, and volume
        """
        return f'Power = {self.status}, Channel = {self.channel}, Volume = {self.volume}.'