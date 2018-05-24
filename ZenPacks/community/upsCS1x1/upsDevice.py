##########################################################################
# Author:               ValeruS
# Date:                 September 2017
# Revised:
#
# upsCS1x1 Device object class
#
# This program can be used under the GNU General Public License version 3
# You can find full information here: http://www.zenoss.com/oss
#
##########################################################################


from Globals import InitializeClass

from Products.ZenModel.Device import Device
from Products.ZenRelations.RelSchema import ToManyCont, ToOne
from Products.ZenModel.ZenossSecurity import ZEN_VIEW

from copy import deepcopy

class upsDevice(Device):
    "upsCS1x1 Device"
    meta_type = portal_type = 'upsDevice'


    _relations = Device._relations + (
        ('upsBattery',       ToManyCont(ToOne, 'ZenPacks.community.upsCS1x1.upsBattery',       'upsDevBattery',),),
        ('upsInput',         ToManyCont(ToOne, 'ZenPacks.community.upsCS1x1.upsInput',         'upsDevInput',),),
        ('upsOutput',        ToManyCont(ToOne, 'ZenPacks.community.upsCS1x1.upsOutput',        'upsDevOutput',),),
        ('upsBypass',        ToManyCont(ToOne, 'ZenPacks.community.upsCS1x1.upsBypass',        'upsDevBypass',),),
    )

InitializeClass(upsDevice)
