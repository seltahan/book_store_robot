*** Settings ***
Documentation   This resource file exposes functionality from Python as keywords

Resource        ../../Resources/Config/config.robot
Library         XML
Library         ../../BookStore/PageObjects/AdminPage.py        AdminPage.robot

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

Add members from file ${file name}
    ${data}=        Parse XML       Tests\\TestResources\\${file name}
    @{Users}=       Get Elements    ${data}   user
    :FOR            ${user}     IN      @{Users}
    \               sleep               3s
    \               ${username}=        Get Element Text    ${user}     name
    \               ${email}=           Get Element Text    ${user}     email
    \               ${password}=        Get Element Text    ${user}     password
    \               ${level}=           Get Element Text    ${user}     level
    \               ${fname}=           Get Element Text    ${user}     fname
    \               ${lname}=           Get Element Text    ${user}     lname
    \               Click on insert member link
    \               Add Login Username ${username}
    \               Add Password ${password}
    \               Add Level ${level}
    \               Add First Name ${fname}
    \               Add Last Name ${lname}
    \               Add Email ${email}
    \               Click on insert button

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

Add Title ${title}
    Addtitle  ${title}

Add Price ${price}
    Addprice  ${price}

