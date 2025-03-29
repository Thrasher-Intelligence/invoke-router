import curses

def run(stdscr, context=None):
    """
    Run the second page.
    
    Args:
        stdscr: The curses standard screen object
        context: Optional data passed from previous page
        
    Returns:
        Optional data to pass to the next page
    """
    # Set up colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    
    # Display page content
    stdscr.addstr(0, 0, "PAGE 2", curses.A_BOLD)
    stdscr.addstr(2, 0, "This is the second page.")
    stdscr.addstr(4, 0, "Type 'go 1' to navigate back to page 1")
    stdscr.addstr(5, 0, "Type 'exit' to quit")
    
    if context:
        stdscr.addstr(7, 0, f"Received context: {context}", curses.color_pair(1))
    
    stdscr.refresh()
    
    # Return some data to pass to the next page
    return "Data from page 2" 