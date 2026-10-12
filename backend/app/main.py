from fastapi import FastAPI


app = FastAPI()

@app.get("/health") # type: ignore
def health() :
    return {"status" : "ok"}


    