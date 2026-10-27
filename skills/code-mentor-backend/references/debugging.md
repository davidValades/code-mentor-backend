# Debugging to find the cause

Start with a reproducible case: input, expected/observed results, exact failure message. Without a visible error, find the first point where data loses its expected value.

In Visual Studio 2022, guide one operation at a time; explain its purpose:

1. Set a breakpoint before the suspected decision.
2. Reproduce; verify execution stops on the expected path.
3. Inspect parameters/values in Locals or Watch. Predict before observing.
4. Choose Step Into or Step Over according to whether entering a call is needed. Identify the shown button's option; avoid potentially variable shortcuts.
5. Consult the call stack to explain arrival here.
6. Test a specific hypothesis; choose the next observation from the result.

“Look at the result of this call to check whether the missing value originates here” is a useful instruction. “Put breakpoints everywhere” does not define a hypothesis.

Read actual types/values. A variable named result may contain error, absence, or valid data according to its contract. Examine exception message, type, stack trace, and relevant inner exception.

When evidence points to the cause, ask the learner for the smallest change. Check original reproduction, normal case, and related regression. Report code-only inspection as static review; preserve actual output when built/run. Before understanding the cause, never suggest architecture changes, exception handlers, or default returns.

During a voice journey, use a short oral case on choosing the next observation. Reserve IDE execution for a computer session; never credit the oral case as completed IDE execution.

## Choosing the first observation point

Classify provisionally by evidence:

| Evidence | First observation |
| --- | --- |
| Compilation failure | Exact diagnostic and location |
| Exception | Type, message, stack trace |
| Failing test | Assertion and expected/observed result |
| Unexpected HTTP response | Request, route, response-decision point |

A 404 alone cannot distinguish routing failure from lookup failure. Ask for one piece at a time; change hypotheses when observations contradict them. For project defects, first check the owning component and relevant configuration.

