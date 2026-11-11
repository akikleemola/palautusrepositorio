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

Register With Password Containing Numbers
    Set Username  pauli
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click  button >> text=Register
    Register Should Succeed

Register With Password Containing Special Characters
    Set Username  pirkko
    Set Password  kalle#abc
    Set Password Confirmation  kalle#abc
    Click  button >> text=Register
    Register Should Succeed

Register With Matching Password Confirmation
    Set Username  sami
    Set Password  sami1234
    Set Password Confirmation  sami1234
    Click  button >> text=Register
    Register Should Succeed

Register With Nonmatching Password Confirmation
    Set Username  sanna
    Set Password  sanna1234
    Set Password Confirmation  sanna5678
    Click  button >> text=Register
    Register Should Fail With Message  Passwords do not match

Register With Password Containing Only Lowercase Letters
    Set Username  laura
    Set Password  kallekalle
    Set Password Confirmation  kallekalle
    Click  button >> text=Register
    Register Should Fail With Message  Password must contain a number or a special character

Register With Password Containing Only Uppercase And Lowercase Letters
    Set Username  Liisa
    Set Password  KalleKalle
    Set Password Confirmation  KalleKalle
    Click  button >> text=Register
    Register Should Fail With Message  Password must contain a number or a special character

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
