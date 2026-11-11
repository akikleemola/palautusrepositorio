*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  maija
    Set Password  maija1234
    Set Password Confirmation  maija1234
    Click  button >> text=Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ab
    Set Password  maija1234
    Set Password Confirmation  maija1234
    Click  button >> text=Register
    Register Should Fail With Message  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  maija
    Set Password  maija12
    Set Password Confirmation  maija12
    Click  button >> text=Register
    Register Should Fail With Message  Password must be at least 8 characters long

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  toinen123
    Set Password Confirmation  toinen123
    Click  button >> text=Register
    Register Should Fail With Message  Username is already in use

*** Keywords ***
Register Should Succeed
    Get Title  ==  Welcome to Ohtu Application!

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle1234
    Go To Register Page

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Get Text  body  *=  ${message}
