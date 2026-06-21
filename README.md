🎙️ AWS Serverless Text-to-Speech Pipeline
📌 Short Description

This project converts .txt files uploaded to Amazon S3 into MP3 audio using AWS Lambda and Amazon Polly.
It stores metadata in DynamoDB and sends notifications via SNS.

🔄 Architecture Flow
User Upload (.txt)
        ↓
   Amazon S3 Bucket
        ↓ (Trigger)
   AWS Lambda
        ↓
 ┌──────────────┬──────────────┬──────────────┐
 │  Amazon Polly │ DynamoDB     │ SNS          │
 │ Text → Speech │ Metadata     │ Notification │
 └──────────────┴──────────────┴──────────────┘
        ↓
   MP3 saved back to S3 (/audio/)
🖼️ Screenshots
1️⃣ Architecture Diagram
<img width="1536" height="1024" alt="ChatGPT Image Jun 21, 2026, 11_51_55 AM" src="https://github.com/user-attachments/assets/4f81cdfe-91ed-4651-858f-f57b626c299e" />



2️⃣ S3 Bucket (Input File Upload)
<img width="1918" height="772" alt="Screenshot 2026-06-21 120705" src="https://github.com/user-attachments/assets/7bc3922d-7031-4418-817e-126a389db9c7" />



3️⃣ Lambda Function Trigger

<img width="1686" height="510" alt="Screenshot 2026-06-21 120820" src="https://github.com/user-attachments/assets/601e680a-3ae5-4913-8b2c-2a27f7585581" />

#CloudWatch output
<img width="1918" height="752" alt="Screenshot 2026-06-21 113430" src="https://github.com/user-attachments/assets/fd38b590-655c-4760-8cc4-a314d6712bb3" />



4️⃣ DynamoDB Table Records

<img width="1881" height="778" alt="Screenshot 2026-06-21 121032" src="https://github.com/user-attachments/assets/c1922588-f0df-4ddf-b8ce-d5e7342fdbf0" />


5️⃣ SNS Notification (Email/SMS)
<img width="1867" height="352" alt="Screenshot 2026-06-21 120117" src="https://github.com/user-attachments/assets/9c3e7f2c-dbae-46d2-b0c7-a0cbc3a4271c" />



6️⃣ Output MP3 in S3
<img width="1897" height="775" alt="Screenshot 2026-06-21 120915" src="https://github.com/user-attachments/assets/c14cd25f-7477-423f-9d77-8344c6017770" />




7 build pipeline
<img width="1895" height="725" alt="Screenshot 2026-06-21 115706" src="https://github.com/user-attachments/assets/84ba56ef-67d2-47ef-8ad9-407b397877e8" />


⚙️ Flow Summary
Upload .txt file to S3
S3 triggers Lambda
Lambda reads file
Polly converts text → speech
MP3 saved in S3
Metadata stored in DynamoDB
SNS sends notification
