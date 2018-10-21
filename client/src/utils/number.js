/**
 * Light implementation of Python's range function.
 *
 * @param n Length of generated range array
 * @returns {number[]} Array from 0 to n - 1 ([0, 1, ..., n-1])
 */
export function range(n) {
  return [...Array(n).keys()];
}
