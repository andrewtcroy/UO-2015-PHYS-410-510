#
# this is a comment

#
# define environment variables (compilers/linker/libraries...)
CC = ipython
FC = ifort
FFLAGS = -c
LIBS =

#
# define targets

all:
	$(CC) hello.py

