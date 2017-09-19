"""Global variables associated to the test suite."""

#: List of CPP variables that should be defined in config.h in order to enable this suite.
need_cpp_vars = [
]

#: List of keywords that are automatically added to all the tests of this suite. 
keywords = [
]

#: This suite contains tests executed with different numbers of MPI processes.
is_multi_parallel = True

#: List of input files
inp_files = [
"t01.in",
"t02.in",
"t03.in",
"t05.in",
"t06.in", 
]
