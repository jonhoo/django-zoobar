Progress on deliverables:

  - We have implemented a near-identical version of Zoobar running on Django.
    https://github.com/jonhoo/django-zoobar
  - We have implemented the necessary Django overrides (similar to symflask) that
    synthesize requests and preserve symbolic ints and strings.
  - We can perform the same Lab 3 concolic execution tests on our version of
    Zoobar running on top of Django, and identify the same bugs as were found
    in Lab 3.

Next steps:

  - We need to implement symbolic versions of more operations on ints and strings
    to be sure Django isn't using those operations internally and thus losing
    symbolic representation.
  - Likewise, we need to expand the set of database queries on Django that support
    concolic execution.
  - We would like to devise invariants for other Django-based applications,
    so that we may test them using our concolic execution framework.

Ideas for improvements:

  - We found that different branch conditions can yield the same solution as input
    to the concolic system. Preventing these duplicate executions would decrease the
    number of iterations in Lab 3 threefold.
  - The lab code has some elementary support for optimizing/reducing constraint
    expressions. The optimizations mentioned in the KLEE paper could be implemented
    in a similar spirit, and their runtime savings measured.
  - Several interactive web applications require multiple requests to expose certain
    bugs. Currently, the testing framework only executes single requests, which limits
    the types of invariants that can be expressed.

Observations about goals:

  - Implementing concolic execution for Django took a long time, even though
    the resulting mocking code is fairly small. Much of this is due to tracking
    down where symbolic values are lost.
  - There seems to be sufficient room for improvement in just running concolic
    execution on Django that expanding z3 to have native database support may
    not be worthwhile.
