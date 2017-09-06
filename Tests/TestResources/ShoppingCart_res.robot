*** Settings ***
Documentation   This resource file exposes functionality from Python as keywords

Resource        ../../Resources/Config/config.robot
Library         ../../BookStore/PageObjects/ShoppingCart.py        ShoppingCart.robot

*** Keywords ***
Open ${name} Browser on Home URL
    Open Web Browser    ${name}     ${Home URL}

Login with Username ${uname} and Password ${pwd}
    Login   ${uname}        ${pwd}
