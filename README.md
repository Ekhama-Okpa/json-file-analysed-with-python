# json-file-analysed-with-python
**Extracting data from a JSON file using Python.**

Through a data unification algorithm, the the tech team at Daikibo converted all telemetry data collected from its 4 factories.

Each factory has 9 types of machines sending a message every 10 minutes. 

Daikibo collected this data for a month and it's contents were shared in the form of a JSON file.

The telemetry data was collected to answer the questions:
Which location did machines break the most?
What are the machines that broke most often in that location?

The structure of the data in the JSON file is shown below:
{    
    "deviceID": "19ff3161-2b3a-40a3-8604-bdc6532d0dab",
    "deviceType": "CNC",
    "timestamp": 1619816400000,
    "location": {
        "country": "japan",
        "city": "tokyo",
        "area": "keiyō-industrial-zone",
        "factory": "daikibo-factory-meiyo",
        "section": "section-1"
        },
    "data": {
        "status": "healthy",
        "temperature": 27
        }
}

I used Python to extract this information. Below is the link to the full JSON file:
https://drive.google.com/file/d/1D9VVjPhHaPU-lteTPAWqM9_var43q_El/view?usp=sharing
