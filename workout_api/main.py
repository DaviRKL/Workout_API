from fastapi import FastAPI

app = FastAPI(title='WorkoutApi')

if __name__ == 'main':
    import uvicorn

    uvicorn.run('main:app', host='0.0.0.0', port=0000, log_level='info', reload=True)