##########################################################################
# Author:               ValeruS
# Date:                 Septeber 2017
# Revised:
#
# upsBypass object class
#
# This program can be used under the GNU General Public License version 3
# You can find full information here: http://www.zenoss.com/oss
#
##########################################################################

__doc__="""upsBypass

upsBypass is a component of a upsCS1x1 Device

"""

from Globals import InitializeClass

from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne


class upsBypass(DeviceComponent, ManagedEntity):
    meta_type = portal_type = "upsBypass"

    upsBypassLineIndexText        = ''
    upsBypassVoltage              = 0
    upsBypassCurrent              = 0
    upsBypassPower                = 0

    _properties = ManagedEntity._properties + (
        {'id': 'upsBypassLineIndexText',       'type': 'string', 'mode': ''},
        {'id': 'upsBypassVoltage',             'type': 'int',    'mode': ''},
        {'id': 'upsBypassCurrent',             'type': 'float',  'mode': ''},
        {'id': 'upsBypassPower',               'type': 'int',    'mode': ''},
    )

    _relations = ManagedEntity._relations + (
        ('upsDevBypass', ToOne(ToManyCont, 'ZenPacks.community.upsCS1x1.upsDevice', 'upsBypass', ),),
    )

    # Defining the "perfConf" action here causes the "Graphs" display to be
    # available for components of this type.
    factory_type_information = ({
        'id'             : 'upsBypass',
        'meta_type'      : 'upsBypass',
        'description'    : """upsBypass info""",
        'product'        : 'upsCS1x1',
        'immediate_view' : 'viewupsBypass',
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
        return self.upsDevBypass()

InitializeClass(upsBypass)
