# MyHealth

This is the repository used for the Agile assignment.

### Running tests

To run all the test from the Python app, including coverage report:

    $ py.test --cov-report=html --cov=app tests/ 

If you want to run a single test:

    $ pytest -k '<the_test>'