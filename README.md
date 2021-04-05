# Automated Ticketing System for a Parking Lot
Create an automated ticketing system which can holds up 'n' number of car. Each slot starts with 1 and increment with the incresaing distance.
When a car enters the parking area, ticket should be issued to the driver and we have to store some information:
1) Registration Number of the vehicle and Age of the driver.
2) Allocate a spot to vehicle and allocation should be done on the basis of nearest available spot.
3) After exit, we should be able to track which slot is available now.

## 1. Approach 
1) Initialize two class for vehicle and parking area and sets up the required information like, registration number, age of driver, parking spots etc.
2) Storing the information of registration number and driver age into a dictionary corresponding to the spots in which the vehicle is parked.
3) Execute commands to get expected Results.

## 2. Flowchart
Created a basic flowchart - flowchart.svg

## 3. Command to run the assignment in Terminal
``` 
python3 parking_processing.py
```
This will take a file as an input and return response in an another file.
## 4.  Unit Test Cases

- Total number of test cases - 8
- Code coverage - 87%

   #### command to run unit test cases in terminal
    ``` 
    python3 -m unittest test.py
    ```
    This will take a file as input and return response in an another file.
    
## 5.  Docker Deployment
- Build a docker image
    ``` 
    sudo docker build -t <image-tag> -f Dockerfile .
    ```
- deploy the container
    ``` 
    sudo docker run --rm -it -d --name parking_lot <image-id>
    ```
- Running File and test cases
    ``` 
    sudo docker exec -it <container-id> python3 parking_processing.py
    ```
    ``` 
    sudo docker exec -it <container-id> python3 test.py
    ```
