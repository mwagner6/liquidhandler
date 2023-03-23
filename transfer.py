from opentrons import protocol_api

metadata = {
    'protocolName': 'transfer10',
    'author': 'Max Wagner <max.wagner.us@gmail.com>',
    'description': 'transfew 10ul to dilution plate',
    'apiLevel': '2.13'
}



def run(protocol: protocol_api.ProtocolContext):

    #labware
    plateOld = protocol.load_labware('nest_96_wellplate_200ul_flat', location='1')
    plateNew = protocol.load_labware('corning_96_wellplate_360ul_flat', location='2')
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



    for r in range(1, 9):
        tipind = "A" + str(r)
        left.pick_up_tip(tiprack[tipind])
        for c in range(1, 9):
            ind = letterTable[r] + str(c)
            left.aspirate(10, plateOld[ind])
            left.dispense(290, plateNew[ind])
        left.drop_tip()

            