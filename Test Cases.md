Test Cases

## 1. Introduction
This document contains test cases for the Railway Reservation Analyzer Python project. The purpose is to verify that all project features work correctly.

## 2. Test Cases

| Test Case ID | Test Scenario | Input | Expected Result |
|---|---|---|---|
| TC01 | Load CSV file | Valid bookings.csv | Data should load successfully |
| TC02 | Missing CSV file | File not available | Display file not found error |
| TC03 | Empty CSV file | Empty bookings.csv | Display empty file error |
| TC04 | Valid fare | Fare = 1500 | Fare should be accepted |
| TC05 | Invalid fare | Fare = ABC | Row should be skipped with warning |
| TC06 | Missing Train | Train is empty | Record should be removed |
| TC07 | Missing Status | Status is empty | Record should be removed |
| TC08 | Bookings per train | Multiple train records | Display train-wise booking count |
| TC09 | Revenue calculation | Confirmed tickets | Calculate confirmed revenue correctly |
| TC10 | Waiting status | Status = Waiting | Count waiting tickets |
| TC11 | Cancelled status | Status = Cancelled | Count cancelled tickets |
| TC12 | Invalid menu choice | Choice = 5 | Display invalid choice message |
| TC13 | Exit program | Choice = 3 | Display thank you message and exit |
| TC14 | Graph generation | Valid booking data | Display bar charts correctly |

## 3. Sample Test Data

Create a file named `bookings.csv`:

```csv
PNR,Train,Class,Fare,Status
123456,Rajdhani Express,AC,1500,Confirmed
123457,Shatabdi Express,Sleeper,800,Waiting
123458,Duronto Express,AC,1200,Cancelled
123459,Rajdhani Express,AC,1800,Confirmed
123460,Shatabdi Express,Sleeper,900,Confirmed
```

## 4. Expected Results

- Total valid bookings: 5
- Rajdhani Express bookings: 2
- Shatabdi Express bookings: 2
- Duronto Express bookings: 1
- Confirmed tickets: 3
- Waiting tickets: 1
- Cancelled tickets: 1
- Total confirmed revenue: Rs. 4200

## 5. Conclusion

The test cases help verify the functionality, accuracy, and reliability of the Railway Reservation Analyzer. The project should successfully process valid booking records, handle invalid data, calculate revenue, and generate graphs.