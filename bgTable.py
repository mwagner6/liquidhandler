from opentrons import protocol_api

metadata = {
    'protocolName': 'bgTable',
    'author': 'Max Wagner <max.wagner.us@gmail.com>',
    'description': '8x8 table blue/green',
    'apiLevel': '2.13'
}

sim = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

def run(protocol: protocol_api.ProtocolContext):

    #labware
    plate = protocol.load_labware('nest_96_wellplate_200ul_flat', location='2')
    tiprack = protocol.load_labware('geb_96_tiprack_300ul', location='5')
    tuberack = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', location='3')
    left = protocol.load_instrument('p300_single', mount='left', tip_racks=[tiprack])

    waterTube = 'A3'
    blueTube = 'B3'
    greenTube = 'B4'

    letterTable = {
        1:"A",
        2:"B",
        3:"C",
        4:"D",
        5:"E",
        6:"F",
        7:"G",
        8:"H"
    }

    left.pick_up_tip(tiprack['A1'])

    #water
    for r in range(1, 9):
        for c in range(1, 9):
            ind = letterTable[r] + str(c)
            amt = 300 - (10*(r-1) + 10*(c-1))
            left.aspirate(amt, tuberack[waterTube])
            left.dispense(amt, plate[ind])
    left.drop_tip()


    left.pick_up_tip(tiprack['A2'])

    #blue
    for r in range(1, 9):
        left.aspirate(280, tuberack[blueTube])
        for c in range(1, 9):
            ind = letterTable[r] + str(c)
            amt = 10*(c-1)
            if amt > 0:
                left.dispense(amt, plate[ind])
    left.drop_tip()


    left.pick_up_tip(tiprack['A3'])

    #green
    for c in range(1, 9):
        left.aspirate(280, tuberack[greenTube])
        for r in range(1, 9):
            ind = letterTable[r] + str(c)
            amt = 10*(r-1)
            if amt > 0:
                left.dispense(amt, plate[ind])
    left.drop_tip()