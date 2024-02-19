# Deploy


cd scoring-pipeline
az ml online-endpoint create --file endpoint.yml -g aml-rg --workspace-name aml-northcentral
az ml online-deployment create --file deployment.yml -g aml-rg --workspace-name aml-northcentral



az ml online-endpoint update --name wa-customer-churn-prediction2 --traffic "blue=90 green=10" -g aml-rg --workspace-name aml-northcentral



az ml online-endpoint update --name wa-customer-churn-prediction2 --traffic "blue=90 green=10" -g aml-rg --workspace-name aml-northcentral

sudo apt-get install apache2-utils


# ApacheBench
ab -p test-data-scoring.json -T application/json -H 'Authorization':'Bearer 1zokzIswBzOZyQTZg7JkM3a81RoPr42o' -c 10 -n 100 https://wa-customer-churn-prediction2.northcentralus.inference.ml.azure.com/score


watch -n 2 'ab -p test-data-scoring.json -T application/json -H "Authorization: Bearer 1zokzIswBzOZyQTZg7JkM3a81RoPr42o" -c 10 -n 100 https://wa-customer-churn-prediction2.northcentralus.inference.ml.azure.com/score'
