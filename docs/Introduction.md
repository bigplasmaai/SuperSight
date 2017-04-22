# Introduction
 
## What is SuperSight ?
 
SuperSight is made to display Matplotlib plots and Pandas data tables within a static HTML report. This report (we could also call it a website) is composed of several sections which can be used to organize topics and subjects.
 
Each section can contain one or several pages.
These pages will then contain plots and data tables.  Both are elements of the page. You can enrich elements with headings, comments and math equations.
 
Below is a simplified view of the HTML result :
 
Report
|
|---Section 1
|     |---Page 1
|     |---Page 2
|
|---Section 2
|     |---Page 1
|     |---Page 2
|           |---Plot 1
|           |---Plot 2 (with one below comment)
|           |---Data Table 1
|           |---Plot 3 (with one headings)
 
## Features
 
Static output (folders and files) hence no need of a web server to host it
Generates a tree of folders according to your sections (one folder by section).
Multi sections/pages to allow analysts to structure their ideas
Natively works with Matplotlib and Pandas
Plots are saved as files in dedicated section folder.
Possibility to insert external SVGs (for compagnies logos ...)
HTML template built on the top of Bootstrap 4 hence easily customizable
Possibility to choose a custom theme/template at render time
 
## Use Case
 
SuperSight can be used as the final step of your data analysis. It allows to present your plots and to report
