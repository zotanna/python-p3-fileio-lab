import tempfile
from file_io import write_file, append_file, read_file
import uuid
import os


def test_write_file():
    '''file_io.py: write_file() takes a filename and input and writes the input to a file.'''
    write_file('lib/testing/write.txt', 'Hello, World!')
    f = open('lib/testing/write.txt', 'r')
    assert(f.read() == 'Hello, World!')
    os.remove('lib/testing/write.txt')

def test_append_to_file():
    '''file_io.py: append_file() takes an existing filename and input and writes the input to the file.'''
    write_file('lib/testing/append.txt', 'Hello, World!\n')
    append_file('lib/testing/append.txt', 'How are you doing today?')

    f = open('lib/testing/append.txt', 'r')
    assert(f.read() == 'Hello, World!\nHow are you doing today?')
    os.remove('lib/testing/append.txt')

def test_read_file():
    '''file_io.py: read_file() takes an existing filename and reads the text from the file.'''
    write_file('lib/testing/read.txt', 'Hello, World!')

    text = read_file('lib/testing/read.txt')
    assert(text == 'Hello, World!')
