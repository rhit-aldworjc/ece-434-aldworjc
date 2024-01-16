-include ./path.mak
CC := $(LINUXarm_GCC)
CFLAGS := -g
LINKER_FLAGS := -lstdc++

app.arm : app.o
	$(CC) $(CFLAGS) $(LINKER_FLAGS) app.o -o app.arm
	
%.o : %.c
	$(CC) $(CFLAGS) -c $< -o $@
	@echo; echo $@ successfully created; echo

.PHONY : clean
clean :
	rm -rf app.arm
	rm -rf app.o

.PHONY : all
all : app.arm	

.PHONY : test
test:
	@echo CC = $(CC)
