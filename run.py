from importlib import reload
import main as main_module
import curses
import time
import os

def cursesMain ( stdscr ):
    cached_stamp = 0

    main_module.preload ( stdscr )

    while True:
        stamp = os.stat ( './main.py' ).st_mtime
        if stamp != cached_stamp:
            cached_stamp = stamp
            try:
                reload ( main_module )
                main_module.setup ( stdscr )
            except:
                pass

        stdscr.clear ()

        try:
            # draw the frame
            main_module.draw ( stdscr, time.clock_gettime ( time.CLOCK_REALTIME ) )
        except:
            pass

        stdscr.refresh ()
        time.sleep ( 0.05 )

if __name__ == "__main__":
    curses.wrapper ( cursesMain )
