import tempfile
from file_io import write_file, append_file, read_file
import uuid
import os

'''Function write_files() in file_io.py'''
def test_write_file():

  #Create temp directory to write file to and see if it exits.
  with tempfile.TemporaryDirectory() as tmp_dirname:
    filename = str(uuid.uuid4())
    expected_file_content = str(uuid.uuid4())
    write_file(f'{tmp_dirname}/{filename}',expected_file_content)
    assert os.path.exists(f'{tmp_dirname}/{filename}.txt') == True
    
    # Check file content
    file_content = ''
    with open(f'{tmp_dirname}/{filename}.txt') as f:
      file_content = f.read()

      assert file_content == expected_file_content

'''Function append_file() in file_io.py'''
def test_append_to_file():

  #Create temp directory to write file to and see if it exits.
  with tempfile.TemporaryDirectory() as tmp_dirname:

    filename = str(uuid.uuid4())
    expected_file_content = f'{str(uuid.uuid4())}\n'
    append_content= f'{str(uuid.uuid4())}\n'
    append_content_two= f'{str(uuid.uuid4())}\n'

    write_file(f'{tmp_dirname}/{filename}', expected_file_content)
    append_file(f'{tmp_dirname}/{filename}', append_content)
    append_file(f'{tmp_dirname}/{filename}', append_content_two)

    assert os.path.exists(f'{tmp_dirname}/{filename}.txt') == True
    
    # Check file content
    expected_content_list = [expected_file_content, append_content, append_content_two]

    with open(f'{tmp_dirname}/{filename}.txt') as f:
      lines = f.readlines()
      assert(len(lines) == 3)
      index = 0

      for line in lines:
        assert expected_content_list[index] == line
        index += 1

'''Function read_file() in file_io.py'''

def test_read_file():

  #Create temp directory to write file to and see if it exits.
  with tempfile.TemporaryDirectory() as tmp_dirname:
    filename = str(uuid.uuid4())
    expected_file_content = str(uuid.uuid4())

    write_file(f'{tmp_dirname}/{filename}', expected_file_content)
    file_content = read_file(f'{tmp_dirname}/{filename}')

    assert os.path.exists(f'{tmp_dirname}/{filename}.txt') == True
    
    # Check file content
    assert expected_file_content == file_content