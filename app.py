if __name__ == "__main__":
    import uvicorn
    # Use port 10000 (standard for Render) or read from environment variable
    import os
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run("app:app", host="0.0.0.0", port=port)
