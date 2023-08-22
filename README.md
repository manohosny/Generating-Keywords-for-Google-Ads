# SEM Keyword Generation for Sofas

## Overview

This project is designed to automate the generation of keywords for a Search Engine Marketing (SEM) campaign related to sofas. By combining product names with shopping-related terms, we create a comprehensive list of potential search terms. The generated list includes both exact and phrase match types.

## Requirements

- Python 3.x
- Pandas library

## Files

- `main.py`: This is the main script that contains the code to generate keywords.
- `keywords.csv`: This CSV file contains the final list of generated keywords.

## How to Run

1. Ensure you have Python 3.x installed.
2. Install the required libraries using pip:
   ```
   pip install pandas
   ```
3. Run the script:
   ```
   python main.py
   ```
4. After execution, check the `keywords.csv` file for the generated keywords.

## Features

- **Keyword Combination**: Combines product names with shopping-related terms to generate potential search terms.
- **Match Types**: Generates keywords for both exact and phrase match types.
- **Export to CSV**: Saves the final list of keywords to a CSV file for easy use in SEM platforms.

## Summary

After running the script, you'll get a summary of the campaign work, grouped by 'Ad Group' and 'Criterion Type', displaying the count of keywords.

---

This README provides a brief overview of the project, its requirements, and instructions on how to run the script. Adjustments can be made based on additional details or specific needs of the project.
