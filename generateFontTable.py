
#                Copyright JF Pelland 2024.
# Distributed under the Boost Software License, Version 1.0.
#    (See accompanying file LICENSE_1_0.txt or copy at
#          https://www.boost.org/LICENSE_1_0.txt)

from glyphDefinitions import *

maxColumnNum = 8
iconWidth = 64

def addListSub(offset: int, paths: list[str]) -> str:
    row1 = '|'
    row2 = '|'
    row3 = '|'
    for i, path in enumerate(paths):
        row1 += f' `U+{(offset+i):04X}` |'
        row2 += ' :---: |'
        row3 += f' <img src="{path}" width="{iconWidth}"> |'
    return f'{row1}\n{row2}\n{row3}'
    
def addList(title: str, offset: int, paths: list[str]) -> str:
    output = f'### {title}\n\n'
    for i in range(0, len(paths), maxColumnNum):
        output += addListSub(offset+i, paths[i : (i+maxColumnNum)]) + '\n\n'
    return output

table = '## Font Table\n\nA list of all icons included as well as the Unicode code point assigned to them in the font files included in the releases.\n\n'
table +=  addList('CPU', cpuOffset, cpuSVGs)
table +=  addList('CPU Cores', cpuCoreOffset, cpuCoreSVGs)
table +=  addList('GPU', gpuOffset, gpuSVGs)
table +=  addList('Motherboard', moboOffset, moboSVGs)
table +=  addList('RAM', ramOffset, ramSVGs)
table +=  addList('Drives', drivesOffset, driveSVGs)
table +=  addList('Drive Letters', driveLettersOffset, driveLettersSVGs)
table +=  addList('Recycling Bin', binOffset, binSVGs)
table +=  addList('Fan', fanOffset, fanSVGs)
table +=  addList('Water Pump', waterPumpOffset, waterPumpSVGs)
table +=  addList('Networking', networkOffset, networkSVGs)
table +=  addList('Statistics', statsOffset, statsSVGs)
table +=  addList('Time', clocksOffset, clocksSVGs)
table +=  addList('Miscellaneous', miscOffset, miscSVGs)

print(table)
