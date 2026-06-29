import re

with open("input.txt","r") as file:
    text=file.read()

emails=re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",text)

with open("emails.txt","w") as output:
    for email in emails:
        output.write(email+"\n")

print("Email addresses found:",len(emails))
print("Saved successfully in emails.txt")
