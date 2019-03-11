workflow "New workflow" {
  on = "push"
  resolves = ["pylint", "pyflakes", "black", "Flake8"]
}

action "Python Syntax Checker" {
  uses = "cclauss/Find-Python-syntax-errors-action@master"
}

action "pyflakes" {
  uses = "lgeiger/pyflakes-action@master"
}

action "pylint" {
  uses = "cclauss/GitHub-Action-for-pylint@master"
  args = "pylint"
}

action "Flake8" {
  uses = "cclauss/GitHub-Action-for-Flake8@master"
  args = "flake8 . --max-line-length=88"
}

action "black" {
  uses = "lgeiger/black-action@master"
  args = ". --check"
}
