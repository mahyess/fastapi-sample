start:
	uvicorn main:app --reload

server:
	uvicorn main:app --host 0.0.0.0 --port 80
