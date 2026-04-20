from datasets import load_dataset
import boto3, json

BUCKET = 'cisc886-medical-chatbot'
s3 = boto3.client('s3')

def upload_jsonl(data, s3_key):
    path = f'/tmp/{s3_key.split("/")[-1]}'
    with open(path, 'w') as f:
        for item in data:
            f.write(json.dumps(item) + '\n')
    s3.upload_file(path, BUCKET, s3_key)
    print(f'Uploaded {len(data)} records to s3://{BUCKET}/{s3_key}')

ds1 = load_dataset('lavita/ChatDoctor-HealthCareMagic-100k', split='train')
upload_jsonl(list(ds1), 'datasets/medical/raw/healthcaremagic.jsonl')

ds2 = load_dataset('UCSD26/medical_dialog', 'en', split='train')
upload_jsonl(list(ds2), 'datasets/medical/raw/meddialog.jsonl')

ds3 = load_dataset('pubmed_qa', 'pqa_labeled', split='train')
upload_jsonl(list(ds3), 'datasets/medical/raw/pubmedqa.jsonl')

print('All 3 datasets uploaded!')
