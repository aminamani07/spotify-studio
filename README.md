# spotify-studio
This is my second AP course  project as an individual in the second semester at IUST . 

<img width="950" height="500" alt="image" src="https://github.com/user-attachments/assets/86f9409e-9592-4cae-a49a-e9511ac581e3" />

################################################################################
#                                                                              #
# 🎵 SPOTIFY DATA STUDIO                                                       #
# ######################                                                       #
# Advanced Interactive Music Data Refinement & Analytics Toolkit               #
#                                                                              #
################################################################################

Welcome to Spotify Data Studio, a robust, object-oriented Data Engineering and 
Analytics tool built from scratch in Python[span_0](start_span)[span_0](end_span). This system is designed to securely 
ingest raw Spotify datasets, encapsulate data into robust software objects, handle 
structural anomalies (missing values and outliers), and provide a dynamic 
Command-Line Interface (CLI) for advanced statistical analysis and data visualization[span_1](start_span)[span_1](end_span).

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
• Strictly manages song attributes via Python @property decorators[span_2](start_span)[span_2](end_span)[span_3](start_span)[span_3](end_span).
• Implements hard validation guards for core metrics (e.g., popularity, 
  danceability, and energy must fall within legal analytical thresholds)[span_4](start_span)[span_4](end_span)[span_5](start_span)[span_5](end_span).

### 2. Advanced Data Pipeline & Cleaning (data_cleaner.py)
----------------------------------------------------------
• Missing Value Imputation: Implements custom fallback engines including 
  MeanImputer, MedianImputer, and multi-attribute KNNImputer[span_6](start_span)[span_6](end_span)[span_7](start_span)[span_7](end_span).
• Outlier Mitigation: Prevents analytical skewing using IQROutlierHandler 
  (Interquartile Range) and ZScoreOutlierHandler boundaries to clamp extreme 
  variations[span_8](start_span)[span_8](end_span)[span_9](start_span)[span_9](end_span).

### 3. Comprehensive Analytics & Recommendation Engine (data_analyzer.py)
--------------------------------------------------------------------------
• Computes exact descriptive statistics (Mean, Median, Min, Max) bypassing 
  missing entries safely[span_10](start_span)[span_10](end_span).
• Offers deep-filtering constraints by specific artists or genres[span_11](start_span)[span_11](end_span)[span_12](start_span)[span_12](end_span).
• Built-in content-based proximity metric to recommend similar tracks based on 
  numeric audio profiles[span_13](start_span)[span_13](end_span).

### 4. Interactive Data Visualization (data_visualizer.py)
----------------------------------------------------------
• Generates clear, publication-grade distribution visualizer
