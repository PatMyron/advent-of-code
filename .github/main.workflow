workflow "New workflow" {
  on = "push"
  resolves = ["Python Syntax Checker", "Lint"]
}

action "Python Syntax Checker" {
  uses = "cclauss/Find-Python-syntax-errors-action@0.1.2"
}

action "Lint" {
  uses = "lgeiger/pyflakes-action@master"
}
