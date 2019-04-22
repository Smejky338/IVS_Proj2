# Makefile
# spusta sa cez prikazovy riadok prikazom make



all: run

run: gui.py
	python gui.py

#todo zabali projekt na odovzdanie
pack:

#todo zmaze subory co nemaju byt odovzdane
clean:

#todo
doc:
	doxygen Doxyfile

test: test_mat_knihovna.py
	pytest test_mat_knihovna.py

profile: profiling.py
	python profiling.py <../profiling/test100.txt