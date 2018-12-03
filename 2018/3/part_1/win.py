#!/usr/bin/env python

class Sheet(object):

    def __init__(self):
        # Columns go inside the rows (point is a set containing which numbers are claiming that point)
        # Starting with 1x1 sheet
        self.rows = [[set()]]

        self._expand_sheet(2000, 2000)

    def designate_sheet(self, designator, col, row, wide, tall):
        # Make sure it can fit
        #self._expand_sheet(row = row + tall + 1, col = col + wide + 1)

        for i in range(row, row + tall):
            for j in  range(col, col+wide):
                self.rows[i][j].add(designator)


    def _expand_sheet(self, row, col):
        """Given int row/col, expand the sheet so that it fits."""
        
        # Columns
        current_col_length = len(self.rows[0])
        if current_col_length <= col:
            for row_iter in self.rows:
                row_iter += [set() for _ in range(col - current_col_length + 1)]

        # Add rows if needed
        if len(self.rows) <= row:
            self.rows += [ 
                    [set() for _ in range(col+1)]
                    for _ in range(row - len(self.rows) + 1) ]

    def __str__(self):
        """String picture of the sheet."""
        table = PrettyTable([str(x) for x in range(len(self.rows[0]))])
        table.header = False
        table.border = False

        for row in self.rows:
            table.add_row(row)

        return str(table)

from prettytable import PrettyTable
from copy import copy, deepcopy
import re

with open("../input", "r") as f:
    inp = f.read().strip()

s = Sheet()

# Regex magic for fun
for designator, col, row, wide, tall in re.findall('#(\d+) @ *(\d+?),(\d+?): (\d+?)x(\d+).*\n', inp+"\n"):
    s.designate_sheet(
            int(designator), col=int(col), row=int(row), wide=int(wide) ,tall=int(tall))


# Calculate overlap
overlap = 0
for i in s.rows:
    for j in i:
        if len(j) > 1:
            overlap += 1

print("Overlap: " + str(overlap))
