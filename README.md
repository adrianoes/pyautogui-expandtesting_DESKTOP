# pyautogui-expandtesting_DESKTOP

Desktop testing in [expandtesting](https://practice.expandtesting.com/notes/api/api-docs/) API documentation through PyAutoGUI. This project contains basic examples on how to use PyAutoGUI to test Desktop tests. Good practices such as hooks, custom commands and tags, among others, are used. All the necessary support documentation to develop this project is placed here. 

# Pre-requirements:

| Requirement                     | Version        | Note                                                            |
| :------------------------------ |:---------------| :-------------------------------------------------------------- |
| Visual Studio Code              | 1.96.4         | -                                                               |
| Python                          | 3.12.5         | -                                                               |
| Python VSC Extension            | 2024.22.2      | -                                                               |
| PyAutoGUI                       | 0.9.54         | -                                                               | 
| yperclip                        | 1.9.0          | -                                                               |            
| Pytest                          | 8.3.4          | -                                                               |
| Faker                           | 35.2.0         | -                                                               |
| pytest-html                     | 4.1.1          | -                                                               |

# Installation:

- See [Visual Studio Code page](https://code.visualstudio.com/) and install the latest VSC stable version. Keep all the prefereced options as they are until you reach the possibility to check the checkboxes below: 
  - :white_check_mark: Add "Open with code" action to Windows Explorer file context menu. 
  - :white_check_mark: Add "Open with code" action to Windows Explorer directory context menu.
Check then both to add both options in context menu.
- See [python page](https://www.python.org/downloads/) and download the latest Python stable version. Start the installation and check the checkboxes below: 
  - :white_check_mark: Use admin privileges when installing py.exe 
  - :white_check_mark: Add python.exe to PATH
and keep all the other preferenced options as they are.
- Look for Python in the extensions marketplace and install the one from Microsoft.
- Open windows propmpt as admin and execute ```pip install pyautogui``` to install PyAutoGUI.
- Open windows propmpt as admin and execute ```pip install pyperclip``` to install pyperclip.
- Open windows prompt as admin and execute ```pip install pytest``` to install Pytest.
- Open windows prompt as admin and execute ```pip install Faker``` to install Faker library.
- Open windows prompt as admin and execute ```pip install pytest-html``` to install pytest-html plugin.

# Tests:

- Execute ```pytest ./tests -v --html=./reports/report.html --self-contained-html``` to run tests in verbose mode and generate a report inside reports folder.

# Support:

- [expandtesting API documentation page](https://practice.expandtesting.com/notes/api/api-docs/)
- [expandtesting API demonstration page](https://www.youtube.com/watch?v=bQYvS6EEBZc)
- [PyAutoGUI](https://pypi.org/project/PyAutoGUI/)
- [pyperclip](https://pypi.org/project/pyperclip/)
- [ChatGPT](https://chatgpt.com/)
- [pytest](https://pypi.org/project/pytest/)
- [Faker](https://pypi.org/project/Faker/)
- [pytest-html](https://pypi.org/project/pytest-html/)

# Tips:

- UI and API tests to send password reset link to user's email and API tests to verify a password reset token and reset a user's password must be tested manually as they rely on e-mail verification.
- Navigate to the get_position.py directory and execute ```python get_position.py``` when theres is the need to find the coordinates of a point.
