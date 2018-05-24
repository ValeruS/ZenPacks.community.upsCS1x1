##########################################################################
# Author:               ValeruS
# Date:                 Septeber 2017
# Revised:
#
# upsOutput object class
#
# This program can be used under the GNU General Public License version 3
# You can find full information here: http://www.zenoss.com/oss
#
##########################################################################

__doc__="""upsOutput

upsOutput is a component of a upsCS1x1 Device

"""

from Globals import InitializeClass

from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne


class upsOutput(DeviceComponent, ManagedEntity):
    meta_type = portal_type = "upsOutput"

    upsOutputLineIndexText       = ''
    upsOutputVoltage             = 0
    upsOutputCurrent             = 0
    upsOutputPower               = 0
    upsOutputPercentLoad         = 0

    _properties = ManagedEntity._properties + (
        {'id': 'upsOutputLineIndexText',      'type': 'string', 'mode': ''},
        {'id': 'upsOutputVoltage',            'type': 'int',    'mode': ''},
        {'id': 'upsOutputCurrent',            'type': 'float',  'mode': ''},
        {'id': 'upsOutputPower',              'type': 'int',    'mode': ''},
        {'id': 'upsOutputPercentLoad',        'type': 'int',    'mode': ''},
    )

    _relations = ManagedEntity._relations + (
        ('upsDevOutput', ToOne(ToManyCont, 'ZenPacks.community.upsCS1x1.upsDevice', 'upsOutput', ),),
    )

    # Defining the "perfConf" action here causes the "Graphs" display to be
    # available for components of this type.
    factory_type_information = ({
        'id'             : 'upsOutput',
        'meta_type'      : 'upsOutput',
        'description'    : """upsOutput info""",
        'product'        : 'upsCS1x1',
        'immediate_view' : 'viewupsOutput',
        'actions'        : 
        (
           {'id'            : 'perfConf',
            'name'          : 'Template',
            'action'        : 'objTemplates',
            'permissions'   : (ZEN_CHANGE_DEVICE,),
           },
        ),
    },)


    # Custom components must always implement the device method. The method
    # should return the device object that contains the component.
    def device(self):
        return self.upsDevOutput()

InitializeClass(upsOutput)
