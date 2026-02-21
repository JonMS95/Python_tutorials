# --------------------------------------
# Makefile for cpp_lib/
# Build a single Pybind11 .so from all src/*.cpp
# Output into lib/
# --------------------------------------

CXX       := g++
CXXFLAGS  := -O3 -Wall -Wextra -fPIC -std=c++17 `python3 -m pybind11 --includes`
LDFLAGS   := -shared

LIB_NAME  := lib_cpp_linear_regression

SRC_DIR   := src
LIB_DIR   := lib
TARGET    := $(LIB_DIR)/$(LIB_NAME).so

# Find all .cpp files in SRC_DIR
SRC       := $(wildcard $(SRC_DIR)/*.cpp)

# Default target
all: $(LIB_DIR) $(TARGET)

# Create lib directory if missing
$(LIB_DIR):
	mkdir -p $(LIB_DIR)

# Compile all .cpp files into one shared library
$(TARGET):
	$(CXX) $(CXXFLAGS) $(LDFLAGS) -o $@ $(SRC)

# Clean up compiled .so
clean:
	rm -f $(TARGET)

.PHONY: all clean
