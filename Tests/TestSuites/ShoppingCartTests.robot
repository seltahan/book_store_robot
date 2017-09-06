*** Settings ***
Documentation   This test suite covers the ShoppingCart functionality

Resource        ../TestResources/ShoppingCart_res.robot

*** Test Cases ***
Adding an item to shopping cart
    Open Edge Browser on Home URL
    Go to Sign Page
    Login with Username salma and Password salma
    Go to Home Page
    Select an item
    Click on Add to shopping cart button