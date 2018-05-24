##########################################################################
# Author:               ValeruS
# Date:                 September 2017
# Revised:
#
# upsBypassMap modeler plugin
#
# This program can be used under the GNU General Public License version 3
# You can find full information here: http://www.zenoss.com/oss
#
##########################################################################

__doc__ = """upsBypassMap

Gather table information from UPS info Modules based on UPS-MIB (.1.3.6.1.2.1.33).
"""

import Globals
from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetTableMap
from Products.DataCollector.plugins.DataMaps import ObjectMap

class upsBypassMap(SnmpPlugin):
    """upsBypassMap"""

    maptype = "upsBypassMap"
    modname = "ZenPacks.community.upsCS1x1.upsBypass"
    relname = "upsBypass"


    snmpGetTableMaps = (
        GetTableMap('upsBypassEntry',
                    '.1.3.6.1.2.1.33.1.5.3.1',
                    {
                       '.2': 'upsBypassVoltage',
                       '.3': 'upsBypassCurrent',
                       '.4': 'upsBypassPower',
                    }
        ),
    )

    def process(self, device, results, log):
        """collect snmp information from this device"""
        log.info('processing %s for device %s', self.name(), device.id)
        getdata, tabledata = results
#        log.info( "Data= %s", tabledata )
        rm = self.relMap()

        upsentry = tabledata.get('upsBypassEntry')

# If no data supplied then simply return
        if not upsentry:
            log.warn( 'No SNMP response from %s for the %s plugin', device.id, self.name() )
            log.warn( "Data= %s", tabledata )
            return

        for oid, data in upsentry.iteritems():
            try:
                om = self.objectMap(data)
                om.snmpindex = oid.strip('.')
                om.upsBypassLineIndexText = "BypassLine" + oid.strip('.')
                om.upsBypassCurrent = float(om.upsBypassCurrent) / 10
                om.id = self.prepId(om.upsBypassLineIndexText)
            except (KeyError, IndexError, AttributeError, TypeError), errorInfo:
                log.warn( ' Error in upsBypassMap modeler plugin %s', errorInfo)
                continue
            rm.append(om)
        return rm
