
#                Copyright JF Pelland 2024.
# Distributed under the Boost Software License, Version 1.0.
#    (See accompanying file LICENSE_1_0.txt or copy at
#          https://www.boost.org/LICENSE_1_0.txt)

import os

from glyphDefinitions import *

maxColumnNum = 8
iconWidth = 64

def addListSub(offset: int, paths: list[str]) -> str:
    row1 = '|'
    row2 = '|'
    row3 = '|'
    for i, path in enumerate(paths):
        basename = os.path.basename(path)
        row1 += f' `U+{(offset+i):04X}` |'
        row2 += ' :---: |'
        row3 += f' <img src="{path}" title="{basename}" alt="{basename}" width="{iconWidth}"/> |'
    return f'{row1}\n{row2}\n{row3}'
    
def addList(title: str, offset: int, paths: list[str]) -> str:
    output = f'### {title}\n\n'
    for i in range(0, len(paths), maxColumnNum):
        output += addListSub(offset+i, paths[i : (i+maxColumnNum)]) + '\n\n'
    return output

table = '## Font Table\n\nA list of all icons included as well as the Unicode code point assigned to them in the font files included in the releases.\n\n'
table +=  addList(f'CPU ({cpuFolder})', cpuOffset, cpuSVGs)
table +=  addList(f'CPU Cores ({cpuFolder}cores/)', cpuCoreOffset, cpuCoreSVGs)
table +=  addList(f'GPU ({gpuFolder})', gpuOffset, gpuSVGs)
table +=  addList(f'Motherboard ({moboFolder})', moboOffset, moboSVGs)
table +=  addList(f'RAM ({ramFolder})', ramOffset, ramSVGs)
table +=  addList(f'Logical Drives ({logicalDrivesFolder})', logicalDrivesOffset, logicalDriveSVGs)
table +=  addList(f'Drive Letters ({logicalDrivesFolder}letters)', logicalDriveLettersOffset, logicalDriveLettersSVGs)
table +=  addList(f'Recycling Bin ({miscFolder})', binOffset, binSVGs)
table +=  addList(f'Fan ({miscFolder})', fanOffset, fanSVGs)
table +=  addList(f'Water Pump ({miscFolder})', waterPumpOffset, waterPumpSVGs)
table +=  addList(f'Networking ({networkFolder})', networkOffset, networkSVGs)
table +=  addList(f'Statistics ({statsFolder})', statsOffset, statsSVGs)
table +=  addList(f'Time ({statsFolder}time)', clocksOffset, clocksSVGs)
table +=  addList(f'Miscellaneous ({miscFolder})', miscOffset, miscSVGs)

print(table)
