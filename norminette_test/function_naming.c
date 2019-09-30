#include <stdio.h>

void foo_1 (void) {
    printf("foo\n");
}

void foo_2 (foo) {
    printf("foo2\n");
}

void foo_3 (void) {
    printf("foo3\n");
}

void foo_4 (void) {
    printf("foo4\n");
}

void main (void) {
    printf("foo\n");
}