## sesSender.py

Use this script to send MIME Multipart bulk email via AWS SES

### Usage

edit `msg.txt` and add the text version of your mail

edit `msg.html` to add the html version of your mail

edit `clientList.txt` to add your recipients list (one per line)

edit sesSender.py and change the following variables with appropriate values:

`region` = "AWS region you want to use"
`key_id` = "SOMEKEYID"
`secret_key` = "SOMESECRETKEY"
`sender` = "SENDER NICE NAME <do_not_reply@email.com>"
`subject` = "This is a bulk email sent via SES"

### TODO
add some error checking...
