*** Settings ***
Resource  resource.robot
Test Setup  Create User kalle

*** Test Cases ***
Register With Valid Username And Password
    Create User  someuser  password123
    Input Login Command
    Input Credentials  someuser  password123
    Output Should Contain  Logged in

Register With Already Taken Username And Valid Password
    Input Register Command
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Register Command
    Input Credentials  u  password123
    Output Should Contain  Invalid username
    
Register With Enough Long But Invalid Username And Valid Password
    Input Register Command
    Input Credentials  Someuser  password123
    Output Should Contain  Invalid username

Register With Valid Username And Too Short Password
    Input Register Command
    Input Credentials  someuser  pass12
    Output Should Contain  Invalid password

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Register Command
    Input Credentials  someuser  passwordpassword
    Output Should Contain  Invalid password

*** Keywords ***
Create User kalle
    Create User  kalle  kalle123
    