# 5. Email Batch Sender 

# Objective: Yield one email at a time for bulk sending with pause-resume logic. 
# Requirements: 
#  Create generator to yield email addresses. 
#  Use .send() to dynamically control batch size. 
#  Use .throw() to simulate and log failures. 
#  Collect StopIteration.value after all emails sent.

def email_sender(emails):
    index = 0
    batch_size = 2
    try:
        while index < len(emails):
            for i in range(batch_size):
                if index < len(emails):
                    yield emails[index]
                    index += 1
            batch_size = yield  # receive new batch size
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        return "All emails sent."

email_list = ["a@mail.com", "b@mail.com", "c@mail.com", "d@mail.com", "e@mail.com"]
sender = email_sender(email_list)

print("Email Batch Sender:")
try:
    print(next(sender))   # a@mail.com
    print(next(sender))   # b@mail.com
    print(sender.send(1)) # c@mail.com
    print(next(sender))   # d@mail.com
    print(next(sender))   # e@mail.com
    print(next(sender))   # triggers StopIteration
except StopIteration as e:
    print("Status:", e.value)
