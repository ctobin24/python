import pytest
from television import *

class Test:
    def setup_method(self):
        self.t1 = Television()

    def teardown_method(self):
        del self.t1

    def test_init(self):
        assert self.t1.status == False
        assert self.t1.muted == False
        assert self.t1.volume == 0
        assert self.t1.channel == 0

    def test_power(self):
        assert self.t1.status == True

    def test_mute(self):
        assert self.t1.muted == True

    def test_channel_up(self):
        assert self.t1.channel_up() == 1
        assert self.t1.channel_up() == 2
        assert self.t1.channel_up() == 0

    def test_channel_down(self):
        assert self.t1.channel_down() == 2
        assert self.t1.channel_down() == 1
        assert self.t1.channel_down() == 0

    def test_volume_up(self):
        assert self.t1.volume_up() == 1
        assert self.t1.volume_up() == 2
        assert self.t1.volume_up() == 3
        assert self.t1.volume_up() == 3

    def test_volume_down(self):
        assert self.t1.volume_down() == 2
        assert self.t1.volume_down() == 1
        assert self.t1.volume_down() == 0
        assert self.t1.volume_down() == 0
