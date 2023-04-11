
email_list = []
with open('CONTACT.in', 'r') as file:
    for line in file:
        email = line.strip().lower()
        if email not in email_list:
            email_list.append(email)

sorted_emails = sorted(email_list)
for email in sorted_emails:
    print(email)
