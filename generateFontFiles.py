
#                Copyright JF Pelland 2024.
# Distributed under the Boost Software License, Version 1.0.
#    (See accompanying file LICENSE_1_0.txt or copy at
#          https://www.boost.org/LICENSE_1_0.txt)

import os, fontforge

from glyphDefinitions import *

fontName = 'HardwareIcons'
outputFolder = './output/'
fontPath = f'{outputFolder}{fontName}'

def addGlyph(font: fontforge.font, pos: int, filename: str) -> None:
    glyph = font.createMappedChar(pos)
    glyph.importOutlines(filename)
    glyph.simplify()
    glyph.addExtrema('all')
    glyph.round()
    glyph.removeOverlap()
    glyph.correctDirection()
    
def addList(font: fontforge.font, startPos: int, filelist: list[str]) -> None:
    for i, file in enumerate(filelist):
        addGlyph(font, startPos+i, file)

if __name__ == '__main__':
    font = fontforge.font()
    font.copyright = 'HardwareIcons font and svg icons are licensed under SIL OFL 1.1. Code is licensed under Boost Software License 1.0'
    font.em = 1024
    font.encoding = 'UnicodeBMP'
    font.familyname = fontName
    font.fontname = fontName
    font.fullname = fontName

    addList(font, cpuOffset, cpuSVGs)
    addList(font, gpuOffset, gpuSVGs)
    addList(font, moboOffset, moboSVGs)
    addList(font, ramOffset, ramSVGs)
    addList(font, fanOffset, fanSVGs)
    addList(font, waterPumpOffset, waterPumpSVGs)
    addList(font, networkOffset, networkSVGs)
    addList(font, miscOffset, miscSVGs)
    addList(font, statsOffset, statsSVGs)
    addList(font, clocksOffset, clocksSVGs)
    addList(font, logicalDrivesOffset, logicalDriveSVGs)
    addList(font, logicalDriveLettersOffset, logicalDriveLettersSVGs)
    addList(font, mdot2DrivesOffset, mdot2DriveSVGs)
    addList(font, mdot2SmallDrivesOffset, mdot2SmallDriveSVGs)
    addList(font, sataDrivesOffset, sataDriveSVGs)
    addList(font, binOffset, binSVGs)
    addList(font, cpuCoreOffset, cpuCoreSVGs)
    
    if not os.path.exists(outputFolder):
        os.makedirs(outputFolder)
    font.save(f'{fontPath}.sfd')
    font.generate(f'{fontPath}.ttf')
    font.generate(f'{fontPath}.otf')
