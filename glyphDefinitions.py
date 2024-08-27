
#                Copyright JF Pelland 2024.
# Distributed under the Boost Software License, Version 1.0.
#    (See accompanying file LICENSE_1_0.txt or copy at
#          https://www.boost.org/LICENSE_1_0.txt)

import itertools

baseFolder = './icons/'

cpuFolder = f'{baseFolder}cpu/'
gpuFolder = f'{baseFolder}gpu/'
moboFolder = f'{baseFolder}motherboard/'
ramFolder = f'{baseFolder}ram/'
logicalDrivesFolder = f'{baseFolder}drives/logical/'
networkFolder = f'{baseFolder}networking/'
statsFolder = f'{baseFolder}stats/'
miscFolder = f'{baseFolder}misc/'

cpuOffset = 0xf000
gpuOffset = 0xf010
moboOffset = 0xf020
ramOffset = 0xf030
logicalDrivesOffset = 0xf080
networkOffset = 0xf050
statsOffset = 0xf070
miscOffset = 0xf060
fanOffset = 0xf040
waterPumpOffset = 0xf048
binOffset = 0xf0b0

logicalDriveLettersOffset = 0xf090
clocksOffset = 0xf0d0
cpuCoreOffset = 0xf100

cpuCoreCount = 32
cpuCorePrefix = f'{cpuFolder}cores/CPU'

logicalDrivesCount = 26
logicalDrivesPrefix = f'{logicalDrivesFolder}letters/drive'

clockNumHours = 12
clockHourDivisions = 4
minuteIncrement = round(60 / clockHourDivisions)
clockPrefix = f'{statsFolder}time/Clock_'

iconList = [
    'Temp', 'Hotspot', 'Amps', 'Volts', 'Power', 'Fan',
    'WaterPump', 'Liquid', 'LiquidAlt', 'Flow',
]

cpuSVGs = [f'{cpuFolder}CPU.svg'] + \
    [f'{cpuFolder}CPU{icon}.svg' for icon in iconList]

gpuSVGs = [f'{gpuFolder}GPU.svg', f'{gpuFolder}GPUCore.svg', f'{gpuFolder}GPUMem.svg'] + \
    [f'{gpuFolder}GPU{icon}.svg' for icon in iconList]

moboSVGs = [f'{moboFolder}Mobo.svg', f'{moboFolder}MoboChipset.svg'] + \
    [f'{moboFolder}Mobo{icon}.svg' for icon in iconList]

ramSVGs = [f'{ramFolder}RAM.svg', f'{ramFolder}RAMSingle.svg', f'{ramFolder}RAMSingleAlt.svg'] + \
    [f'{ramFolder}RAM{icon}.svg' for icon in iconList]

logicalDriveSVGs = [f'{logicalDrivesFolder}Drive.svg'] + \
    [f'{logicalDrivesFolder}Drive{icon}.svg' for icon in iconList]


netTypes = ['Internet', 'Ethernet', 'Wifi']
netSuffixes = ['', 'Download', 'Upload', 'UpDown', 'UpDownAlt']
networkSVGs = [f'{networkFolder}{r[0]+r[1]}.svg' for r in itertools.product(netTypes, netSuffixes)]

statsSVGs = [
    f'{statsFolder}Clock.svg',
    f'{statsFolder}Timer.svg',
    f'{statsFolder}BarGraph.svg',
    f'{statsFolder}Graph.svg',
    f'{statsFolder}0.1_Percentile.svg',
    f'{statsFolder}1.0_Percentile.svg',
    f'{statsFolder}50_Percentile.svg',
    f'{statsFolder}99.0_Percentile.svg',
    f'{statsFolder}99.9_Percentile.svg',
]

fanSVGs = [
    f'{miscFolder}Fan.svg',
    f'{miscFolder}FanBlades.svg',
]

waterPumpSVGs = [
    f'{miscFolder}WaterPump.svg',
]

binSVGs = [
    f'{miscFolder}RecyclingBin.svg',
    f'{miscFolder}RecyclingBinFull.svg',
]

miscSVGs = [
    f'{miscFolder}Thermometer.svg',
    f'{miscFolder}Flame.svg',
    f'{miscFolder}AmpsDC.svg',
    f'{miscFolder}VoltsDC.svg',
    f'{miscFolder}Power.svg',
    f'{miscFolder}PowerFilled.svg',
    f'{miscFolder}WaterDrop.svg',
    f'{miscFolder}WaterDropFilled.svg',
    f'{miscFolder}WaterDrops.svg',
    f'{miscFolder}WaterDropsFilled.svg',
    f'{miscFolder}WaterFlow.svg',
]

cpuCoreSVGs = []
for i in range(cpuCoreCount+1):
    cpuCoreSVGs += [f'{cpuCorePrefix}{i:02}.svg']

logicalDriveLettersSVGs = []
for i in range(logicalDrivesCount):
    letter = chr(ord('A') + i)
    logicalDriveLettersSVGs += [f'{logicalDrivesPrefix}{letter}.svg']

clocksSVGs = []
for hours in range(clockNumHours):
    for num in range(clockHourDivisions):
        offset = (hours*clockHourDivisions) + num
        minutes = num * minuteIncrement
        clocksSVGs += [f'{clockPrefix}{hours:02}_{minutes:02}.svg']

if __name__ == '__main__':
    for key, value in globals().copy().items():
        if isinstance(value, list):
            print(f'{key}:')
            for item in value:
                print(f'\t{item}')
            print()
        else:
            print(f'{key}: {value}')
