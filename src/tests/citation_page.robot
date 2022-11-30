*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
Open Citation Page
    Go To Citations Page
    Citations Page Should Be Open

*** Keywords ***
Citations Page Should Be Open
    Page Should Contain  List of citations