#simplyjob##############################
#simplyjob is an AI agent which asks your
#prefence and if its job-related, then
#asks your biography and feedbacks that
#it receives your given biography
#rossikamal@gmail.com
#kamalrossi.github.io/profile
##################################




import chainlit as cl

@cl.on_message
def main(message:str):
 your_typed_text_at_first=message.title()
 
 if 'job'  in message:
   file=None
   while file==None: 
     file=cl.ask_for_file(title="please upload biography",accept={"text/plain"})
   text=file.content.decode("utf-8")

   cl.send_message(content="Your biography stands as {text}")
 cl.send_message(content="your initial input{your_typed_text_at_first}")
 