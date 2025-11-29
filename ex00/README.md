Timsort - O(n log n) - Worst, O(n) - Best
Merge Sort - O(n log n) - All
Insertion Sort - O(n²) - All

Tests:
10 iterations,
10 000 numbers in each dataset

==============================
Dataset:  Random
==============================
Timsort
MIN: 0.0011 seconds
MAX: 0.0013 seconds
AVR: 0.0012 seconds
SUM: 0.0115 seconds

Merge Sort
MIN: 0.0117 seconds
MAX: 0.0121 seconds
AVR: 0.0118 seconds
SUM: 0.1180 seconds

Insertion Sort
MIN: 1.6247 seconds
MAX: 1.7742 seconds
AVR: 1.6627 seconds
SUM: 16.6266 seconds


==============================
Dataset:  Sorted
==============================
Timsort
MIN: 0.0000 seconds
MAX: 0.0001 seconds
AVR: 0.0000 seconds
SUM: 0.0004 seconds

Merge Sort
MIN: 0.0089 seconds
MAX: 0.0098 seconds
AVR: 0.0092 seconds
SUM: 0.0917 seconds

Insertion Sort
MIN: 0.0006 seconds
MAX: 0.0007 seconds
AVR: 0.0006 seconds
SUM: 0.0061 seconds


==============================
Dataset:  Reversed
==============================
Timsort
MIN: 0.0000 seconds
MAX: 0.0001 seconds
AVR: 0.0000 seconds
SUM: 0.0005 seconds

Merge Sort
MIN: 0.0091 seconds
MAX: 0.0096 seconds
AVR: 0.0092 seconds
SUM: 0.0925 seconds

Insertion Sort
MIN: 2.8628 seconds
MAX: 3.0824 seconds
AVR: 2.9410 seconds
SUM: 29.4100 seconds