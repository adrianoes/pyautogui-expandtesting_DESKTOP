# pyautogui-expandtesting_DESKTOP

Desktop testing in [expandtesting](https://practice.expandtesting.com/notes/api/api-docs/) API documentation through PyAutoGUI. This project contains basic examples on how to use PyAutoGUI to test Desktop tests. Good practices such as hooks, custom commands and tags, among others, are used. All the necessary support documentation to develop this project is placed here. 

# Pre-requirements:

| Requirement                     | Version                     | Note                      |
| :------------------------------ |:----------------------------| :------------------------ |
| Visual Studio Code              | 1.96.4                      |                           |
| Python                          | 3.12.5                      |                           |
| Python VSC Extension            | 2024.22.2                   |                           |
| PyAutoGUI                       | 0.9.54                      |                           | 
| Pyperclip                       | 1.9.0                       |                           |            
| Pytest                          | 8.3.4                       |                           |
| Faker                           | 35.2.0                      |                           |
| pytest-html                     | 4.1.1                       |                           |
| xvfb                            | 2:21.1.12-1ubuntu1.1        | Remote dependency only.   |
| x11-utils                       | 7.7+6build2                 | Remote dependency only.   |
| xauth                           | 1:1.1.2-1build1             | Remote dependency only.   |
| ffmpeg                          | 7:6.1.1-3ubuntu5            |                           |
| ImageMagick                     | 8:6.9.12.98+dfsg1-5.2build2 | Remote dependency only.   |
| fluxbox                         | 1.3.7-1build2               | Remote dependency only.   |
| python3-tk                      | 3.12.3-0ubuntu1             | Remote dependency only.   |
| xterm                           | 390-1ubuntu3                | Remote dependency only.   |

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
- Open windows prompt as admin and execute ```pip install pytest``` to install Pytest.
- Open windows prompt as admin and execute ```pip install Faker``` to install Faker library.
- Open windows prompt as admin and execute ```pip install pytest-html``` to install pytest-html plugin.

# Tests:

- Execute ```pytest ./tests -v --html=./reports/report.html --self-contained-html``` to run tests in verbose mode and generate a report inside reports folder.

# Support:

- [expandtesting API documentation page](https://practice.expandtesting.com/notes/api/api-docs/)
- [expandtesting API demonstration page](https://www.youtube.com/watch?v=bQYvS6EEBZc)
- [PyAutoGUI](https://pypi.org/project/PyAutoGUI/)
- [ChatGPT](https://chatgpt.com/)
- [pytest](https://pypi.org/project/pytest/)
- [Faker](https://pypi.org/project/Faker/)
- [pytest-html](https://pypi.org/project/pytest-html/)
- [he Ultimate Guide to Install XVFB On Ubuntu 20.04](https://www.youtube.com/watch?v=ACYjKAMEvaQ)
- [How to Install Xvfb on Ubuntu 20.04](https://neuronvm.com/docs/install-xvfb-on-ubuntu-20-04/)
- [x11-utils](https://www.x.org/wiki/Releases/)
- [xauth](https://linux.die.net/man/1/xauth)
- [ffmpeg](https://ffmpeg.org/documentation.html)
- [ImageMagick](https://imagemagick.org/script/index.php)
- [python3-tk](https://wiki.python.org/moin/TkInter)
- [fluxbox](https://fluxbox.org/)
- [Fluxbox](https://wiki.archlinux.org/title/Fluxbox)
- [xterm](https://www.root.cz/man/1/xterm/)
- [Linux Commands Cheat Sheet](https://www.geeksforgeeks.org/linux-commands-cheat-sheet/)
- [Reusing output from last command in Bash [duplicate]](https://stackoverflow.com/a/48398357)
- [os](https://docs.python.org/3/library/os.html)
- [json](https://docs.python.org/3/library/json.html)
- [subprocess](https://docs.python.org/3/library/subprocess.html)
- [random](https://docs.python.org/3/library/random.html)
- [PyScreeze](https://pypi.org/project/PyScreeze/)

# Tips:

- API tests to send password reset link to user's email and to verify a password reset token and reset a user's password must be tested manually as they rely on e-mail verification.
- Python presented better performance calling functions from same files as tests. I will check better approaches.