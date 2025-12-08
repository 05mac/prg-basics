# tv_show.py file
# main program
from tv import TV

def main():
   # object creation
    tv1 = TV()

   # object usage
    tv1.show_status()
    tv1.turn_on()
    tv1.show_status()
    tv1.set_channel(5)
    tv1.show_status()
    tv1.turn_off()
    tv1.show_status()


if __name__ == "__main__":
   main() 

 