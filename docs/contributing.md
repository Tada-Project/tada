# Contributing Tada

## Adding New Features to Tada

You can follow these steps to add a new feature if you are already a
collaborator on the project. If you want to add a new feature, please ensure
that it is accompanied by high coverage test cases and that you do not break any
of the existing test cases or features. First, you should type the following
command, substituting the name of your feature for the word `featurename`.

```bash
git checkout -b new-featurename
git checkout master
git push -u origin new-featurename
```

To install development dependencies, type the following command in the terminal:

```bash
pipenv install --dev
```

Finally, you should open a pull request on the GitHub repository for the new
branch that you have created. This pull request should describe the new feature
that you are adding and give examples of how to run it on the command line. Of
course, if you are not a collaborator on this project, then you will need to
fork the repository, add your new feature, document and test it as appropriate,
and then create a pull request.
