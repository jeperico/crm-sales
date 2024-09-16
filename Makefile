makevenv:
	python3 -m venv .venv

deps:
	.venv/bin/pip install -r requirements.txt

# venv:
# 	source .venv/bin/activate

streamlit:
	streamlit run app.py

docs:
	mkdocs serve
