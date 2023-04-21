#For the seling Price alert
def Selling_alert(subject,body,to):
    '''Impoet Some Librery For The perfoming'''
    import smtplib
    from email.message import EmailMessage

    #Take Input for The Subjext Body And Emali For The Sender 
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
            
    user = "novagaming990768@gmail.com"
    msg['from'] = user
    password = 'kkijmijchbgsdbxw'
            
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(user,password)
    server.send_message(msg)
            
    server.quit()
    
def Buying_alert(subject,body,to):
    '''Impoet Some Librery For The perfoming'''
    import smtplib
    from email.message import EmailMessage

    #Take Input for The Subjext Body And Emali For The Sender 
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
            
    user = "hyperdesk7@gmail.com"
    msg['from'] = user
    password = 'kdhwttrtoewteshw'
            
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(user,password)
    server.send_message(msg)
            
    server.quit()

