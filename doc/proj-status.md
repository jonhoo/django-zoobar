What we have:
+ implement zoobar in django.
+ override portions of django to preserve symbolic strings during url
and request processing.
+ perform the same lab3 concolic execution tests on our django-fied zoobar.

What we are working on:
+ symbolic-fy additional operations on ints, strings, and databases
that django uses.
+ devise invariants for other django applications and test them on our
web app concolic execution api.

=========================

Below is a summary of what we discussed today. Please let me know if I
got anything wrong.

> clean up and document api for web app concolic execution.

> implement all string and int methods.
> support all (or more) database lookups.
> optimize the condition generation loop, see klee paper.
> clarify purpose of built-in symint.

> find other web apps and state invariants.
> support multi-request concolic checks.
> execute full range of zoobar urls.
