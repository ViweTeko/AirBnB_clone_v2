#!/usr/bin/python3
""" Tests AirBnB clone modules """
import os
deom typing import TextIO
from models.engine.file_storage import FileStorage


def clear_stream(stream: TextIO):
    """Clears contents of given stream
    Args:
        stream: Stream to clear
    """
    if stream.seekable():
        stream.seek(0)
        stream.truncate(0)

def read_text_file(file_name):
    """Reads content of given file
    Args:
        file_name: Name of file
    Returns:
        str: contents of file
    """
    lines = []
    if os.path.isfile(file_name):
        with open(file_name, mode='r') as f:
            for line in f.readlines():
                lines.append(line)
    return ''.join(lines)

def write_text_file(file_name, text):
    """Writes a text to given file
    Args:
        file_name: Name of file written to
        text: Content of file
    """
    with open(file_name, mode='w') as f:
        f.write(text)

def reset_store(store: FileStorage, file_path='file.json'):
    """Resets items in given store
    Args:
        store: FileStorage to reset
        file_path: Path to store's file
    """
    with open(file_path, mode='w') as f:
        f.write('{}')
        if store is not None:
            store.reload()

def delete_file(file_path: str):
    """Removes existing file
    Args:
        store: FileStorage to reset
        file_path: Path to store's file
    """
    if os.path.isfile(file_path):
        os.unlink(file_path)
