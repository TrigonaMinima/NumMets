/*
* in usual radix 3 separate arrays are used viz. output, offset, buffer
* http://codercorner.com/RadixSortRevisited.htm
* This implementation is an attempt to achieve that using 2 arrays viz. output and offset/buffer.
*/

# include <stdio.h>
# include <string.h>
# include <time.h>


void
radix(int input[], int max, int limit)
{
        int offset[limit], output[max], i, holder, sum=0;
        printf("%d\n", limit);
        memset(offset, 0, limit*sizeof(int));
        memset(offset, 0, limit*sizeof(int));
        for(i=0; i<max; i++)
                offset[input[i]]++;
        printf("sdfsd\n");

        holder = offset[0];
        offset[0] = 0;
        for (i = 1; i < limit; i++)
        {
                sum = offset[i-1] + holder;
                holder = offset[i];
                offset[i] = sum;
        }
        for(i=0; i<max; i++)
        {
                // holder = input[i];
                output[offset[input[i]]++] = input[i];
        }
        for (i = 0; i < max; i++)
                printf("%d ", output[i]);
}


int
main(int argc, char *argv[])
{
        // int limit = 65000;
        // int max = 65000;
        // ensure proper usage
        if (argc != 3)
        {
                printf("Incorrect usage!!\n");
                return 1;
        }
        int limit = atoi(argv[2]), max = atoi(argv[1]), size;
        int input[max];
        srand((unsigned int) time(NULL));
        for (size = 0; size < max; size++)
                input[size] = rand() % limit;
        radix(input, size, limit);
        printf("\n");
        return 0;
}

// 12 4 5 7 2 6 7 8 9 12 20 23 3 7

// 0 1 1 1 1 1 3 1 1 0   0   2   0   0   0   0   0   0  0   1   0   0  1

// 0 0 1 2 3 4 5 8 9 10 10 10 12 12 12 12 12 12 12 13 13 13 13

// 0 2 3 4 5 6 7 7 7 8 9 12 12 20 23