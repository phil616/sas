print("GO")
import uvicorn
from main import application as fastapi_app
if __name__ == '__main__':

    uvicorn.run(
        fastapi_app,
        host="0.0.0.0",
        port=88
    )
