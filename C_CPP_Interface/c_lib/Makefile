# --------------------------------------
# Makefile for c_lib/
# Build .so files from src/
# Output into lib/
# --------------------------------------

CC       := gcc
CFLAGS   := -Wall -Wextra -O2 -fPIC -fvisibility=hidden -Iinclude
LDFLAGS  := -shared

SRC_DIR  := src
INC_DIR  := include
LIB_DIR  := lib

SRC      := $(wildcard $(SRC_DIR)/*.c)
SOFILES  := $(patsubst $(SRC_DIR)/%.c,$(LIB_DIR)/%.so,$(SRC))

# Default target
all: $(LIB_DIR) $(SOFILES)

$(LIB_DIR):
	mkdir -p $(LIB_DIR)

# src/file.c → lib/file.so
$(LIB_DIR)/%.so: $(SRC_DIR)/%.c
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ $<

clean:
	rm -f $(LIB_DIR)/*.so

.PHONY: all clean
