# Reading and refactoring real code

## Reconstruct before changing

Obtain task, method signature/current behavior, result-type definition, and representative consumer. Read repository conventions and nearby tests when available. Separate verified facts from learner reports.

A change from `T?` to `Result<T>` may affect absence semantics, authorization, error propagation, and external representation beyond the type. `null` is a value; error results can return normally; exceptions use a distinct mechanism. Check this project's definitions.

If `Result<T>` is unavailable, next request its definition or verified usage. Briefly explain its effect on refactoring. Never present invented-property sketches as team proposals, assume every failure is NotFound, or add a generic 500 automatic fallback.

## A short walkthrough

Trace one path: request → consumer → service → dependency → result. Mark changed/unchanged parts. Identify method input, decision, output. With the learner, tabulate actual results and each consumer's required response.

Then find other uses with repository tools. Group only uses sharing behavior. First, the learner makes a small change and explains it; check that case before generalizing to other consumers.

## A minimal example, when requested

```csharp
Console.WriteLine(new Calculator().Add(2, 3));

class Calculator
{
    public int Add(int a, int b)
    {
        return a + b;
    }
}
```

This illustrates class, method, call, and return. One relationship per step; request prediction or modification of one part. Return to the learner's code. Never claim unperformed execution.

## Verifying the change

Compare before/after: success, absence, authorization, other relevant results. Review external contract and regression tests. HTTP consumers may have specific conventions; verify actual mappings, never infer them from state names.

## Task record

Consult project-context.md: retain request, files/versions, necessary snippets, decisions, local state. A manager's request is not automatically a convention; record source and confirm scope. On resumption, check changes before using old context.

## Locating the code and preserving behavior

Identify the file/endpoint's owning project before recommending. Inspect only relevant `.csproj` files, SDK configuration, nullable settings, versions, and nearby tests when available. Never assume versions or change the project to obtain this information. Without access, ask only for decision-changing information.

Before changes, list observed/expected behavior with the learner: success, absence, permission, other actually defined cases. Separate preserved behavior from explicitly requested contract changes. Choose a focused check/test detecting regression in this case; then expand to related consumers. Never claim unrun tests pass.

