# RightCandidate

This is dynamic django CRUD app which got two pages(apps), One for applying jobs and another for displaying it with filtering appliants based on their skillsets.


- ### Application Page

  <image src="applications.JPG" height=400 width=600>
  
  This is application page(app) which takes candidate's name, email, phone number and skills and store these values to database(sqlite).
  
  
- ### Submissions Page

  <image src="submissions.JPG" height=400 width=600>  
  
  This is submission page(app) which shows the all submissions in three colour(red, yellow and green). The colour is decided by compactibility scale which is measured by the skills defined by employer with skills of apllicant that they have mentioned in application page.
  
  - If Applicant's skills matches 80% or more, then his entry will be displayed in green(most compactible).
  - If Applicant's skills matches 40% or more, then his entry will be displayed in yellow(some extent compactible).
  - If Applicant's skills matches 80% or more, then his entry will be displayed in green(least compactible).
  
  ---
  
## Resources used:
  - **Pyhton(backend)**
  - **Django(RestAPI)**
  - **HTML, CSS and Bootstrap(frontend)**
  - **SQLite(Database)**
