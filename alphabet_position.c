#include <stdio.h>

char alphabet_position(char c) {
    if (c >= 'a' && c <= 'z') {
        return c - 'a' + 1;
    }
    else {
        return 0;
    }
}

int main() {
    for (char c = 'a'; c <= 'z'; c++) {
        printf("%d\n", alphabet_position(c));

    }
    // printf("%d\n", alphabet_position('a')); // Output: 1
}