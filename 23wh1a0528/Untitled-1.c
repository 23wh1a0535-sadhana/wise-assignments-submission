#include <stdio.h>

#define SIZE 10

int main() {
   int array1[SIZE];
   int array2[SIZE];
   int i;

   printf("Enter %d elements in Array1: ", SIZE);
   for (i = 0; i < SIZE; i++) {
      scanf("%d", &array1[i]);
   }

   for (i = 0; i < SIZE; i++) {
      array2[i] = array1[i];
   }

   printf("Elements of Array1: ");
   for (i = 0; i < SIZE; i++) {
      printf("%d ", array1[i]);
   }

   printf("\nElements of Array2: ");
   for (i = 0; i < SIZE; i++) {
      printf("%d ", array2[i]);
   }
