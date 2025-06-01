# run.py

import os
import uvicorn

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))

    uvicorn.run(
        "open_webui.main:app",
        host="0.0.0.0",
        port=port,
        reload=True,
        forwarded_allow_ips="*"
    )
# This script is used to run the FastAPI application using Uvicorn.
