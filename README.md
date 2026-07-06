# spotify-studio
This is my second AP course  project as an individual in the second semester at IUST . 

<img width="950" height="500" alt="image" src="https://github.com/user-attachments/assets/86f9409e-9592-4cae-a49a-e9511ac581e3" />

# 🎵 Spotify Data Studio 
### Advanced Interactive Music Data Refinement & Analytics Toolkit

Welcome to **Spotify Data Studio**, a robust, object-oriented Data Engineering and Analytics tool built from scratch in Python. This system is designed to securely ingest raw Spotify datasets, encapsulate data into robust software objects, handle structural anomalies (missing values and outliers), and provide a dynamic Command-Line Interface (CLI) for advanced statistical analysis and data visualization.

---

## 🏗️ Project Architecture & File Structure

The project is designed with a strict modular approach to ensure clean separation of concerns, scalability, and adherence to Object-Oriented Programming (OOP) principles. 

```text
📦 Spotify-Data-Studio
├── 📂 src
│   ├── song.py                 # Core Data Model (Encapsulation & Property Validation)
│   ├── data_loader.py          # Safe File I/O, CSV parsing, and Data State Management
│   ├── data_cleaner.py         # Advanced Imputation & Outlier Handling (IQR/Z-Score)
│   ├── data_analyzer.py        # Statistical Engine (Mean, Median, Filtering, Recommendations)
│   └── data_visualizer.py      # Graphics Engine (Matplotlib plots, Heatmaps, WordClouds)
├── 📂 data
│   └── spotify_dataset.csv     # Raw input dataset
├── main.py                     # Project Executable & Interactive CLI Dashboard
└── README.md                   # Project Documentation

