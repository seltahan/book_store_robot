*** Settings ***
Documentation   This resource file exposes functionality from Python as keywords

Resource        ../../Resources/Config/config.robot
Library         ../../BookStore/Common/DBConnection.py      .   testuser    123@sta.com

*** Keywords ***
Verify User ${user name} exists in DB
    ${exists}=          User exists    ${user name}
    should be true      ${exists}

Check User email ${email} exists in DB
    User email exists   ${email}

Verify Book ${book name} exists in DB
    ${Exists}=          Book exists    ${book name}
    should be true      ${Exists}

Check Price ${price} exists in DB
    Price exists   ${price}