# S3 Bucket Object Listing API

A simple Python + Flask API that lists objects and prefixes in an AWS S3 bucket. Packaged with Docker and deployable with Terraform.

---

## Features

* `/health` endpoint for health checks
* `/api/objects` endpoint to list objects and prefixes
* Dockerized for easy local run
* Terraform config for AWS S3 bucket provisioning
* `.env.example` provided for environment variables

---

## Prerequisites

* Docker & Docker Compose v2 (`docker compose` command)
* AWS CLI configured
* Terraform >= 1.0

---

## Setup

### 1. Clone and configure

```bash
git clone <your_repo>
cd s3-api-project
cp .env.example .env
```

Fill in `.env` with your AWS credentials and bucket name.

### 2. Run API with Docker

```bash
docker compose up -d
```

Check health:

```bash
curl http://localhost:5000/health
```

### 3. Provision AWS S3 with Terraform

> ⚠️ **Note:** Make sure to change the `bucket_name` variable in `terraform/variables.tf` to a globally unique name before applying.

```bash
cd terraform
terraform init
terraform apply -auto-approve
```

### 4. Test Object Listing

```bash
curl http://localhost:5000/api/objects
```

Expected response:

```json
{
  "bucket": "my-test-bucket-123456",
  "objects": ["hello.txt"],
  "prefixes": ["folder1"]
}
```

---

## Environment Variables

See `.env.example` for required variables:

```env
AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
AWS_DEFAULT_REGION=us-east-1
S3_BUCKET_NAME=your-bucket-name
```

---