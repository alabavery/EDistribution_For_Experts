SEEN_EMAIL_FILE_NAME = "seen_email_data.json"
ADDRESSES_JSON_FILE_NAME = "unused_addresses.json"
LOG_FILE_PATH = "logging.txt"

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly','https://www.googleapis.com/auth/gmail.send','https://www.googleapis.com/auth/gmail.modify']
CLIENT_SECRET_FILE_NAME = 'client_secret.json'
APPLICATION_NAME = 'TellOnKlein'
APPLICATION_EMAIL = 'tellonklein@gmail.com'

NEW_ADDRESSES_SUBJECT = "TBNY Mission Dispatch"
ATTACHMENT_PROMPT_SUBJECT = "TBNY Mission Dispatch"
CAPITULATION_RESPONSE_SUBJECT = "TBNY Mission Dispatch"

CAPITULATION_TEXT = "code red"

NEW_ADDRESSES_TEXT = """Hello, Agent of the Resistance. Thank you for volunteering for this important mission.

Did you know that most Democrats in Jeff Klein's district don't know he sold out to the GOP? Today, with your help, we're going to let them know.

Instructions

STEP 1: Below are the addresses of 10 VERY reliable Democratic voters in Klein's district. Please write them each a postcard. Something like:

"Hi ____,

I'm writing to let you know that your senator, Jeff Klein, gave control of the state senate to a right wing Republican named John Flanagan. Because of this, we can't pass any progressive legislation in NY. Please call Klein and tell him to stop: (718) 822-2049.

Best,
_______"

STEP 2: Once the postcards are written and stamped, take a quick photo of all of them and send it back to this e-mail address. Then mail out the postcards and we'll send you 10 more addresses.

If at anytime you realize you won't be able to complete the mission, help us out by replying to this email with the words 'code red' in your message body.  
That way, we can get another Agent on the case.

Together, we can make NY True Blue one voter at a time.

Sincerely,
The TBNY Postcard Robot

Your 10 Voters:
"""

ATTACHMENT_PROMPT_TEXT = """Hey there, Agent.  If you're emailing to get 10 more voter addresses, please attach an image of the postcards that you've 
already sent and we'll give you 10 more.  If you're emailing about something else, give us some time to read your email and we'll get back to you ASAP.

Sincerely,
The TBNY Postcard Robot
"""
CAPITULATION_RESPONSE_TEXT = """Thanks for letting us know.  If you want to restart the mission at any time, send another email.

Sincerely,
The TBNY Postcard Robot"""