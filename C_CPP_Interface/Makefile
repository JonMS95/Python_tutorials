# --------------------------------------
# Makefile — Build .so directly from .c
# --------------------------------------

CC       := gcc
CFLAGS   := -Wall -Wextra -O2 -fPIC -fvisibility=hidden
LDFLAGS  := -shared

SRC      := $(wildcard *.c)
SOFILES  := $(SRC:.c=.so)

# Default target: build all .so files
all: $(SOFILES)

# Rule: file.c -> file.so
%.so: %.c
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ $<

# Clean generated .so files
clean:
	rm -f *.so

.PHONY: all clean
