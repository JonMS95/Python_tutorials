check		= checkIntSign
square		= squareNumber

src_check	= C_Source_files/$(check).c
src_square	= C_Source_files/$(square).c

so_check	= C_Dynamic_libraries/lib$(check).so
so_square	= C_Dynamic_libraries/lib$(square).so

all: clean check.so square.so

check.so: $(src_check)
	gcc -g -fPIC -shared $(src_check) -o $(so_check)

square.so: $(src_square)
	gcc -g -fPIC -shared $(src_square) -o $(so_square)

clean:
	rm -rf C_Dynamic_libraries/*