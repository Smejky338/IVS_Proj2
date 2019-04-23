## @file Makefile
# @brief makefile - k jednoduchemu spusteni casti programu, zabaleni, vycisteni, testovani, ..
# @author Veronika Svítková xsvitk00 
# @date April 2019
# spusteni sa pres prikazovy radek prikazem make

all: run

run: gui.py
	python gui.py

#todo zabali projekt na odovzdanie
pack: clean doc
	mkdir ../../doc
	mv ../doc/html ../../doc
	rm -r ../doc
	mkdir ../../install
	cp ../../setup_kalk.exe ../../install
	mkdir ../../repo
	cp -r ../* ../../repo
	mkdir ../../xsmejk27_xdvora2z_xsvitk00_xkonde04
	mv ../../repo ../../doc ../../install ../../xsmejk27_xdvora2z_xsvitk00_xkonde04
	zip -r ../../xsmejk27_xdvora2z_xsvitk00_xkonde04.zip ../../xsmejk27_xdvora2z_xsvitk00_xkonde04
	
	

#todo zmaze subory co nemaju byt odovzdane
clean:	
	rm -rf ../__pycache__

#todo
doc:
	doxygen Doxyfile

test: test_mat_knihovna.py
	pytest test_mat_knihovna.py

profile: profiling.py
	python profiling.py <../profiling/test100.txt
