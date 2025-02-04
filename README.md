# robot-expandtesting_UI_and_API

UI and API testing in [expandtesting](https://practice.expandtesting.com/notes/app/) note app. This project contains basic examples on how to use Robot Framework to test UI, API and how to combine UI and API tests. Good practices such as hooks, custom commands and tags, among others, are used. All the necessary support documentation to develop this project is placed here. When it comes to the API part, it deals with the x-www-form-urlencoded content type. Although custom commands are used, the assertion code to each test is kept in it so we can work independently in each test. It creates one .json file for each test so we can share data between different requests in the test. The .json file is excluded after each test execution. 

# Pre-requirements:

| Requirement                     | Version        | Note                                                            |
| :------------------------------ |:---------------| :-------------------------------------------------------------- |
| Visual Studio Code              | 1.96.4         | -                                                               |
| Python                          | 3.12.5         | -                                                               |
| Python VSC Extension            | 2024.22.2      | -                                                               |
| PyAutoGUI                       | 0.9.54         | -                                                               | 
| yperclip                        | 1.9.0          | -                                                               |

| Browser Library                 | 18.8.1         | -                                                               | 
| RequestsLibrary                 | 0.9.7          | -                                                               | 
| JSONLibrary                     | 0.5            | -                                                               | 
| robotframework-faker            | 5.0.0          | -                                                               |
| setuptools                      | 75.1.0         | -                                                               |  
| Robot Framework Language Server | 1.12.0         | -                                                               |
| Chrome TruePath                 | 1.0.0          | Optional. Recommended so you can work with accurate locators.   |              

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
- Navigate to the get_position.py directory and execute ```python get_position.py``` when theres is the need to find the coordinates of a point.








- Open windows propmpt as admin and execute ```pip install robotframework-pabot``` to install Pabot plugin.
- Open windows propmpt as admin and execute ```pip install robotframework-browser``` to install Browser library.
- Open windows propmpt as admin and execute ```pip install robotframework-requests``` to install RequestsLibrary.
- Open windows propmpt as admin and execute ```pip install robotframework-jsonlibrary``` to install JSONLibrary.
- Open windows propmpt as admin and execute ```pip install robotframework-faker``` to install robotframework-faker.
- Open windows propmpt as admin and execute ```pip install setuptools``` to install setuptools package.
- Open windows propmpt as admin and execute ```rfbrowser init``` to initialize the Browser library.
- Look for Robot Framework Language Server in the extensions marketplace and install the one from Robocorp.

# Tests:

- Execute ```robot -d ./results tests``` to run all tests in headless mode and store results in separated folder.
- Execute ```robot -d ./results .\tests\ui\users_ui.robot``` to run all the tests in the users_ui.robot suite in headless mode and store results in separated folder.
- Execute ```robot -d ./results -t "Change a user\'s password via UI" tests/ui/users_ui.robot``` to run Change a user's password via UI test case inside users_ui.robot suite and store results in separated folder.
- Hit :point_right:**Testing** button on left side bar in VSC and choose the tests you want to execute.
- Execute ```robot -d results -i BASIC tests``` to run the tests tagged with API tag and store results in separated folder.
- Execute ```robot -d results -e UI -e NEGATIVE .\tests\api\notes_ui.robot``` to run all the tests but the ones tagged with UI, NEGATIVE or both tags inside notes_ui.robot suite and store results in separated folder.
- Execute ```robot -d results -i API -i FULL .\tests\api\users_api.robot``` to run all the tests tagged with API, FULL or both tags inside users_api.robot suite and store results in separated folder.
- Execute ```robot -d results -i UI_AND_API .\tests\api\users_ui_and_api.robot``` to run all the tests tagged with UI_AND_API inside users_ui_and_api.robot suite and store results in separated folder.
- Execute ```pabot --testlevelsplit tests``` to run all tests in parallel and headless mode.
- Execute ```pabot --processes 8 tests``` to run all tests in parallel according to each execution splited in 8 CPU cores which will execute 8 processes at time and headless mode.

# Support:

- [expandtesting API documentation page](https://practice.expandtesting.com/notes/api/api-docs/)
- [expandtesting API demonstration page](https://www.youtube.com/watch?v=bQYvS6EEBZc)
- [PyAutoGUI](https://pypi.org/project/PyAutoGUI/)
- [pyperclip](https://pypi.org/project/pyperclip/)





- [JSONLibrary](https://robotframework-thailand.github.io/robotframework-jsonlibrary/JSONLibrary.html#library-documentation-top)
- [FakerLibrary](https://marketsquare.github.io/robotframework-faker/)
- [String](https://robotframework.org/robotframework/latest/libraries/String.html#Remove%20String)
- [OperatingSystem](https://robotframework.org/robotframework/latest/libraries/OperatingSystem.html)
- [BuiltIn](https://robotframework.org/robotframework/latest/libraries/BuiltIn.html)
- [Error regarding installing robotframework-jsonlibrary explicitly](https://blog.finxter.com/fixed-modulenotfounderror-no-module-named-robotframework-jsonlibrary/)
- [No module named 'pkg_resources'](https://cursos.alura.com.br/forum/topico-problemas-com-a-library-no-robot-339325)
- [InsecureRequestWarning: Unverified HTTPS request is being made in Robot Framework.](https://stackoverflow.com/a/45223128/10519428)
- [How can i get the Local Storage data using "Execute Javascript" Keyword in Robot Framework](https://stackoverflow.com/a/73624779/10519428)
- [How to perform a FOR loop in the Robot Framework!?](https://www.youtube.com/watch?v=j6AB2Rh4mKw)
- [Set List Value](https://robotframework.org/robotframework/latest/libraries/Collections.html#Set%20List%20Value)
- [How to use IF ELSE in Robot Framework #12](https://www.youtube.com/watch?v=NcLXjVz163A)
- [How to Use IF and ELSE in Robot Framework](https://stackoverflow.com/a/72145975/10519428)
- [Can't extract url value from ahref to variable](https://forum.robotframework.org/t/cant-extract-url-value-from-ahref-to-variable/3159/4)
- [Maximize Browser Window | Browser Library | Robot Framework](https://www.youtube.com/watch?v=c80_sJUgIXQ)
- [Examples Of Handling Checkbox Validations using the Browser Library in Robot Framework](https://www.linkedin.com/pulse/examples-handling-checkbox-validations-using-browser-library-kumar-g-jixec/)
- [Wait for Response - how to get status_code](https://forum.robotframework.org/t/wait-for-response-how-to-get-status-code/4540)
- [Fetch From Left](https://robotframework.org/robotframework/latest/libraries/String.html#Fetch%20From%20Left)
- [How to use Tags and Document your test #6](https://www.youtube.com/watch?v=bBnPFNOTkdQ)
- [Running tests in parallel](https://docs.robotframework.org/docs/parallel)
- [Browser - Timeout 10000ms on page.goto (New Page)](https://forum.robotframework.org/t/browser-timeout-10000ms-on-page-goto-new-page/825/3)
- [How to update/upgrade a package using pip?](https://stackoverflow.com/a/47071257/10519428)

# Tips:

- UI and API tests to send password reset link to user's email and API tests to verify a password reset token and reset a user's password must be tested manually as they rely on e-mail verification.
- Pabot documentation has some interesting tricks. Have a look!
- Configure a reasonable timeout and use Scroll To Element in the assertions that allows you to do so.   
- Faker e-mail keyword has presented repeated e-mails and related test fails with 409 code (conflict). Random lowercase letters were added to workaround.   
