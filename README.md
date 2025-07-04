🎯 3D Printer Analytics Project
This project explores operational efficiency in a 3D printing construction marketplace using real-world-inspired data.
It features a complete data pipeline — from ETL and data modeling to interactive Power BI dashboards — to analyze printer performance, optimize parameters and identify trends.

📌 Tools: Python, Pandas, Jupyter, Power BI
📈 Dashboards: Success Rate by Printer Model, Duration vs Layer Height, Avg Speed
📂 Includes: Cleaned dataset, ETL scripts, notebook, .pbix file and project summary.
🔍 Ideal for roles in: Data Analytics, Supply Chain, Manufacturing Intelligence

👉 Perfect for demonstrating your skills in analytics, visualization and supply chain data storytelling
# 🛠️ 3D Printer Analytics for Construction Marketplace

Welcome to a real-world analytics project designed to simulate how data-driven decision-making can optimize product performance in a **3D printing construction marketplace**. This end-to-end project demonstrates data cleaning, ETL automation, Jupyter analysis and Power BI dashboards.

---

## 📌 Project Objective

To analyze the performance of various 3D printer models by understanding the relationship between print parameters (speed, temperature, layer height) and key outcomes like **success rate** and **print duration** — enabling better product selection, process tuning and supply chain insight.

---

## 🚀 Key Features

- ✅ Realistic dataset of 3D printer performance
- ✅ Automated ETL process using Python
- ✅ End to End SQL queries for Product KPI
- ✅ Jupyter notebook for EDA & correlation analysis
- ✅ 📊 Power BI dashboard with 3 dynamic visuals
- ✅ Clean GitHub structure for portfolio showcase

## 🧾 Dataset Overview

| Column Name     | Description                            |
|-----------------|----------------------------------------|
| printer_model   | Printer type used (e.g., Ender 3, MK3) |
| layer_height    | Layer height in mm                     |
| print_speed     | Speed in mm/s                          |
| nozzle_temp     | Nozzle temperature (°C)                |
| bed_temp        | Bed temperature (°C)                   |
| print_duration  | Total duration of the print (minutes)  |
| print_time      | Timestamp of the job                   |
| success         | 1 = Successful print, 0 = Failed       |


## ⚙️ ETL Process (Python)

Run the Python script to:
- Load the raw dataset
- Clean and preprocess
- Group by printer model
- Generate a summary CSV of success rate, average duration and layer height
