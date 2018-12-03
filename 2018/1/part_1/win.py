#!/usr/bin/env python

with open("../input","r") as f:
    inp = f.read()

inp = inp.replace("\n","")
inp = "0" + inp
inp.strip()
print(eval(inp))
