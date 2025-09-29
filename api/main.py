from flask import Flask, jsonify
import boto3, os

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

def get_client():
    return boto3.client(
        "s3",
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        region_name=os.getenv("AWS_DEFAULT_REGION", "us-east-1")
    )

@app.route("/api/objects")
def list_objects():
    bucket = os.getenv("S3_BUCKET_NAME")
    s3 = get_client()
    resp = s3.list_objects_v2(Bucket=bucket, Delimiter="/")

    return jsonify({
        "bucket": bucket,
        "objects": [o["Key"] for o in resp.get("Contents", [])],
        "prefixes": [p["Prefix"].rstrip("/") for p in resp.get("CommonPrefixes", [])]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)