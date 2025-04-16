# 🩺 Diabetes Xplorer

**Diabetes Xplorer** is an interactive data visualization dashboard built using **Preswald**, designed to explore and analyze the popular `diabetes.csv` dataset. It allows users to view data summaries, filter by glucose level, and visualize relationships in the data through charts and statistics.

---

## 📊 Features

- ✅ Load and preview the diabetes dataset from CSV.
- 📋 Summary statistics for each numeric column.
- 🔘 Interactive slider to filter records by **Glucose** level.
- 📈 Scatter plot comparing **Glucose vs. BMI** colored by outcome.
- 📊 Histogram showing **BMI distribution**.
- 🥧 Pie chart representing the distribution of diabetes outcomes.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| [Preswald](https://preswald.com) | Python-based UI framework for data apps |
| Pandas | Data manipulation and analysis |
| Plotly Express | Interactive charts and graphs |

---

## 📂 Project Structure
diabetes-xplorer/
│
├── data/
│   └── diabetes.csv           # Dataset used for analysis
│
├── main.py                    # Main dashboard logic and UI
├── preswald.toml              # Project configuration file
├── README.md                  # You're here!
│
└── images/
    ├── logo.png               # (Optional) Logo for dashboard
    └── favicon.ico            # (Optional) Favicon


---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/diabetes-xplorer.git
cd diabetes-xplorer
```

### 2. Install Preswald
Make sure Python 3.8+ is installed. Then run:

```bash
pip install preswald
```

### 3. Folder Setup
Ensure your dataset diabetes.csv is inside a folder called data/
```
data/
└── diabetes.csv
```

## ⚙️ preswald.toml Configuration
Your preswald.toml should look like this:
```
[project]
title = "Diabetes Explorer"
entrypoint = "main.py"
port = 8501
slug = "diabetes-app"

[branding]
name = "Diabetes Data Dashboard"
logo = "images/logo.png"
favicon = "images/favicon.ico"
primaryColor = "#3498db"

[data.diabetes]
type = "csv"
path = "data/diabetes.csv"

[logging]
level = "INFO"
format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

```


### 🚀 Running the App
To launch the dashboard:

```bash
preswald run
```
Then open your browser and navigate to:
```arduino
http://localhost:8501
```
