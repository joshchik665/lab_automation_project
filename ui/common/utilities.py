# utilities.py

from PySide6.QtWidgets import QFileDialog
from ui.common_gui.message_boxes import invalid_filetype


def open_file_dialog(prompt:str, filetype:str, parent = None) -> str:
    """Opens a file dialog to open a file and returns the filepath for that file

    Args:
        prompt (str): Prompt that the user is shown
        filetype (str): The file type to be opened
        parent (QWidget, optional): The parent widget for this dialog. Defaults to None.

    Returns:
        str: Filepath
    """
    filetypes = {
        '.json': 'JSON Files (*.json)',
    }
    
    # Opens the filedialog, if the filetype desired is unknown, returns
    try:
        file_path, __ = QFileDialog.getOpenFileName(parent,prompt,r'configs\user_configs',filetypes[filetype])
    except KeyError:
        invalid_filetype()
        return ''
    
    # Only returns filepath if it is the correct type and exists
    if not file_path:
        return ''
    elif not file_path.endswith(filetype):
        invalid_filetype()
        return ''
    else:
        return file_path


def save_file_dialog(prompt:str, filetype:str, parent = None) -> str:
    """Opens a file dialog to save a file

    Args:
        prompt (str): Prompt for the user
        filetype (str): The filetype to be saved as
        parent (QWidget, optional): The parent widget. Defaults to None.

    Returns:
        str: The filepath to the file to be saved
    """
    filetypes = {
        '.json': 'JSON Files (*.json)',
    }
    
    # if the file type to be selected is not supported, let the user know and return nothing
    try:
        file_path, __ = QFileDialog.getSaveFileName(parent,prompt,r'configs\user_configs',filetypes[filetype])
    except KeyError:
        invalid_filetype()
        return ''
    
    return file_path


def remove_trailing_zeros(string:str) -> str:
    """Removes the trailing zeros and decimal point from a string, effectively converting it to and int

    Args:
        string (str): String to have its zeros removed

    Returns:
        str: the string without the zeros
    """
    while string.endswith('0'):
        string = string[:-1]
    if string.endswith('.'):
        string = string[:-1]
    return string