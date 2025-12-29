# tv_show.py file
# main program
import tv


def main():
    # object creation
    telewizor_salon = tv.TV()

    # object usage
    telewizor_salon.show_status()
    telewizor_salon.turn_on()
    telewizor_salon.show_status()
    telewizor_salon.show_channels()
    telewizor_salon.set_channels(["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery","TV TRWAM"])
    telewizor_salon.show_channels()
    
    telewizor_salon.increaseVolume(2)
    telewizor_salon.show_status()
    telewizor_salon.set_channel(2)
    telewizor_salon.decreaseVolume(3)
    telewizor_salon.show_status()
    telewizor_salon.set_channel(3)
    telewizor_salon.show_status()
    telewizor_salon.set_channel(4)
    telewizor_salon.show_status()
    telewizor_salon.set_channel(5)
    telewizor_salon.show_status()
    telewizor_salon.set_channel(6)
    telewizor_salon.show_status()
    telewizor_salon.set_channel(7)
    telewizor_salon.show_status()
if __name__ == "__main__":
    main()
