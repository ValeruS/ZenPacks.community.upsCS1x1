##########################################################################
# Author:               ValeruS
# Date:                 Septeber 2017
# Revised:
#
# upsInput object class
#
# This program can be used under the GNU General Public License version 3
# You can find full information here: http://www.zenoss.com/oss
#
##########################################################################

__doc__="""upsInput

upsInput is a component of a upsCS1x1 Device

"""

from Globals import InitializeClass

from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne


class upsInput(DeviceComponent, ManagedEntity):
    meta_type = portal_type = "upsInput"

    upsInputLineIndexText        = ''
    upsInputFrequency            = 0
    upsInputVoltage              = 0
    upsInputCurrent              = 0
    upsInputTruePower            = 0

    _properties = ManagedEntity._properties + (
        {'id': 'upsInputLineIndexText',       'type': 'string', 'mode': ''},
        {'id': 'upsInputFrequency',           'type': 'float',  'mode': ''},
        {'id': 'upsInputVoltage',             'type': 'int',    'mode': ''},
        {'id': 'upsInputCurrent',             'type': 'float',  'mode': ''},
        {'id': 'upsInputTruePower',           'type': 'int',    'mode': ''},
    )

    _relations = ManagedEntity._relations + (
        ('upsDevInput', ToOne(ToManyCont, 'ZenPacks.community.upsCS1x1.upsDevice', 'upsInput', ),),
    )

    # Defining the "perfConf" action here causes the "Graphs" display to be
    # available for components of this type.
    factory_type_information = ({
        'id'             : 'upsInput',
        'meta_type'      : 'upsInput',
        'description'    : """upsInput info""",
        'product'        : 'upsCS1x1',
        'immediate_view' : 'viewupsInput',
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
        return self.upsDevInput()

InitializeClass(upsInput)
