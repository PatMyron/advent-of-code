workflow "New workflow" {
  on = "push"
  resolves = ["pylint", "black", "pocket-lint"]
}

action "pocket-lint" {
  uses = "PatMyron/pocket-lint@master"
}

action "pylint" {
  uses = "cclauss/GitHub-Action-for-pylint@master"
  args = "pip install -r requirements.txt; pylint **/*.py"
  needs = ["pocket-lint"]
}

action "black" {
  uses = "lgeiger/black-action@master"
  args = ". --check"
  needs = ["pylint"]
}
