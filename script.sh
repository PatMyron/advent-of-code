#!/usr/bin/env bash
ulimit -s 40000; ulimit -a; for d in 2*; do (cd $d; pwd; ls * | xargs -n 1 time python); done;