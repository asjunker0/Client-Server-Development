<!--# Client-Server-Development
CS-340 Client-Server-Development
<br/>
<br/>(From the SNHU CS-340 Syllabus)
<br/>Learn how to apply database systems concepts and principles to develop client/server applications that interface client-side code with databases.

# Course Competencies
This course covers the following competencies, which represent the knowledge and skills relevant to the field:
<br/>CS-30433: Apply database systems concepts and principles in the development of a client/server application
<br/>CS-30434: Create a database that can interface with client-side code
<br/>CS-30435: Develop client-side code that interfaces with databases>-->

# Austin Animal Shelter Dashboard

A full-stack data dashboard built with Python (Dash) and MongoDB that enables 
real-time filtering and analysis of Austin Animal Center intake records.

## Features
- Dynamic filtering by rescue type and intake type using MongoDB queries
- Interactive data table with per-column search and sorting
- Breed distribution pie chart that updates with filtered results
- Geolocation map displaying animal location data
- Reset mechanism to restore the default dataset view

## Tech Stack
- **Python** — Dash, Pandas, Plotly, dash-leaflet
- **MongoDB Compass** — data storage and querying via PyMongo
- **Jupyter** — development and dashboard execution
- **VS Code** *(optional)* — recommended for editing `.py` and `.ipynb` files

# Dashboard Executions
__Unfiltered View:__
<!--<img width="975" height="402" alt="image" src="https://github.com/user-attachments/assets/391827b7-ec22-4c4b-85b6-ccf6aeda8082" />-->
<img width="1778" height="909" alt="image" src="https://github.com/user-attachments/assets/64d4af19-0885-484f-979f-0525b8012b06" />


<!--<br/> __Water Rescue Type Filtering:__
<img width="975" height="428" alt="image" src="https://github.com/user-attachments/assets/a776c775-d63a-48a5-80db-816bdee2eca5" 
<img width="1872" height="947" alt="image" src="https://github.com/user-attachments/assets/f9785fb4-583b-41be-a9a1-f93e0b9dab40" />>-->


<br/> __Mountain or Wilderness Rescue Type Filtering:__
<!--<img width="975" height="572" alt="image" src="https://github.com/user-attachments/assets/37d9e0b3-e377-4bd0-8a01-1b8844204007" />-->
<img width="1017" height="1181" alt="image" src="https://github.com/user-attachments/assets/9f9e2208-72d7-44a8-bbf9-b450d92fbf41" />


<!--<br/> __Rescue and Intake Type Filtering:__
<img width="975" height="575" alt="image" src="https://github.com/user-attachments/assets/48c3a626-3a68-44ef-97a2-34ebee3fe68f" />
<img width="1878" height="946" alt="image" src="https://github.com/user-attachments/assets/1269e334-0ed5-4025-870f-ba772127be0f" />

<!--<br/> __Pie Chart and Geolocation Widget Example:__
<img width="975" height="423" alt="image" src="https://github.com/user-attachments/assets/34ea1145-6b40-4046-a0f8-7dd9bb1675e9" />-->
<br/> __Filtering by Search: Name = "Claire"__
<img width="944" height="984" alt="image" src="https://github.com/user-attachments/assets/13824b79-e1b1-4698-a281-9fda2ccf6a00" />


<br/> __CRUD methods in python file:__</br>
<img width="783" height="646" alt="image" src="https://github.com/user-attachments/assets/c7d7b543-46f5-419e-a2eb-ba8a806df074" />

<!--<br/> __Core Backend Logic__<br/>
<br/>Developed a reusable Python CRUD module (animal_shelter.py) to abstract database operations
<br/>Implemented create, read, update, and delete functionality for MongoDB collections
<br/>Designed modular backend logic to separate data handling from UI components
<br/>Enabled scalability by allowing the dashboard to easily integrate with different datasets-->

# How to Run

### Prerequisites
- Python 3.x
- MongoDB Compass

### 1. Install Dependencies
```bash
pip install dash jupyter-dash dash-leaflet pandas pymongo plotly numpy matplotlib
```

### 2. Set Up MongoDB
- Ensure your MongoDB server is running locally
- Open MongoDB Compass — your connection string will be shown on the home screen.
  The default is:
```
  mongodb://localhost:27017
```
- If your port differs, check the Compass home screen or your MongoDB config file
  <br/>Change this if your MongoDB is running on a different port
  <br/>MONGO_PORT = 27017
  <br/>db = AnimalShelter("localhost", MONGO_PORT, "AAC", "animals")
  
- Click **"Create Database"**
  - Database Name: `AAC`
  - Collection Name: `animals`
- Select the `animals` collection, click **"Add Data" → "Import File"**
- Import `Austin_Animal_Center.csv` and select **CSV** as the file type

> For a more recent dataset, download directly from [data.austintexas.gov](https://data.austintexas.gov)

### 3. Run the Dashboard
- Ensure `animal_shelter.py` and `Dashboard.ipynb` are in the **same directory**
- Open and run `Dashboard.ipynb`
- The dashboard will be available at `http://127.0.0.1:8050/`

