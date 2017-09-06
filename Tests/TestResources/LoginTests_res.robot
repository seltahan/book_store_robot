*** Settings ***
Documentation   This resource file exposes functionality from Python as keywords

Resource        ../../Resources/Config/config.robot
Library         ../../BookStore/PageObjects/LoginPage.py        LoginPage.robot

*** Keywords ***
Open ${name} Browser on Home URL
    Open Web Browser    ${name}     ${Home URL}

Login with Username ${uname} and Password ${pwd}
    Login   ${uname}        ${pwd}

Verify user ${uname} is logged in
    ${current url}=         get cuurent url
    should be equal         ${current url}      ${Login Success URL}
    ${current user label}=   get user label
    should be equal         ${current user label}   ${uname}