# Team Name: Telco's

## Contributors: Hadley McCormack, Colby Robbins, Daniel Yaari

## Dataset

The Telco Customer Churn dataset contains data on 7,032 customers, including demographics, account details, subscribed services, contract information, and billing charges. The prediction task is to use these features to predict whether a customer will churn or remain with the company. The goal is to evaluate how well three different models (linear, logistic, and GAM) predict churn while also considering how interpretable their predictions are.

## Assumption Checks

| Model | Key Assumptions Checked | Evidence | Concern |
|---|---|---|---|
| Linear regression | Linearity, Homoscedasticity, Normality of residuals, Multicollinearity, Independence | The correlation heatmap shows that tenure and TotalCharges are highly correlated (correlation coefficient of 0.83) and MonthlyCharges and TotalCharges are moderately correlated (0.65 coefficient). The residual plot reveals two straight diagonal lines rather than a random scatter. The residual histogram is also bimodal (two humps: one for actual churners and one for actual non-churners) instead of one smooth bell curve. Lastly, the predictions from the model ranged from a minimum of -0.195 to the maximum of 0.844, which is problematic for predicting churn since probabilities can only be in the range from 0 to 1. | Churn is a binary variable, which leads to the core assumptions of linear regression being violated, which is shown by the predictions going outside the valid 0-1 range and by the non-random residual pattern. |
| Logistic regression | Binary outcome, class balance, and adequate sample size | Churn is a binary outcome (Yes/No), which is suitable for logistic regression analysis. The dataset contains 7,032 customers, with 73.4% non-churners and 26.6% churners. A stratified train-test split was used to preserve this class distribution during evaluation. | The classes are moderately imbalanced (which led to further issues regarding accuracy of the model), which can cause the model to favor the majority non-churn class. Additionally, independence and linearity in the log-odds were not tested. |
| GAM | No Concurvity, Independence of Observations, No Influential Outliers, Absence of Perfect Separation, Large Sample Size | High correlation between partial dependence curves shows concurvity. The Durbin-Watson score was 1.7, which lands within the acceptable range of no concering autocorrelation. Each partial dependence curve showed no erratic egde behavior indicating no influential outliers. No binary columns were found that show only one target class, so no perfect separation. Sampling strategies were avoided to mazimize use of the 7032 customer observations and keep a large sample size, especially for a GAM model. | Concurvity between the continuous features is the most concerning, and warrants deeper feature selection. |

## Model Comparison

| Model | Performance Evidence | Interpretability Strength | Interpretability Weakness |
|---|---|---|---|
| Linear regression | The model produced an MSE of 0.146 and an R^2 value of 0.252, indicating a weak fit (the model only explains about 25.2% of the variance in churn). | Linear regressions are directly interpretable due to the fact that a one-unit increase in a numeric feature (or the presence of a categorical feature) corresponds to an exact, constant change in the predicted value, whereas logistic regression coefficients represent changes in log-odds and must be exponentiated into odds ratios before they have a clear, interpretable meaning. | Linear regression assumes a continuous target variable, but Churn is binary, which made this a mismatched model approach from the start. In addition, the correlation heatmap showed high correlation coefficients between tenure, MonthlyCharges, and TotalCharges, revealing  signs of multicollinearity. This means that individual coefficients for these features might not accurately reflect each feature's actual individual effect on churn. |
| Logistic regression | Accuracy = 80.5%; Precision = 65.0%; Recall = 57.2%; F1 = 60.9%; ROC-AUC = 0.836. A confusion matrix was also added to examine classification errors. | Logistic regression is inherently interpretable because each feature has a directly inspectable coefficient. Coefficients can also be converted to odds ratios, if chosen, to describe how predictors are associated with the odds of churn while holding other included variables constant. This file is on a Python file. | The model identified only 57.2% of actual churners, meaning approximately 43% were missed. It also provided an 80% accuracy, but is not substantial considering the nonchurn group was 73%. Correlated predictors can also make individual coefficient explanations less reliable. |
| GAM |  |  |  |

## Recommendation

Recommended model:

Why this model:

What the company can responsibly conclude:

What the company should not conclude yet:

One next analysis we would run:

