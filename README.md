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


⚠️ Note on File Structure: The main executable engine (main.py) is purposefully kept outside the source (src/) directory to maintain a clean root entry point for execution.

### 🚀 Key Features

1. Robust Data Encapsulation (song.py)

• Strictly manages song attributes via Python @property decorators.

• Implements hard validation guards for core metrics (e.g., popularity, danceability, and energy must fall within legal analytical thresholds).


2. Advanced Data Pipeline & Cleaning (data_cleaner.py)

• Missing Value Imputation: Implements custom fallback engines including MeanImputer, MedianImputer, and multi-attribute KNNImputer.

• Outlier Mitigation: Prevents analytical skewing using IQROutlierHandler (Interquartile Range) and ZScoreOutlierHandler boundaries to clamp extreme variations.


3. Comprehensive Analytics & Recommendation Engine (data_analyzer.py)

• Computes exact descriptive statistics (Mean, Median, Min, Max) bypassing missing entries safely.

• Offers deep-filtering constraints by specific artists or genres.

• Built-in content-based proximity metric to recommend similar tracks based on numeric audio profiles.


4. Interactive Data Visualization (data_visualizer.py)

• Generates clear, publication-grade distribution visualizers (Box Plots for pre/after cleaning comparisons).

• Creates automated feature relations using Scatter Plots.

• Computes full Audio Feature Correlation Matrices rendered with dynamic coolwarm heatmaps and clean text annotations.



### 🛠️ Installation & Setup
### Prerequisites
Make sure you have Python 3.8+ installed along with the required engineering libraries



### Execution

To launch the interactive CLI control dashboard, run the root executable



### 💻 Technical Details & OOP Design
This architecture actively leverages modern software engineering principles instead of raw linear scripting:

• Encapsulation: Hidden data states protected by explicit setters and getters ensuring valid data frames.

• Inheritance & Polymorphism: Specialized Imputers and Outlier Handlers inherit from unified abstract-like base structures (BaseImputer, BaseOutlierHandler), executing custom algorithmic behaviors seamlessly at runtime.

• Error Resilience: Complete multi-tier try-except wrappers inside numerical transformations to prevent crashes on corrupted strings.



### 🔊 Interactive System Sounds
The interactive terminal environment features integrated contextual Sound feedback systems to alert users during file saving transitions, automated calculations completion, and critical error occurrences.
