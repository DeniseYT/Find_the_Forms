Find the forms from IRS website 
https://apps.irs.gov/app/picklist/list/priorFormPublication.html


Version of Python: 3.8.0


The process of running this script -

1. Test if connected and response:
<Response [200]>
We fetch the url!

2. Start from asking users few questions: 
Which form number are you looking for? 
Form W-2, Form 1095-C, Form W-3 ...etc.

3. User input 
>> Form W-2, Form 1095-C, Form W-3
note: multiple forms should be seperated by ", "

4. Next question to users
Would you like to download them? (y/n)

5. User input
>> y or n

6. Next question to users
What years are you looking for? ex.2018-2020
note: multiple forms should be seperated by "-"

7. User input
>> 2018-2020

8. Return results
Output JSON
For example:
[{'form_number': 'Form W-2',
  'form_title': 'Wage and Tax Statement (Info Copy Only)',
  'max_year': '2022',
  'min_year': '1954'},

   {'form_number': 'Form 1095-C',
  'form_title': 'Employer-Provided Health Insurance Offer and Coverage',
  'max_year': '2022',
  'min_year': '2014'}]

9. Download PDF files to a subdirectory under my main directory, and follow by "Form Name - Year" -> "Form W-2" or "Form 1095-C"
Return below information
Searching Form W-2 from here: https://apps.irs.gov/app/picklist/list/priorFormPublication.html?value=Form+W-2&criteria=formNumber&submitSearch=Find
downloading now for 2020
downloading now for 2019
downloading now for 2018

Searching Form 1095-C from here: https://apps.irs.gov/app/picklist/list/priorFormPublication.html?value=Form+1095-C&criteria=formNumber&submitSearch=Find
downloading now for 2020
downloading now for 2019
downloading now for 2018

Completed

