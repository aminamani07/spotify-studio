# spotify-studio
This is my second AP course  project as an individual in the second semester at IUST . 

<img width="950" height="500" alt="image" src="https://github.com/user-attachments/assets/86f9409e-9592-4cae-a49a-e9511ac581e3" />

############################################################################################################
#                                                                              #
# 🎵 SPOTIFY DATA STUDIO                                                       #
# Advanced Interactive Music Data Refinement & Analytics Toolkit               #
#                                                                              #

Welcome to Spotify Data Studio, a robust, object-oriented Data Engineering and 
Analytics tool built from scratch in Python. This system is designed to securely 
ingest raw Spotify datasets, encapsulate data into robust software objects, handle 
structural anomalies (missing values and outliers), and provide a dynamic 
Command-Line Interface (CLI) for advanced statistical analysis and data visualization.

================================================================================
## 🏗️ PROJECT ARCHITECTURE & FILE STRUCTURE
================================================================================

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



⚠️ NOTE ON FILE STRUCTURE: 
The main executable engine (main.py) is purposefully kept outside the source 
(src/) directory to maintain a clean root entry point for execution.

================================================================================
## 🚀 KEY FEATURES
================================================================================

### 1. Robust Data Encapsulation (song.py)
------------------------------------------
• Strictly manages song attributes via Python @property decorators.
• Implements hard validation guards for core metrics (e.g., popularity, 
  danceability, and energy must fall within legal analytical thresholds).

### 2. Advanced Data Pipeline & Cleaning (data_cleaner.py)
----------------------------------------------------------
• Missing Value Imputation: Implements custom fallback engines including 
  MeanImputer, MedianImputer, and multi-attribute KNNImputer.
• Outlier Mitigation: Prevents analytical skewing using IQROutlierHandler 
  (Interquartile Range) and ZScoreOutlierHandler boundaries to clamp extreme 
  variations.

### 3. Comprehensive Analytics & Recommendation Engine (data_analyzer.py)
--------------------------------------------------------------------------
• Computes exact descriptive statistics (Mean, Median, Min, Max) bypassing 
  missing entries safely.
• Offers deep-filtering constraints by specific artists or genres.
• Built-in content-based proximity metric to recommend similar tracks based on 
  numeric audio profiles.

### 4. Interactive Data Visualization (data_visualizer.py)
----------------------------------------------------------
• Generates clear, publication-grade distribution visualizer
