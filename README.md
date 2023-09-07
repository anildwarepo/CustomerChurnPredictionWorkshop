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




### Pre-requisites
* Azure Machine Learning workspace provisioned.
* Compute Cluster provisioned in the workspace.
* Training Cluster created. Recommend to create training cluster with 3 nodes with each Node have 2 vCPUs. This can reduce the AutoML training time. This notebook takes about 12 minutes to complete the training on a 3 node CPU cluster with Standard_DS11_v2 (2 cores, 14 GB RAM, 28 GB disk). 
* Recommendation is to use AML compute instance to run the notebook.
* The notebook can be run locally but will the following dependencies installed locally:
 
    - python installed - python 3.8+
    - conda installed
    - Azure ML Python [SDK](https://learn.microsoft.com/en-us/python/api/overview/azure/ai-ml-readme?view=azure-python) and [CLI](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-configure-cli?view=azureml-api-2&tabs=public) v2 installed.
    - Install additional dependencies in the conda_env.yml
    
            conda env create -f conda_env.yml

* Clone repo from AML Compute Instance terminal or locally. 
        
        git clone https://github.com/anildwarepo/CustomerChurnPredictionWorkshop.git


* AML workspace can be configured with Private Endpoint with necessary DNS changes as documented [here](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-custom-dns?view=azureml-api-2&tabs=azure-cli). 

* Compute Cluster and Compute intances provisioned. 

### Please review some of the AML concepts here. 

[Data concepts in Azure Machine Learning](https://learn.microsoft.com/en-us/azure/machine-learning/concept-data?view=azureml-api-2).

[Create and run machine learning pipelines using components with the Azure Machine Learning SDK v2](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-create-component-pipeline-python?view=azureml-api-2).

[Create and run machine learning pipelines using components with the Azure Machine Learning studio](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-create-component-pipelines-ui?view=azureml-api-2).

There are two ways with which one can accomplish Automl training and scoring in AML. 
1. Automated ML UI.  [Please see this for more details.](https://learn.microsoft.com/en-us/azure/machine-learning/concept-designer?view=azureml-api-2).

2. Jupyter Notebook or Cli using AML python SDK V2.

- For Automate ML using UI please see [this](Designer.md).

- For notebook based Automl, please see [this](Notebook.md).




