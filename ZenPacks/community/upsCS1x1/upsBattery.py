##########################################################################
# Author:               ValeruS
# Date:                 Septeber 2017
# Revised:
#
# upsBattery object class
#
# This program can be used under the GNU General Public License version 3
# You can find full information here: http://www.zenoss.com/oss
#
##########################################################################

__doc__="""upsBattery

upsBattery is a component of a upsCS1x1 Device

"""

from Globals import InitializeClass

from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne


class upsBattery(DeviceComponent, ManagedEntity):
    meta_type = portal_type = "upsBattery"

    upsBatteryStatus               = 0
    upsBatteryStatusText           = ''
    upsSecondsOnBattery            = 0
    upsEstimatedMinutesRemaining   = 0
    upsEstimatedChargeRemaining    = 0
    upsBatteryVoltage              = 0
    upsBatteryCurrent              = 0
    upsBatteryTemperature          = 0
    upsTestResultsSummary          = 0
    upsTestResultsSummaryText      = 0

    _properties = ManagedEntity._properties + (
        {'id': 'upsBatteryStatus',              'type': 'int',    'mode': ''},
        {'id': 'upsBatteryStatusText',          'type': 'string', 'mode': ''},
        {'id': 'upsSecondsOnBattery',           'type': 'int',    'mode': ''},
        {'id': 'upsEstimatedMinutesRemaining',  'type': 'int',    'mode': ''},
        {'id': 'upsEstimatedChargeRemaining',   'type': 'int',    'mode': ''},
        {'id': 'upsBatteryVoltage',             'type': 'int',    'mode': ''},
        {'id': 'upsBatteryCurrent',             'type': 'float',  'mode': ''},
        {'id': 'upsBatteryTemperature',         'type': 'int',    'mode': ''},
        {'id': 'upsTestResultsSummary',         'type': 'int',    'mode': ''},
        {'id': 'upsTestResultsSummaryText',     'type': 'string', 'mode': ''},
    )

    _relations = ManagedEntity._relations + (
        ('upsDevBattery', ToOne(ToManyCont, 'ZenPacks.community.upsCS1x1.upsDevice', 'upsBattery', ),),
    )

    # Defining the "perfConf" action here causes the "Graphs" display to be
    # available for components of this type.
    factory_type_information = ({
        'id'             : 'upsBattery',
        'meta_type'      : 'upsBattery',
        'description'    : """upsBattery info""",
        'product'        : 'upsCS1x1',
        'immediate_view' : 'viewupsBattery',
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
        return self.upsDevBattery()

InitializeClass(upsBattery)
