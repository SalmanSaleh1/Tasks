*** Settings ***
Library  SeleniumLibrary
Library  OperatingSystem
Library  String
Library  Collections  # Import the Collections library

*** Variables ***
${BROWSER}        Chrome
${URL}            https://www.automationexercise.com/login
${LOGIN_BUTTON}   xpath=//button[@data-qa='login-button']
${USERNAME_FIELD}  xpath=//input[@data-qa='login-email']
${PASSWORD_FIELD}  xpath=//input[@data-qa='login-password']
${CSV_FILE}       resources/Data2.csv

*** Test Cases ***
Login with Users From CSV
    ${users}=  Read CSV  ${CSV_FILE}
    FOR  ${user}  IN  @{users}
        Login To Website  ${user[0]}  ${user[1]}
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
