Progress on deliverables:

  - We have implemented a near-identical version of Zoobar running on Django
    https://github.com/jonhoo/django-zoobar
  - We have implemented necessary Django overrides (similar to symflask) to
    synthesize requests and preserve symbolic strings and ints 
  - We can perform the same lab3 concolic execution tests on our version of
    Zoobar running on top of Django, and identify the same bugs as were found
    in lab3.

Next steps:

 - Implement symbolic versions of more operations on ints and strings
 - Expand the set of database queries that can be performed in a symbolic
   execution friendly manner
 - Devise invariants for other Django-based applications, and test them using
   our concolic execution framework.

Ideas for improvements:

  - Preventing duplicate executions when different branch conditions yield the
    same sets of inputs has a potential to decrease the number of iterations in
    the Zoobar applications threefold.
  - We want to investigate some of the optimizations used by KLEE to see if
    that can further reduce the concolic execution time.
  - Many application bugs are likely to require multiple requests to be
    performed in order to be exposed. The testing framework currently only
    executes a single request, which limits the type of bugs it can find.

Observations about goals:

  - Implementing concolic execution for Django took a long time, even though
    the resulting mocking code is fairly small. Much of this is due to tracking
    down where symbolic values are lost.
  - There seem to be sufficient room for improvement in just running concolic
    execution on Django that expanding z3 to have native database support may
    not be worthwhil.
