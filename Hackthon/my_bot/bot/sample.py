from flask import Flask,render_template,request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


app = Flask(__name__) 
bot = ChatBot("Chatterbot",storage_adapter="chatterbot.storage.SQLStorageAdapter",
              filters = ["chatterbot.filters.RepetitiveResponseFilter"],
              
              logic_adapter=[
              {
                  'import_path':"chatterbot.logic.BestMatch"
                  
              },




              {
                  'import_path':"chatterbot.logic.LowConfidenceAdapter",
                  'threshold':0.55,
                  'default_response':'Sorry I do not know that'
              }])
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")



@app.route("/")
def index():
     return render_template("index.html") #to send context to html

@app.route("/get")
def get_bot_response():
     userText = request.args.get("msg") #get data from input,we write js  to index.html
     return str(bot.get_response(userText))


if __name__ == "__main__":
     app.run(debug = True)
     


