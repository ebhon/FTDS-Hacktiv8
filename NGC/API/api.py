from fastapi import FastAPI, HTTPException, Header

app = FastAPI()

API_KEY = "testingapitokenkey1234" #testing api token key 1234

@app.get("/")
def home():
  return {"message":"This is my API. Welcome!"}

@app.get("/protected")
def protect(api_key: str = Header(None)):

  if api_key is None or api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

  return {"message":"This endpoint is protected by API Token Key.",
          "data":{"1":{"username":"fahmi","password":"1234"},
                  "2":{"username":"raka","password":"abcd123"},
                  "3":{"username":"rachman","password":"h8teacher"}
                 }
          }