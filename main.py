from fastapi import FastAPI
from entities.FailoverManager import FailoverManager

# uvicorn main:app --reload

app = FastAPI()

""" Main CLI APP """


def main():
    failover_manager: FailoverManager = FailoverManager()
    # ejecutar operacion
    for k in range(5):
        try:
            value = failover_manager.do()
        except Exception as e:
            failover_manager.cambiar_modulo()
            failover_manager.do()
            print("**** ERROR **** ", e)
        print(f"[-] Value: {value}")
        print("-"*30)


main()

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
