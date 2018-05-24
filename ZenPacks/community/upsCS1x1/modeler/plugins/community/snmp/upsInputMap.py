##########################################################################
# Author:               ValeruS
# Date:                 September 2017
# Revised:
#
# upsInputMap modeler plugin
#
# This program can be used under the GNU General Public License version 3
# You can find full information here: http://www.zenoss.com/oss
#
##########################################################################

__doc__ = """upsInputMap

Gather table information from UPS info Modules based on UPS-MIB (.1.3.6.1.2.1.33).
"""

import Globals
from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetTableMap
from Products.DataCollector.plugins.DataMaps import ObjectMap

class upsInputMap(SnmpPlugin):
    """upsInputMap"""

    maptype = "upsInputMap"
    modname = "ZenPacks.community.upsCS1x1.upsInput"
    relname = "upsInput"


    snmpGetTableMaps = (
        GetTableMap('upsInputEntry',
                    '.1.3.6.1.2.1.33.1.3.3.1',
                    {
                       '.2': 'upsInputFrequency',
                       '.3': 'upsInputVoltage',
                       '.4': 'upsInputCurrent',
                       '.5': 'upsInputTruePower',
                    }
        ),
    )

    def process(self, device, results, log):
        """collect snmp information from this device"""
        log.info('processing %s for device %s', self.name(), device.id)
        getdata, tabledata = results
#        log.info( "Data= %s", tabledata )
        rm = self.relMap()

        upsentry = tabledata.get('upsInputEntry')

# If no data supplied then simply return
        if not upsentry:
            log.warn( 'No SNMP response from %s for the %s plugin', device.id, self.name() )
            log.warn( "Data= %s", tabledata )
            return

        for oid, data in upsentry.iteritems():
            try:
                om = self.objectMap(data)
                om.snmpindex = oid.strip('.')
                om.upsInputFrequency = float(om.upsInputFrequency) / 10
                om.upsInputCurrent = float(om.upsInputCurrent) / 10
                om.upsInputLineIndexText = "InputLine" + oid.strip('.')
                om.id = self.prepId(om.upsInputLineIndexText)
            except (KeyError, IndexError, AttributeError, TypeError), errorInfo:
                log.warn( ' Error in upsInputMap modeler plugin %s', errorInfo)
                continue
            rm.append(om)
        return rm
