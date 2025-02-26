*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${BROWSER}        Chrome
${URL}            https://www.automationexercise.com/login
${LOGIN_BUTTON}   xpath=//button[@data-qa='login-button']
${USERNAME_FIELD}  xpath=//input[@data-qa='login-email']
${PASSWORD_FIELD}  xpath=//input[@data-qa='login-password']
${SUCCESS_PAGE}   xpath=//*[contains(text(),'Logged in as')]  # XPath for the "Logged in as" text

*** Test Cases ***
Login with Valid User
    Open Browser  ${URL}  ${BROWSER}
    Input Text  ${USERNAME_FIELD}  validuse77r@example.com
    Input Text  ${PASSWORD_FIELD}  123123
    Click Button  ${LOGIN_BUTTON}
    sleep  2s
    Wait Until Element Is Visible    //*[text()=' Logged in as ']
    Close Browser

Login with Invalid User
    Open Browser  ${URL}  ${BROWSER}
    Input Text  ${USERNAME_FIELD}  invaliduser@example.com
    Input Text  ${PASSWORD_FIELD}  invalidpassword
    Click Button  ${LOGIN_BUTTON}
    sleep  2s
    Wait Until Element Is Visible    //*[text()='Your email or password is incorrect!']
    Close Browser
