*** Settings ***
Documentation   This test suite covers the Admin functionality

Resource        ../TestResources/ChangeMemAuthorityTests_res.robot
Resource        ../../BookStore/RobotResources/DataBase_res.robot

*** Test Cases ***
Login with Admin User
    Open Edge Browser on Home URL
    Go to Admin Page
    Login with Username admin and Password admin
    sleep   3s
    Verify admin has Administration Menu when logged in
    close web browser


Add New Member
    Open Edge Browser on Home URL
    Go to Admin Page
    Login with Username admin and Password admin
    Click on memebers link
    Click on insert member link
    Add Login Username salma
    Add Password salma
    Add Level Member
    Add First Name salma
    Add Last Name Mosaad
    Add Email salmamosaad@yahoo.com
    Click on insert button
    close web browser

Verify User existence in DB
    open db connection
    Verify User salma exists in DB
    Check User email salmamosaad@yahoo.com exists in DB
    Close database connection

Change Member Authority
    Click on member info
    Click on login name
    Add Password salma
    Add Level Administrator
    Click on update button
    Click on member info
    close web browser
