*** Settings ***
Documentation   This test suite covers the Login functionality.

Resource        ../TestResources/LoginTests_res.robot

*** Test Cases ***
Login with Admin User
    Open Edge Browser on Home URL
    Go to Login Page
    Login with Username admin and Password admin
    sleep   3s
    Verify user admin is logged in
    close web browser