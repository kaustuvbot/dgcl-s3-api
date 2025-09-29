provider "aws" { region = var.region }

resource "aws_s3_bucket" "main" {
  bucket = var.bucket_name
}

resource "aws_s3_object" "root_file" {
  bucket = aws_s3_bucket.main.bucket
  key    = "hello.txt"
  source = "/dev/null"
}

resource "aws_s3_object" "nested_file" {
  bucket = aws_s3_bucket.main.bucket
  key    = "folder1/nested.txt"
  source = "/dev/null"
}
