# --------------------------------------
# Makefile for cpp_lib/
# Build .so files from src/
# Output into lib/
# --------------------------------------

CXX       := g++
CXXFLAGS  := -Wall -Wextra -O2 -fPIC -std=c++17
LDFLAGS   := -shared

SRC_DIR   := src
LIB_DIR   := lib

# Get all cpp source files in src/
SRC       := $(wildcard $(SRC_DIR)/*.cpp)
SOFILES   := $(patsubst $(SRC_DIR)/%.cpp,$(LIB_DIR)/%.so,$(SRC))

# Default target
all: $(LIB_DIR) $(SOFILES)

# Create lib directory if it does not exist
$(LIB_DIR):
	mkdir -p $(LIB_DIR)

# Compile src/file.cpp → lib/file.so
$(LIB_DIR)/%.so: $(SRC_DIR)/%.cpp
	$(CXX) $(CXXFLAGS) $(LDFLAGS) -o $@ $<

# Clean compiled .so files
clean:
	rm -f $(LIB_DIR)/*.so

.PHONY: all clean
