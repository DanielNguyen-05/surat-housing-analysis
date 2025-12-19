### 1. Team Plan and Work Distribution

# Team Plan & Work Distribution

## 1. Team Member Information
| Member Name | Student ID | Role |
| :--- | :--- | :--- | :--- |
| **Nguyen Huu Phuc** | 23127248 | Data Engineer & Analyst | 
| **Le Nhat Khoi** | 23127004 | Statistician & Analyst | 
| **Nguyen Hai Dang** | 23127165 | ML Engineer & Lead | 

## 2. Work Breakdown
**Total Contribution:** 100% 

*   **Nguyen Huu Phuc (100%)**
    *   **Phase 1:** Data Collection & Initial cleaning logic (Regex parsing for `price` and `area`).
    *   **Phase 2:** Handled Data Exploration (Section 2.1 - 2.3) and Outlier Analysis.
    *   **Analysis:** Conducted **Q1 (Unit Price Efficiency)** and **Q4 (Floor Effect Analysis)**.
    *   **Deliverable:** Wrote the "Data Collection" documentation and formatted the final charts for floor analysis.

*   **Le Nhat Khoi (100%)**
    *   **Phase 1:** Developed the "Cross-Swap" cleaning logic for mixed categorical columns.
    *   **Phase 2:** Statistical Profiling (Correlations, Categorical distributions).
    *   **Analysis:** Conducted **Q2 (Neighborhood Premium)** and **Q3 (Pricing Uncertainty)**.
    *   **Deliverable:** Implemented the Hedonic Regression model and Levene’s Test logic.

*   **Nguyen Hai Dang (100%)**
    *   **Phase 1:** Finalized the Preprocessing Pipeline and helper functions.
    *   **Analysis:** Conducted **Q5 (Clustering/Segmentation)** and **Q6 (Price Prediction ML)**.
    *   **Deliverable:** Wrote the Project Summary, Limitations, and complied the final `README.md`.

## 3. Collaboration Process
*   **Version Control:** We used a shared GitHub repository. Each member worked on separate feature branches and merged via Pull Requests.
*   **Communication:** Weekly syncs on Messenger to discuss "Red Flags" in the data (e.g., the mixed floor/transaction columns).
*   **Integration:** We agreed on a common processed data format (`surat_cleaned.npy`) early on so that Q1-Q6 could be developed in parallel without conflict.

## 4. Project Timeline
*   **Week 1:** Dataset Selection (Kaggle), initial skimming, and drafting the 6 Research Questions.
*   **Week 2:** Deep Data Exploration and building the Cleaning Pipeline (handling the "Uncleaned" aspects).
*   **Week 3:** Conducting Analysis for Q1, Q2, Q3, and Q4.
*   **Week 4:** Advanced ML (Q5, Q6), Writing Conclusions, and Final Notebook assembly.

---

### 2. Jupyter Notebook Organization

```text
/submission_folder
│
├── 01_data_collection.ipynb  
├── 02_data_exploration.ipynb                
├── 03_data_preprocessing.ipynb              
├── 04_question_01.ipynb       
├── 04_question_02.ipynb   
├── 04_question_03.ipynb   
├── 04_question_04.ipynb 
├── 04_question_05.ipynb
├── 04_question_06.ipynb                  
├── 05_project_summary.ipynb      
│
├── data/
│   ├── raw/surat_uncleaned.csv
│   └── processed/surat_cleaned.npy
│
├── requirements.txt
├── README.md
└── TEAM_PLAN.md
```
