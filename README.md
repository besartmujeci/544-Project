# Automated Analysis of Licensee Event Reports in Nuclear Power Plants
We present our work on automated analysis of Licensee Event Reports (LERs) from three different power plants in the US to create a summary of the most common and recurring safety issues. We aimed to map each incident reported into ten key traits in nuclear safety culture identified by the Institute of Nuclear Power Operations (INPO). We used a GPT-based large language model for the multi-label classification task, implementing both Zero-Shot and Few-Shot approaches.

## Installation
```bash
pip install scikit-llm
```

## Description of Jupyter Files
**1. All_Models.ipynb:** Includes all models analyzed (Zero-shot, Few-shot, and Random Classifier)

**2. Evaluation.ipynb:** Presents evaluation of all models analyzed + true/predicted trait counts visualization.

**3. All_LERs.ipynb:** Uses the best model to predict the traits for all 250 LERs + histogram visualization of trait counts by power plant

