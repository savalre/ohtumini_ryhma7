*** Settings ***
Resource  resource.robot
Resource  form_input_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
Open Add Book Page
    Go To Add Book Page
    Add Book Page Should Be Open

Invalid Form Does Not Submit
    Go To Add Book Page
    Click Button  Submit
    Add Book Page Should Be Open

Valid Form Sumbits
    Go To Add Book Page
    Set Cite  Book
    Set Author  Moti Motivaatio
    Set Title  Motivaation Puute
    Set Year  2022
    Set Publisher  Motivaatio OY
    Click Button  Submit
    Add Book Page Should Be Open
    Go To Citations Page
    Page Should Contain  @Book
    Page Should Contain  author: { Moti Motivaatio }
    Page Should Contain  publisher: { Motivaatio OY }
    Page Should Contain  title: { Motivaation Puute }
    Page Should Contain  year: { 2022 }
