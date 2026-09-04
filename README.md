# Team Name: Telco's

## Contributors: Hadley McCormack, Colby Robbins, Daniel Yaari

## Dataset

The Telco Customer Churn dataset contains data on 7,032 customers, including demographics, account details, subscribed services, contract information, and billing charges. The prediction task is to use these features to predict whether a customer will churn or remain with the company. The goal is to evaluate how well three different models (linear, logistic, and GAM) predict churn while also considering how interpretable their predictions are.

## Assumption Checks

| Model | Key Assumptions Checked | Evidence | Concern |
|---|---|---|---|
| Linear regression |  |  |  |
| Logistic regression | Binary outcome, class balance, and adequate sample size | Churn is a binary outcome (Yes/No), which is suitable for logistic regression analysis. The dataset contains 7,032 customers, with 73.4% non-churners and 26.6% churners. A stratified train-test split was used to preserve this class distribution during evaluation. | The classes are moderately imbalanced (which led to further issues regarding accuracy of the model), which can cause the model to favor the majority non-churn class. Additionally, independence and linearity in the log-odds were not tested. |
| GAM |  |  |  |

## Model Comparison

| Model | Performance Evidence | Interpretability Strength | Interpretability Weakness |
|---|---|---|---|
| Linear regression |  |  |  |
| Logistic regression | Accuracy = 80.5%; Precision = 65.0%; Recall = 57.2%; F1 = 60.9%; ROC-AUC = 0.836. A confusion matrix was also added to examine classification errors. | Logistic regression is inherently interpretable because each feature has a directly inspectable coefficient. Coefficients can also be converted to odds ratios, if chosen, to describe how predictors are associated with the odds of churn while holding other included variables constant. This file is on a Python file. | The model identified only 57.2% of actual churners, meaning approximately 43% were missed. It also provided an 80% accuracy, but is not substantial considering the nonchurn group was 73%. Correlated predictors can also make individual coefficient explanations less reliable. |
| GAM |  |  |  |

## Recommendation

Recommended model:

Why this model:

What the company can responsibly conclude:

What the company should not conclude yet:

One next analysis we would run:

