# 🚆 Railway Reservation Analyzer
## Project Details
- **Project Number:** 61
- **Language:** Python 3
- **Developer:** Mayank Dongre
- **ERP:** RU-26-02389

## Project Mentor
- **Mentored by:** Mr. Satyaprakash Sethy
- **Github:** @SATYAPRAKASHSETHY
- **Role:** Python Mentor/ Technical guide

## 📌 Project Description
Railway Reservation Analyzer is a Python-based data analysis project that analyzes railway booking records using a CSV file. It helps calculate train-wise bookings, confirmed ticket revenue, and ticket status summaries.

## 🎯 Features
- **Bookings Per Train:** Counts the total bookings for each train.
- **Revenue Per Train:** Calculates total revenue from confirmed tickets.
- **Ticket Status Summary:** Displays Confirmed, Waiting, and Cancelled ticket counts.
- **Data Validation:** Detects invalid fares and missing train or status values.
- **Data Visualization:** Displays bar charts using Matplotlib.
- **Interactive Menu:** Allows users to select different analysis options.

## 🛠️ Technologies Used
- Python
- Pandas
- Matplotlib
- CSV File Handling

## 📂 Project Structure

```text
Railway-Reservation-Analyzer/
│
├── main.py
├── bookings.csv
└── README.md
```

## ⚙️ Requirements

Install Python 3 and the required libraries:

```bash
pip install pandas matplotlib
```

## ▶️ How to Run the Project

1. Download or clone the project.
2. Open the project folder in VS Code.
3. Make sure `main.py` and `bookings.csv` are in the same folder.
4. Open the terminal.
5. Run the following command:

```bash
python3 main.py
```

## 📊 Main Menu

```text
==============================
 RAILWAY RESERVATION ANALYZER
==============================

===== MAIN MENU =====
1. Bookings per train
2. Revenue per train
3. Exit

Enter your choice:
```

## 📄 CSV File Format

The `bookings.csv` file should contain these columns:

| PNR | Train | Class | Fare | Status |
|---|---|---|---|---|
| 123456 | Rajdhani Express | AC | 1500 | Confirmed |
| 123457 | Shatabdi Express | Sleeper | 800 | Waiting |
| 123458 | Duronto Express | AC | 1200 | Cancelled |

## 📈 Expected Output

- Total bookings per train.
- Total confirmed revenue per train.
- Ticket status summary.
- Bar charts for bookings and revenue.

## 🎓 Learning Outcomes

Through this project, I learned:
- Python functions and loops.
- Conditional statements.
- Exception handling.
- CSV file handling.
- Data cleaning using Pandas.
- Data visualization using Matplotlib.

## 👨‍💻 Author
**Student Project**

## 📝 Conclusion
The Railway Reservation Analyzer makes railway booking data easier to understand by providing useful statistics and graphical representations. It demonstrates the practical use of Python for data analysis.
