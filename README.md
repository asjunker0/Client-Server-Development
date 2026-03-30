# Client-Server-Development
CS-340 Client-Server-Development
<br/>
<br/>(From the SNHU CS-340 Syllabus)
<br/>Learn how to apply database systems concepts and principles to develop client/server applications that interface client-side code with databases.

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

# Client Server Project Overview
__Project Summary__<br/>
Built a full-stack data dashboard using Python (Dash) and MongoDB to help a client filter and analyze animal shelter data in real time.
Implemented a custom Python CRUD module to handle database interactions and support dynamic filtering, visualization, and geolocation features.
<br/>

__Features__
<br/>Implemented dynamic filtering for rescue and outcome types using MongoDB queries
<br/>Built an interactive data table to display filtered results in real time
<br/>Developed data visualizations including breed distribution (pie chart)
<br/>Integrated geolocation mapping to display animal locations
<br/>Designed a reset mechanism to restore default dataset state

# Dashboard Executions
__Unfiltered View:__
<img width="975" height="402" alt="image" src="https://github.com/user-attachments/assets/391827b7-ec22-4c4b-85b6-ccf6aeda8082" />

<br/> __Water Rescue Type Filtering:__
<img width="975" height="428" alt="image" src="https://github.com/user-attachments/assets/a776c775-d63a-48a5-80db-816bdee2eca5" />

<br/> __Mountain or Wilderness Rescue Type Filtering:__
<img width="975" height="572" alt="image" src="https://github.com/user-attachments/assets/37d9e0b3-e377-4bd0-8a01-1b8844204007" />

<br/> __Disaster or Individual Tracking Type Filtering:__
<img width="975" height="575" alt="image" src="https://github.com/user-attachments/assets/48c3a626-3a68-44ef-97a2-34ebee3fe68f" />

<br/> __Reset Button Clicked:__
<img width="975" height="630" alt="image" src="https://github.com/user-attachments/assets/e3d73db2-2339-4c5c-bec1-23c305ec13b5" />

<br/> __Pie Chart and Geolocation Widget Example:__
<img width="975" height="423" alt="image" src="https://github.com/user-attachments/assets/34ea1145-6b40-4046-a0f8-7dd9bb1675e9" />

<br/> __CRUD methods in python file:__</br>
<img width="783" height="646" alt="image" src="https://github.com/user-attachments/assets/c7d7b543-46f5-419e-a2eb-ba8a806df074" />

<br/> __Core Backend Logic__<br/>
* Developed a reusable Python CRUD module (animal_shelter.py) to abstract database operations
* Implemented create, read, update, and delete functionality for MongoDB collections
* Designed modular backend logic to separate data handling from UI components
* Enabled scalability by allowing the dashboard to easily integrate with different datasets

# How to Run
- Ensure MongoDB Compass is installed
- Install dependencies in bash:
- ```pip install dash pandas pymongo plotly jupyter dash-leaflet```
- Ensure MongoDB server is running
- Open Compass and connect to your local host
- ```mongodb://localhost:yourport```
- Click "Create Database"
- Name Database: ```AAC```
- Name Collection: ```animals```
- Import dataset ```Austin_Animal_Center.csv``` (For a more recent dataset, download directly from ```data.austintexas.gov```)
- 

