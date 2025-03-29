import importlib
import curses
import sys
import os
from invoke_router.utils.panel_registry import load_registry, resolve_panel_name, get_module_name

def invoke(panel_name, stdscr, context=None):
    """
    Dynamically imports and runs the specified panel module.
    
    Args:
        panel_name (str): The name of the panel to invoke
        stdscr: The curses standard screen object
        context: Optional data to pass between panels
        
    Returns:
        Any data returned by the panel's run function
    """
    try:
        # Load the panel registry
        registry = load_registry()
        
        # Resolve the panel name to a registry key
        panel_key = resolve_panel_name(panel_name, registry)
        if not panel_key:
            raise ImportError(f"No panel found with name or alias '{panel_name}'")
        
        # Get the module name for the panel
        module_name = get_module_name(panel_key, registry)
        if not module_name:
            raise ImportError(f"No module defined for panel '{panel_key}'")
            
        # Import the module dynamically
        module = importlib.import_module(module_name)
        
        # Run the module's run function
        return module.run(stdscr, context)
    except ImportError as e:
        # Handle case where module doesn't exist
        stdscr.clear()
        stdscr.addstr(0, 0, f"Error: Panel '{panel_name}' not found")
        stdscr.addstr(1, 0, f"Details: {str(e)}")
        stdscr.refresh()
        return None
    except AttributeError as e:
        # Handle case where module doesn't have run function
        stdscr.clear()
        stdscr.addstr(0, 0, f"Error: Panel '{panel_name}' doesn't have a run function")
        stdscr.addstr(1, 0, f"Details: {str(e)}")
        stdscr.refresh()
        return None 