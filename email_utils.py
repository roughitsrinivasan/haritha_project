import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders



def index(email,username,cur_date,order_id,address,phnNo):
    try:
        body=f'''
        Dear {username},

        We're excited to confirm your recent boutique purchase with [Your Boutique Name]. Your trust in us means a lot, and we appreciate your choice to shop with us.

        Here are the key details of your purchase:

        Order Number: {order_id}
        Date of Purchase: {cur_date}
        Shipping Address: {address}

        Thank you for choosing classic threads for your hair care needs. 
        We value your trust and look forward to serving you in the future.

        Best regards,

        {username}
        '''
        # put your email here
        sender = 'kernel23symposium@gmail.com'
        # get the password in the gmail (manage your google account, click on the avatar on the right)
        # then go to security (right) and app password (center)
        # insert the password and then choose mail and this computer and then generate
        # copy the password generated here
        password = 'rweriuwugqodjdme'
        # put the email of the receiver here
        receiver = email

        #Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender
        message['To'] = receiver
        message['Subject'] = "Successfully registered"

        message.attach(MIMEText(body, 'plain'))
        # filen = +".pdf"
        # __location__ = os.path.realpath(
        # os.path.join(os.getcwd(), os.path.dirname(__file__)))
        # with open(os.path.join(__location__, filen),'rb') as pdf:
            # print(pdf)
            # pdfname = '/api/rank-test.pdf'

            # pdfname = open(pdf, 'rb')
            
            # payload = MIMEBase('application', 'octate-stream', Name=filen)
            # # payload = MIMEBase('application', 'pdf', Name=pdfname)
            # payload.set_payload((pdf).read())

            # enconding the binary into base64
            # encoders.encode_base64(payload)
            
            # # add header with pdf name
            # payload.add_header('Content-Decomposition', 'attachment', filename=filen)
            # message.attach(payload)

            #use gmail with port
        session = smtplib.SMTP('smtp.gmail.com', 587)

            #enable security
        session.starttls()

            #login with mail_id and password
        session.login(sender, password)

        text = message.as_string()
        session.sendmail(sender, receiver, text)
        session.quit()
        print('Mail Sent')

        return True
    except Exception as e:
        print(e)
        return False