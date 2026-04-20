# Launch EMR Cluster
aws emr create-cluster --name "MedicalChatbotSpark" --release-label emr-6.15.0 --applications Name=Spark Name=Hadoop --instance-groups InstanceGroupType=MASTER,InstanceType=m5.xlarge,InstanceCount=1 InstanceGroupType=CORE,InstanceType=m5.xlarge,InstanceCount=2 --use-default-roles --ec2-attributes KeyName=my-key-project --log-uri s3://cisc886-medical-chatbot/emr-logs/

# Terminate cluster after job
# aws emr terminate-clusters --cluster-ids j-XXXXXXXXX
