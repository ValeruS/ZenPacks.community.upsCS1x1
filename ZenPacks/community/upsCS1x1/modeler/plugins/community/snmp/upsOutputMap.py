##########################################################################
# Author:               ValeruS
# Date:                 September 2017
# Revised:
#
# upsOutputMap modeler plugin
#
# This program can be used under the GNU General Public License version 3
# You can find full information here: http://www.zenoss.com/oss
#
##########################################################################

__doc__ = """upsOutputMap

Gather table information from UPS info Modules based on UPS-MIB (.1.3.6.1.2.1.33).
"""

import Globals
from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetTableMap
from Products.DataCollector.plugins.DataMaps import ObjectMap

class upsOutputMap(SnmpPlugin):
    """upsOutputMap"""

    maptype = "upsOutputMap"
    modname = "ZenPacks.community.upsCS1x1.upsOutput"
    relname = "upsOutput"


    snmpGetTableMaps = (
        GetTableMap('upsOutputEntry',
                    '.1.3.6.1.2.1.33.1.4.4.1',
                    {
                       '.2': 'upsOutputVoltage',
                       '.3': 'upsOutputCurrent',
                       '.4': 'upsOutputPower',
                       '.5': 'upsOutputPercentLoad',
                    }
        ),
    )

    def process(self, device, results, log):
        """collect snmp information from this device"""
        log.info('processing %s for device %s', self.name(), device.id)
        getdata, tabledata = results
#        log.info( "Data= %s", tabledata )
        rm = self.relMap()

        upsentry = tabledata.get('upsOutputEntry')

# If no data supplied then simply return
        if not upsentry:
            log.warn( 'No SNMP response from %s for the %s plugin', device.id, self.name() )
            log.warn( "Data= %s", tabledata )
            return

        for oid, data in upsentry.iteritems():
            try:
                om = self.objectMap(data)
                om.snmpindex = oid.strip('.')
                om.upsOutputCurrent = float(om.upsOutputCurrent) / 10
                om.upsOutputLineIndexText = "OutputLine" + oid.strip('.')
                om.id = self.prepId(om.upsOutputLineIndexText)
            except (KeyError, IndexError, AttributeError, TypeError), errorInfo:
                log.warn( ' Error in upsOutputMap modeler plugin %s', errorInfo)
                continue
            rm.append(om)
        return rm
