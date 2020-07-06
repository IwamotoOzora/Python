from python3_test1 import MP3Player
from python3_test3 import CellPhone

class SmartPhone(MP3Player, CellPhone):
    pass

smartPhone = SmartPhone("080-1111-1111", "aiueo@mail.co.jp")

smartPhone.play_music()
smartPhone.next_song()
smartPhone.previous_song()
smartPhone.stop_music()
smartPhone.call()
smartPhone.send_mail()