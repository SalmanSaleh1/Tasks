*** Settings ***
Library  SeleniumLibrary
Library  OperatingSystem
Library  String
Library  Collections

*** Variables ***
${BROWSER}        Chrome
${URL}            https://www.saucedemo.com/v1


${USERNAME_FIELD}    //*[@id='user-name']
${PASSWORD_FIELD}   //*[@id='password']
${LOGIN_BUTTON}    //*[@id='login-button']
${Products}    //*[text()='Products']

${cart_image}      xpath=//a[contains(@class, 'shopping_cart_link')]
${Checkout_button}    //*[text()='CHECKOUT']

${Checkout_page}    //*[text()='Checkout: Your Information']

*** Keywords ***

Open Driver
    Open Browser  ${URL}  ${BROWSER}

Close Driver
    Close Browser    ${URL}  ${BROWSER}

Login with validate
    Input Text    ${USERNAME_FIELD}    standard_user
    Input Text    ${PASSWORD_FIELD}    secret_sauce
    Sleep    2s
    Click Button  ${LOGIN_BUTTON}
    Sleep    2s
    Wait Until Element Is Visible    ${Products}

Search for Item and add it to cart
    Wait Until Element Is Visible    //div[text()='Sauce Labs Bolt T-Shirt']/ancestor::div[@class='inventory_item']//button
    Click Button  //div[text()='Sauce Labs Bolt T-Shirt']/ancestor::div[@class='inventory_item']//button
    Sleep    2s

Click in cart and checkout
    Click Element    ${cart_image}
    Wait Until Element Is Visible    ${Checkout_button}
    Sleep    2s
    Click Element    ${Checkout_button}
    Wait Until Element Is Visible   ${Checkout_page}
    Sleep    2s

Fill Checkout page information
    Wait Until Element Is Visible   //*[text()='Checkout: Your Information']
    Input Text    //*[@id='first-name']    Salman
    Sleep    2s
    Input Text    //*[@id='last-name']    Saleh
    Sleep    2s
    Input Text    //*[@id='postal-code']    28383
    Sleep    2s
    Click Element    //*[@value='CONTINUE']
    
Validate the order and Finish Order 
    Wait Until Element Is Visible   //*[text()='Checkout: Overview']
    Wait Until Element Is Visible   //*[text()='Sauce Labs Bolt T-Shirt']
    Click Element    //*[text()='FINISH']
    Sleep    2s
    Click Element    //*[text()='THANK YOU FOR YOUR ORDER']
    Sleep    2s

*** Test Cases ***

Full Scenario To Choose an item and finish the order
    Open Driver
    Login with validate
    Search For Item And Add It To Cart
    Click In Cart And Checkout
    Fill Checkout Page Information
    Validate The Order And Finish Order
