run:
	@uvicorn workout_api.main:app --reload
create-migrations:
	@PYTHOMPATH=SPYTHONPATH:$(pwd) alembic revision --autogenerate -m $(d)
run-migrations:
	@PYTHOMPATH=SPYTHONPATH:$(pwd) alembic upgrade head