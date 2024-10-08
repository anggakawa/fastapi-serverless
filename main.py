import uvicorn
from runner.app import create_app

app = create_app()

def main():
    uvicorn.run(app, host="0.0.0.0", port=5000)

if __name__ == "__main__":
    main()