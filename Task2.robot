*** Settings ***
Library  SeleniumLibrary
Library  OperatingSystem
Library  String
Library  Collections

*** Variables ***
${BROWSER}        Chrome
${URL}            https://www.automationexercise.com/login
${LOGIN_BUTTON}   xpath=//button[@data-qa='login-button']
${USERNAME_FIELD}  xpath=//input[@data-qa='login-email']
${PASSWORD_FIELD}  xpath=//input[@data-qa='login-password']
${CSV_FILE}       resources/Data2.csv

*** Test Cases ***
Login with Valid Users
    ${users}=  Read CSV  ${CSV_FILE}
    FOR  ${user}  IN  @{users}
        ${username}=  Get From List  ${user}  0
        ${password}=  Get From List  ${user}  1
        ${valid}=  Get From List  ${user}  2
        Run Keyword If  '${valid}' == 'True'  Login To Website  ${username}  ${password}
    END

Login with Invalid Users
    ${users}=  Read CSV  ${CSV_FILE}
    FOR  ${user}  IN  @{users}
        ${username}=  Get From List  ${user}  0
        ${password}=  Get From List  ${user}  1
        ${valid}=  Get From List  ${user}  2
        Run Keyword If  '${valid}' == 'False'  Login To Website  ${username}  ${password}
    END

*** Keywords ***
Read CSV
    [Arguments]  ${file_path}
    ${content}=  Get File  ${file_path}
    ${lines}=  Split String  ${content}  \n
    ${csv_data}=  Create List
    FOR  ${line}  IN  @{lines}
        ${fields}=  Split String  ${line}  ,
        Append To List  ${csv_data}  ${fields}
    END
    [Return]  ${csv_data}

Login To Website
    [Arguments]  ${username}  ${password}
    Open Browser  ${URL}  ${BROWSER}
    Input Text  ${USERNAME_FIELD}  ${username}
    Input Text  ${PASSWORD_FIELD}  ${password}
    Click Button  ${LOGIN_BUTTON}
    sleep  2s
    Close Browser
