# CISC886 Medical Chatbot

A domain-specific medical chatbot powered by fine-tuned TinyLlama, deployed on AWS.

## Phases
- Phase 1: Model Selection (TinyLlama)
- Phase 2: Dataset Collection (HealthCareMagic + MedDialog + PubMedQA)
- Phase 3: Spark Processing on AWS EMR
- Phase 4: Fine-tuning with QLoRA + Unsloth
- Phase 5: Deployment on AWS EC2 + Docker + ECR
- Phase 6: GitHub Organization + CI/CD

## Tech Stack
- Model: TinyLlama-1.1B
- Fine-tuning: QLoRA via Unsloth on Google Colab
- Data Processing: Apache Spark on AWS EMR
- Storage: AWS S3
- Deployment: Ollama + Flask + Docker on EC2
- CI/CD: GitHub Actions
