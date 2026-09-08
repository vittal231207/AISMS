import os, smtplib

email = "smspythonproj@gmail.com"
password = os.environ.get("EDUMATRIX_SMTP_PASS")

print("Testing Gmail login...")
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(email, password)
    print("✅ Login successful!")