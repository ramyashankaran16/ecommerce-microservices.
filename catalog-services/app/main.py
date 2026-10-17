from fastapi import FastAPI     #fastapilibrary is the main tool

app = FastAPI()                  #creating web application appis the server

@app.get("/health")              # someone open the brower run the below function
def health():                    # health is the function
   return{"status":"ok"}         #JSON reply that it is alive


   
