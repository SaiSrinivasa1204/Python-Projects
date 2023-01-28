email_id = input("Please enter your company email id: ").strip()

username = email_id[:email_id.index('@')]

domain = email_id[email_id.index('@')+1:]

print(f"Your company username is {username} and your domain is {domain}")

