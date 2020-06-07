from twilio.rest import Client 
 
account_sid = 'AC09fc7a7c525d079ddbfd588d0000' 
auth_token = 'b0419ca52d723cb2429f272506f68000000' 
client = Client(account_sid, auth_token) 
def send_love():
    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Love you Daddy',      
                              to='whatsapp:+918919904214' 
                          ) 
 
    print(message.sid)
