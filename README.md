# Customer Churn Prediction using Azure Machine Learning Automl with Python SDK V2


Introduction to Azure Machine Learning Automated ML Using Telco Customer Churn Sample Dataset

In today's highly competitive business landscape, retaining customers is paramount to the success of any organization. To this end, understanding and predicting customer churn, or the likelihood of customers leaving a service or product, is a crucial task for businesses across various industries. This is where the power of machine learning comes into play, enabling organizations to harness data-driven insights to reduce customer churn rates and enhance customer retention strategies.

Azure Machine Learning, Microsoft's cloud-based machine learning platform, offers an array of tools and services to empower data scientists and developers in building and deploying machine learning models with ease. One of its standout features is Automated Machine Learning (AutoML), which simplifies the end-to-end machine learning process, from data preparation and feature engineering to model selection and deployment.

In this workshop, we will explore the capabilities of Azure Machine Learning's Automated ML using the Telco Customer Churn sample dataset. The Telco Customer Churn dataset is a classic example in the field of customer churn prediction, comprising various features related to customer demographics, services subscribed, contract details, and the ultimate churn status. Leveraging this dataset within the Azure Machine Learning environment, we will showcase how AutoML can help streamline the model development process, leading to more accurate and efficient predictions of customer churn.

Key Takeaways:

Simplified Machine Learning Workflow: Azure AutoML simplifies the often complex process of building machine learning models. It automates many of the tedious and time-consuming tasks, allowing data scientists and developers to focus on high-level tasks such as feature engineering and model deployment.

Efficient Model Selection: AutoML automatically evaluates a wide range of machine learning algorithms and hyperparameters to identify the best-performing model for the given dataset. This eliminates the need for manual trial-and-error, saving time and resources.

Interpretability and Explainability: Azure AutoML provides tools to understand and interpret model predictions. This is essential for businesses that require transparency in their decision-making processes, especially in sensitive areas like customer churn prediction.

Scalability and Cloud Integration: Being a cloud-based solution, Azure Machine Learning offers scalability to handle large datasets and complex machine learning tasks. It seamlessly integrates with other Azure services, making it easier to deploy and manage machine learning models in a production environment.

Improved Customer Retention: By using the Telco Customer Churn dataset as an example, we'll demonstrate how AutoML can help organizations identify potential churners early and develop effective strategies to retain valuable customers. This can lead to reduced churn rates, increased customer satisfaction, and ultimately, improved business outcomes.

Through this exploration of Azure Machine Learning Automated ML and the Telco Customer Churn dataset, you'll gain insights into the power of automated machine learning in solving real-world business challenges and enhancing customer retention efforts. Let's dive in and harness the potential of data-driven decision-making with Azure AutoML.


