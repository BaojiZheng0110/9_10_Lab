PYTHON = python3
TARGET = Baoji_Lab4_solution.py

run:
	$(PYTHON) $(TARGET)

test:
	$(PYTHON) $(TARGET)

clean:
	rm -rf __pycache__ *.pyc
