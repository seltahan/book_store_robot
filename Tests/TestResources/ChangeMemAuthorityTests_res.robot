*** Settings ***
Documentation   This resource file exposes functionality from Python as keywords

Resource        ../../Resources/Config/config.robot
Library         ../../BookStore/PageObjects/ChangeMemAuthorityPage.py   ChangeMemAuthorityPage.robot

*** Keywords ***
Open ${name} Browser on Home URL
    Open Web Browser    ${name}     ${Home URL}

Login with Username ${uname} and Password ${pwd}
    Login   ${uname}        ${pwd}

Verify admin has ${adminmenu} when logged in
    ${current url}=         get cuurent url
    should be equal         ${current url}      ${Admin Success URL}
    ${current user label}=   get user label
    should be equal         ${current user label}   ${adminmenu}

Add Login Username ${username}
    Addlogin  ${username}

Add Password ${password}
    Addpassword  ${password}

Add Level ${member}
    Addlevel  ${member}

Add First Name ${fname}
    Addfname  ${fname}

Add Last Name ${lname}
    Addlname  ${lname}

Add Email ${email}
    Addemail  ${email}


