from fastapi import FastAPI, HTTPException
import pandas as pd
import os

app = FastAPI()

csv = 'clean_data.csv'

def load_data():
    if os.path.exists(csv):
        df = pd.read_csv(csv)
        if 'level_0' in df.columns:
            df.drop(columns=['level_0'], inplace=True)
        df.reset_index(inplace=True)
        return df
    return pd.DataFrame(columns=["duration"])

def save_data(df):
    df.to_csv(csv, index=False)

@app.get("/lihatdata")
def get_data():
    df = load_data()
    return df.to_dict(orient='records')

@app.delete("/hapusdata")
def delete_data(index: int):
    df=load_data()
    if index < 0 or index >= len(df):
        raise HTTPException(status_code=404, detail="item not found")
    
    df = df.drop(index)
    save_data(df)

    return {"message": "Item deleted succesfully"}