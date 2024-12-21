include .env
export

# enumeration of * .py files storage or folders is required.
files_to_format 	?= app tests
files_to_check 	?= app tests

## Default target
.DEFAULT_GOAL := run

## Build api docker containers
docker_up:
	docker-compose up --build -d

run:
	uvicorn app:create_app --host localhost --reload --port ${API__PORT}

## Format all
format: remove_imports isort black docformatter add-trailing-comma

## Check code quality
check: flake8 black_check docformatter_check safety bandit

## Migrate database
migrate:
	poetry run python -m scripts.migrate

## Rollback migrations in database
migrate-rollback:
	poetry run python -m scripts.migrate --rollback

migrate-reload:
	poetry run python -m scripts.migrate --reload

## Remove unused imports
remove_imports:
	autoflake -ir --remove-unused-variables \
		--ignore-init-module-imports \
		--remove-all-unused-imports \
		${files_to_format}


## Sort imports
isort:
	isort ${files_to_format}


## Format code
black:
	black ${files_to_format}


## Check code formatting
black_check:
	black --check ${files_to_check}


## Format docstring PEP 257
docformatter:
	docformatter -ir ${files_to_format}


## Check docstring formatting
docformatter_check:
	docformatter -cr ${files_to_check}


## Check pep8
flake8:
	flake8 ${files_to_check}


## Check typing
mypy:
	mypy ${files_to_check}


## Check if all dependencies are secure and do not have any known vulnerabilities
safety:
	safety check --full-report -i 35015 -i 59473 -i 53048


## Check code security
bandit:
	bandit -r ${files_to_check} -x tests

## Add trailing comma works only on unix.
# an error is expected on windows.
add-trailing-comma:
	find app tests -name "*.py" -exec add-trailing-comma '{}' --py36-plus \;
