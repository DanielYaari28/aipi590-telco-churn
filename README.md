# Team Name: Telco's

## Contributors: Hadley McCormack, Colby Robbins, Daniel Yaari

## Dataset

The Telco Customer Churn dataset contains data on 7,032 customers, including demographics, account details, subscribed services, contract information, and billing charges. The prediction task is to use these features to predict whether a customer will churn or remain with the company. The goal is to evaluate how well three different models (linear, logistic, and GAM) predict churn while also considering how interpretable their predictions are.

## Assumption Checks

| Model | Key Assumptions Checked | Evidence | Concern |
|---|---|---|---|
| Linear regression |  |  |  |
| Logistic regression | Binary outcome, class balance, and adequate sample size | Churn is a binary outcome (Yes/No), which is suitable for logistic regression analysis. The dataset contains 7,032 customers, with 73.4% non-churners and 26.6% churners. A stratified train-test split was used to preserve this class distribution during evaluation. | The classes are moderately imbalanced (which led to further issues regarding accuracy of the model), which can cause the model to favor the majority non-churn class. Additionally, independence and linearity in the log-odds were not tested. |
| GAM | No Concurvity, Independence of Observations, No Influential Outliers, Absence of Perfect Separation, Large Sample Size | High correlation between partial dependence curves shows concurvity. The Durbin-Watson score was 1.7, which lands within the acceptable range of no concering autocorrelation. Each partial dependence curve showed no erratic egde behavior indicating no influential outliers. No binary columns were found that show only one target class, so no perfect separation. Sampling strategies were avoided to mazimize use of the 7032 customer observations and keep a large sample size, especially for a GAM model. | Concurvity between the continuous features is the most concerning, and warrants deeper feature selection. |

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

