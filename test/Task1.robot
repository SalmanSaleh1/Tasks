*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${BROWSER}        Chrome
${URL}            https://the-internet.herokuapp.com/login
${USERNAME}       tomsmith
${PASSWORD}       SuperSecretPassword!
${LOGIN_BUTTON}   xpath=//button[@type='submit']
${USERNAME_FIELD}  xpath=//input[@id='username']
${PASSWORD_FIELD}  xpath=//input[@id='password']
${SUCCESS_MSG}    xpath=//div[@id='flash' and contains(@class, 'success')]


*** Test Cases ***
Login To Web Application
    Open Browser  ${URL}  ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible  ${USERNAME_FIELD}  10s
    Input Text  ${USERNAME_FIELD}  ${USERNAME}
    Sleep    1s
    Input Text  ${PASSWORD_FIELD}  ${PASSWORD}
    Sleep    1s
    Click Button  ${LOGIN_BUTTON}
    Wait Until Element Is Visible  ${SUCCESS_MSG}  10s
    Sleep    1s
    Element Should Be Visible  ${SUCCESS_MSG}
    Close Browser
