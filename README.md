# Fuzzer

A Python-based network fuzzer for automated URL/path discovery and
HTTP response analysis.

## Overview

This project implements a basic network fuzzer that generates different
URL candidates from a given wordlist and checks their HTTP responses.

For example, given:

python3 project4.py -u http://ffuf.me/cd/basic/FUZZ -mc 200 -w common-reduced.txt

output:
200 http://ffuf.me/cd/basic/class 
200 http://ffuf.me/cd/basic/development.log 
