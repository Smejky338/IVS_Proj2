## @file profiling.py
# @brief program pro spusteni profilovani programu stddev.py
# priklad spusteni: python3 profiling.py <test1000.txt
# @author Jan Smejkal, xsmejk27

import profile
import stddev

profile.run('stddev.odchylka()')#spusteni odchylky
#spusteni profilingu napriklad takto: python3 profiling.py <test1000.txt