This notebook uses [Telco Customer Churn data from IBM Sample Datasets](https://community.ibm.com/community/user/businessanalytics/blogs/steven-macko/2019/07/11/telco-customer-churn-1113).


### In the real world
In the real-world scenario described, we are addressing the challenge of customer churn prediction using machine learning. Customer churn refers to the phenomenon where customers stop using a product or service offered by a company. Predicting customer churn is crucial for businesses as it allows them to proactively take actions to retain customers and maintain profitability. Here, we'll elaborate on the process using proper machine learning terminology and discuss the real-world challenges involved:

1. **Data Collection**:
   - Historical Data: To build a churn prediction model, we start by gathering historical data. This data contains information about past customers who have churned. It typically includes features such as customer demographics, usage patterns, purchase history, and the churn label (whether they churned or not).
   - Current Data: Additionally, we collect data from the current set of customers. This data will include features similar to the historical data but will not have churn labels.

2. **Data Preprocessing**:
   - Data Cleansing: The collected data is often messy, containing missing values, incorrect entries, and duplicates. Data cleansing involves identifying and rectifying these issues to ensure the dataset's quality.
   - Feature Engineering: Feature engineering is the process of creating new informative features or transforming existing ones to improve the model's predictive power. For example, calculating customer tenure or creating customer segments.

3. **Data Splitting**:
   - The cleansed historical data is divided into two parts: a training dataset and a validation dataset. The training dataset is used to train the machine learning model, while the validation dataset is used to assess the model's performance during training.

4. **Machine Learning Model Selection**:
   - Automated Machine Learning (AutoML) tools are employed to automate the process of selecting the most suitable machine learning algorithm and hyperparameters. AutoML helps save time and resources in model development.

5. **Model Training**:
   - The selected machine learning model is trained using the historical data. The model learns to recognize patterns that lead to churn based on the provided features.

6. **Model Evaluation**:
   - The model's performance is evaluated on the validation dataset using metrics such as accuracy, precision, recall, F1-score, and ROC AUC. This step helps assess how well the model generalizes to unseen data.

7. **Deployment**:
   - Once the model is satisfactory, it is deployed into the production environment. This allows it to make predictions on the current set of customers.

8. **Continuous Monitoring and Updating**:
   - The training dataset can be periodically updated with new churn data or changes in customer behavior. This ensures that the model remains relevant and accurate over time.
   - Regular updates to the model are necessary to adapt to shifts in customer behavior, market conditions, and other external factors.

Real-World Challenges:
- **Data Quality**: Ensuring the quality of historical and current data is a significant challenge. Cleaning and preprocessing the data can be time-consuming and require domain expertise.
- **Imbalanced Data**: Churn data is often imbalanced, with a majority of customers not churning. This can lead to model bias, and specialized techniques like oversampling or undersampling may be needed.
- **Model Interpretability**: Understanding why the model makes certain predictions is crucial for taking appropriate actions to prevent churn.
- **Scalability**: Handling large datasets and maintaining model performance as the dataset grows can be challenging.
- **Model Maintenance**: Continuously updating and retraining the model to reflect changing customer behavior and business conditions requires a well-defined process.

In summary, predicting customer churn using machine learning involves a series of steps, from data collection and preprocessing to model training and deployment. Addressing real-world challenges is essential to build an effective churn prediction system that helps businesses retain valuable customers and improve their bottom line.



### Pre-requisites for the Customer Churn workshop
* Azure Machine Learning workspace provisioned.
* Compute Cluster provisioned in the workspace.
* Training Cluster created. Recommend to create training cluster with 3 nodes with each Node have 2 vCPUs. This can reduce the AutoML training time. This notebook takes about 12 minutes to complete the training on a 3 node CPU cluster with Standard_DS11_v2 (2 cores, 14 GB RAM, 28 GB disk). 

* AML workspace can be configured with Private Endpoint with necessary DNS changes as documented [here](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-custom-dns?view=azureml-api-2&tabs=azure-cli). 

* Compute Cluster and Compute intances provisioned. 
* VS Code with Python and Jupyter extensions installed. Or a Jupyter environment which can host notebooks. 


### Please review some of the AML concepts here. 

[Data concepts in Azure Machine Learning](https://learn.microsoft.com/en-us/azure/machine-learning/concept-data?view=azureml-api-2).

[Create and run machine learning pipelines using components with the Azure Machine Learning SDK v2](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-create-component-pipeline-python?view=azureml-api-2).

[Create and run machine learning pipelines using components with the Azure Machine Learning studio](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-create-component-pipelines-ui?view=azureml-api-2).

[Compute Targets](https://learn.microsoft.com/en-us/azure/machine-learning/concept-compute-target?view=azureml-api-2).

There are two ways with which one can accomplish Automl training and scoring in AML. 
1. Automated ML UI.  [Please see this for more details.](https://learn.microsoft.com/en-us/azure/machine-learning/concept-designer?view=azureml-api-2).

- For Automate ML using UI please see [this](Designer.md).

2. Jupyter Notebook or Cli using AML python SDK V2.

- For notebook based Automl, please see [this](Notebook.md).




