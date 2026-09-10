<html>
  <head>
    <body
      ><h1> 1. Balanced Brackets </h1>
    </body>
  </head>
</html>

Brackets close in the reverse order they open — that's a stack (LIFO), basically by definition.

Push every opening bracket. On a closing bracket, check the top of the stack: if it matches, pop and continue; if not (or the stack's empty), fail immediately. At the end, a non-empty stack means something was never closed — also a fail.

Counting bracket types instead wouldn't work — `([)]` has balanced counts but wrong order. The stack is what actually enforces "last opened, first closed."

**Complexity:** O(n) time, O(n) space worst case.

OUTPUT:
![image alt](https://github.com/GovindGaur-2006/TJ-Tasks-2026-Govind_Gaur/blob/c8d87ec9e5d0257c74d1e4c0f979da321dc2a056/easy_1.png)


<html>
  <head>
    <body
      ><h1> 2. Second Largest Distinct Element </h1>
    </body>
  </head>
</html>

Sorting and grabbing the second-from-last unique value works, but it's O(n log n) for something a single pass can do.

Instead I track two variables, `largest` and `second`, while scanning once:

- Equal to `largest`? Skip — it's a duplicate.
- Bigger than `largest`? Old `largest` becomes `second`, this becomes the new `largest`.
- Otherwise, bigger than `second`? It becomes the new `second`.

The duplicate check matters — without it, `[7, 7]` would wrongly look like it has a second largest of 7. If `second` never gets set, print `-1`.

**Complexity:** O(n) time, O(1) space.

OUTPUT:
![image alt](https://github.com/GovindGaur-2006/TJ-Tasks-2026-Govind_Gaur/blob/main/README.md)


<html>
  <head>
    <body
      ><h1> 3. Subarray Sum Equals K </h1>
    </body>
  </head>
</html>

The array can have negatives, which rules out a sliding window (it only works when the sum grows monotonically as the window expands). So this needs prefix sums + a hashmap instead.

If `prefix[j]` is the running sum up to index `j`, a subarray from `i+1` to `j` sums to `prefix[j] - prefix[i]`. I want that to equal `K`, so I'm really looking for earlier prefix sums equal to `prefix[j] - K`.

So while scanning left to right: keep a running prefix sum, look up how many times `prefix - K` has occurred so far (that's how many valid subarrays end here), then record the current prefix sum and continue.

Important detail: seed the hashmap with `{0: 1}` before starting, or subarrays starting at index 0 get missed.

**Complexity:** O(n) time, O(n) space worst case.

OUTPUT:
![image alt](https://github.com/GovindGaur-2006/TJ-Tasks-2026-Govind_Gaur/blob/08207b523b0691970e2236414eb1240176005b32/medium_1.png)
