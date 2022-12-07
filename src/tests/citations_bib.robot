*** Settings ***
Resource  resource.robot
Resource  form_input_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
Bib With No Citations
    Go To Bib Page
    Page Should Contain  No citations selected

Bib With Citations
    Go To Add Go To Citations Page
    Select From List By Value  name:entry_type  book
    Click Button  Submit
    Set Cite  moti2022
    Set Author  Moti Motivaatio
    Set Title  Motivaation Puute
    Set Year  2022
    Set Publisher  Motivaatio OY
    Click Button  Submit
    Go To Bib Page
    Page Should Contain  @moti2022
    Page Should Contain  author = {Moti Motivaatio}
    Page Should Contain  publisher = {Motivaatio OY}
    Page Should Contain  title = {Motivaation Puute}
    Page Should Contain  year = {2022}
