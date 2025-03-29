import os
import json
import subprocess
import logging
from pathlib import Path

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_git_root():
    """
    Determine if the current directory is inside a Git repository.
    If so, return the repository root path.
    """
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except (subprocess.SubprocessError, FileNotFoundError):
        return None

def load_registry():
    """
    Load the panel registry from the configuration file.
    
    Search order:
    1. ./config/panels.json
    2. <git_root>/.config/invoke/panels.json
    3. Fall back to default hardcoded mapping
    
    Returns:
        dict: The panel registry mapping
    """
    # Try local config first
    local_config = Path("config/panels.json")
    if local_config.exists():
        logger.info(f"Loading panel registry from {local_config}")
        with open(local_config, 'r') as f:
            return json.load(f)
    
    # Try git root config
    git_root = get_git_root()
    if git_root:
        git_config = Path(git_root) / ".config" / "invoke" / "panels.json"
        if git_config.exists():
            logger.info(f"Loading panel registry from {git_config}")
            with open(git_config, 'r') as f:
                return json.load(f)
    
    # Fall back to default mapping
    logger.info("No config file found, using default panel mapping")
    return {
        "1": {
            "module": "examples.one",
            "label": "Page One",
            "aliases": ["one"]
        },
        "2": {
            "module": "examples.two",
            "label": "Page Two",
            "aliases": ["two"]
        }
    }

def resolve_panel_name(name, registry):
    """
    Resolve a panel name or alias to its registry key.
    
    Args:
        name (str): The panel name or alias to resolve
        registry (dict): The panel registry
        
    Returns:
        str: The resolved panel key, or None if not found
    """
    # Check for exact match
    if name in registry:
        return name
    
    # Check aliases
    for key, panel in registry.items():
        if "aliases" in panel and name in panel["aliases"]:
            return key
    
    return None

def get_module_name(panel_key, registry):
    """
    Get the module name for a panel key.
    
    Args:
        panel_key (str): The panel key
        registry (dict): The panel registry
        
    Returns:
        str: The module name, or None if not found
    """
    if panel_key in registry and "module" in registry[panel_key]:
        return registry[panel_key]["module"]
    return None 