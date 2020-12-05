# Contributing Tada

## Add New Features to Tada

You can follow these steps to add a new feature if you are already a
collaborator on the project. First, you should create and publish your new branch
via the following command. Substitute the name of your feature/branch for the word
`feature-name`.

- `git checkout -b feature-name`
- `git checkout master`
- `git push -u origin feature-name`

To install development dependencies, type the following commands in the terminal:

```bash
poetry install
```

You can activate the shell with the following command:

```shell
poetry shell
```

Finally, you should open a pull request on the GitHub repository for the new
branch that you have created. This pull request should describe the new feature
that you are adding and give examples of how to run it on the command line.
Of course, if you are not a collaborator on this project, then you will need to
fork the repository, add your new feature, document and test it as appropriate,
and then create a pull request similarly.

We highly recommend you to provide tests along with the feature that you
implemented and you should not break the existing test cases or features.

### Test Tada

To run the test suite for Tada's functions within the shell by typing the
following in your terminal window:

```shell
pytest
```

If you want to collect the coverage of the provided test suite, then you can
run:

```shell
pytest --cov-config pytest.cov --cov
```

If you want to collect the coverage of the provided test suite and see what
lines of code are not covered, then you can run:

```shell
pytest --cov-config pytest.cov --cov --cov-report term-missing
```
