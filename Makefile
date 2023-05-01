run format:
	black . & isort .

run requirements:
	pip freeze --local > requirements.txt
