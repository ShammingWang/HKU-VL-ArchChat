# run.py
import os
from dotenv import load_dotenv
import uvicorn

load_dotenv(dotenv_path=".env.development")


if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    print(os.getenv("DATA_DIR"))
    uvicorn.run(
        "open_webui.main:app",
        host="0.0.0.0",
        port=port,
        reload=True,
        forwarded_allow_ips="*"
    )
# This script is used to run the FastAPI application using Uvicorn.
