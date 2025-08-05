# Client-Server-Development
CS-340 Client-Server-Development
<br/>
<br/>(From the SNHU CS-340 Syllabus)
<br/>Students will learn how to apply database systems concepts and principles to develop client/server applications that interface client-side code with databases.

# Course Competencies
This course covers the following competencies, which represent the knowledge and skills relevant to the field:
<br/>CS-30433: Apply database systems concepts and principles in the development of a client/server application
<br/>CS-30434: Create a database that can interface with client-side code
<br/>CS-30435: Develop client-side code that interfaces with databases

# Software and Tools
<br/>MongoDB: Used to store and manage animal shelter records.
<br/>Jupyter: Used for development and testing of the dashboard.
<br/>Dash / JupyterDash: Frameworks used to create the interactive dashboard.
<br/>VS Code (Optional): Recommended for editing .py files like animal_shelter.py.

# Software Test Project Overview
__Project Summary__<br/>
This is a Python dashboard built using Dash and MongoDB for Grazioso Salvare, a company that trains rescue dogs. The dashboard helps the client filter and view dogs from animal shelters in the Austin, TX area.
The dashboard was built in Jupyter Notebook and connects to a MongoDB database using a custom Python module (animal_shelter.py) that supports basic CRUD operations.
<br/>

__Features__<br/>
<br/>Filters to select Rescue Type and Outcome Type
<br/>Reset button to clear filters
<br/>Data table showing matching animal records
<br/>Pie chart showing breed distribution
<br/>Geolocation map showing selected animal's location

# How do you write programs that are maintainable, readable, and adaptable? Especially consider your work on the CRUD Python module from Project One, which you used to connect the dashboard widgets to the database in Project Two. What were the advantages of working in this way? How else could you use this CRUD Python module in the future?

For programs to be maintainable, readable, and adaptable, they need to be modular and independantly working. It also helps with readability to follow naming conventions by having clear and readable variable names along with commented descriptions and documentation. It's easy to maintain organization, especially in this project, by keeping the CRUD functions in their own moule while having the dash in another file. This keeps them modular, so they are maintainable and adaptable.

# How do you approach a problem as a computer scientist? Consider how you approached the database or dashboard requirements that Grazioso Salvare requested. How did your approach to this project differ from previous assignments in other courses? What techniques or strategies would you use in the future to create databases to meet other client requests?

As a computer scientist its important to approach a problem by understanding the requirements of the program. Identifying these requirements offer a base level of what is absolutely needed for the program to function, for example, a filter in the dash that filters the data by type. After that comes some design of the CRUD module and Dash. Then building and testing functionality.

# What do computer scientists do, and why does it matter? How would your work on this type of project help a company, like Grazioso Salvare, to do their work better?

Computer scientists take real world problems and turn them into automated solutions. In this project, we needed a way to filter data, like dogs based on breed. This is automated with a user friendly interface and CRUD logic that is capable of filtering that data in a matter of seconds. This matters because it turns hours of manual searching and spreadsheet-shuffling into seconds of interactive filtering. It reduces human error and scales as data grows.
