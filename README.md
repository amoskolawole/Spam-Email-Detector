# Spam-Email-Detector
NLP Machine Learning project for detecting spam email using TF-IDF and Logistic Regression.


## Objective
- Load and Clean Data
- Build a classification model using TF-IDF(For NLP) Logistic Regression
- Evaluate model performance using confusion matrix and classification report
- Understand how Model was able to learn some important words and text pattern
- Perform manual testing

## Tools and Liberary Used
- Python
- Pandas
- Scikit-learn

## Machine Learning Workflow
1. Data Prepreocessing
2. Feature Encoding
3. Train-Test-Split
4. TF-IDF Vectorization
5. Logistic Regression Modeling
6. Evaluation using:
   - Accuracy Score
   - Confusion Matrix
   - Classification Report
7. Word Importance Analysis
8. Custom Message Testing


## Findings
- Spam messages contain strong identifiable keywords that TF-IDF was able to identify using Vectorizer
- LogisticRegression was used for Classification and it performs strongly in text classification
- Precision for spam detection was very high while Recall showed some spam messages were still missed


## Conclusion
Model perform excellently in classification with a very high accuracy both for training and testing(No Overfitting) and precision in catching spam messages was very high though some spam messages still escaped detection. Model also perform well with manual testing.
