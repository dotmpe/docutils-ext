#!/bin/bash


# Add fallbacks for non-std BATS functions

type fail >/dev/null 2>&1 || {
  fail()
  {
    test -z "$1" || echo "Reason: $1" >> $BATS_OUT
    exit 1
  }
}

type diag >/dev/null 2>&1 || {
  # Note: without failing test, output will not show up in std Bats install
  diag()
  {
    BATS_TEST_DIAGNOSTICS=1
    echo "$1" >>"$BATS_OUT"
  }
}

type TODO >/dev/null 2>&1 || { # tasks:no-check
  TODO() # tasks:no-check
  {
    test -n "$TODO_IS_FAILURE" && {
      ( 
          test -z "$1" &&
              "TODO ($BATS_TEST_DESCRIPTION)" || echo "TODO: $1"  # tasks:no-check
      )>> $BATS_OUT
      exit 1
    } || {
      # Treat as skip
      BATS_TEST_TODO=${1:-1}
      BATS_TEST_COMPLETED=1
      exit 0
    }
  }
}

type stdfail >/dev/null 2>&1 || {
  stdfail()
  {
    test -n "$1" || set -- "Unexpected. Status"
    fail "$1: $status, output(${#lines[@]}) is '${lines[*]}'"
  }
}

type pass >/dev/null 2>&1 || {
  pass() # a noop() variant..
  {
    return 0
  }
}

type test_ok_empty >/dev/null 2>&1 || {
  test_ok_empty()
  {
    test ${status} -eq 0 && test -z "${lines[*]}"
  }
}

type test_ok_nonempty >/dev/null 2>&1 || {
  test_ok_nonempty()
  {
    test ${status} -eq 0 && test -n "${lines[*]}" && {
      test -z "$1" || fnmatch "$1" "${lines[*]}"
    }
  }
}

type test_nok_nonempty >/dev/null 2>&1 || {
  test_nok_nonempty()
  {
    test ${status} -ne 0 &&
    test -n "${lines[*]}" && {
      test -z "$1" || {
        case "$1" in
          # Test line-count if number given
          "[0-9]"* ) test "${#lines[*]}" = "$1"  || return $? ;;
          # Test line-glob-match otherwise
          * ) case "${lines[*]}" in $1 ) ;; * ) return 1 ;; esac
            ;;
        esac
      }
    }
  }
}



test -n "$uname" || export uname="$(uname -s)"

filesize()
{
  while test $# -gt 0
  do
    case "$uname" in
      Darwin )
          stat -L -f '%z' "$1" || return 1
        ;;
      Linux )
          stat -L -c '%s' "$1" || return 1
        ;;
      * ) error "filesize: $1?" 1 ;;
    esac; shift
  done
}
