from fastapi import FastAPI     #fastapilibrary is the main tool

app = FastAPI()                  #creating web application appis the server

@app.get("/health")              # someone open the brower run the below function
def health():                    # health is the function
   return{"status":"ok"}         #JSON reply that it is alive


   
products = [{"sku":"SKU-001","name":"Laptop","price":45000,"catagory":"electronics"},{"sku":"SKU-002","name":"Harry potter","price":5000,"catagory":"Books"},{"sku":"SKU-003","name":"T-shirt","price":500,"catagory":"clothing"}]
@app.get("/products")         #with url down function gets run
def get_products():
   return products            #full list JSON will sent and automatically FASTAPI changes python list ah JSON changed