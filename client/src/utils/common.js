/**
 * Error type for noticing that assertion is failed.
 */
class AssertionError extends Error {}

/**
 * Simple implementation of assert function.
 * Raise AssertionError if given expression is not true.
 *
 * @param shouldBeTrue boolean expression that should be true
 * @param msg
 */
export function assert(shouldBeTrue, msg = null) {
  if (shouldBeTrue) return;
  if (msg) throw new AssertionError(msg);
  else throw new AssertionError();
}
