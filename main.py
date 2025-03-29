import curses
import sys
import os

# Add the parent directory to the path so we can import from invoke_router
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from invoke_router.invoke import invoke

def main(stdscr):
    # Initialize curses
    curses.curs_set(0)  # Hide cursor
    stdscr.clear()
    
    # Start with page 1 by default
    current_page = "1"
    result = None
    
    while True:
        # Clear screen
        stdscr.clear()
        
        # Display current page
        result = invoke(current_page, stdscr, result)
        
        # Get command input
        stdscr.addstr(curses.LINES-1, 0, "> ")
        stdscr.refresh()
        curses.echo()
        command = stdscr.getstr(curses.LINES-1, 2).decode('utf-8').strip()
        curses.noecho()
        
        # Process command
        if command.lower() == "quit" or command.lower() == "exit":
            break
        elif command.lower().startswith("go "):
            try:
                new_page = command.split(" ")[1]
                current_page = new_page
            except IndexError:
                # Invalid command format
                pass

if __name__ == "__main__":
    curses.wrapper(main) 