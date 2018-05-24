##########################################################################
# Author:               ValeruS
# Date:                 September 2017
# Revised:
#
# upsBatteryMap modeler plugin
#
# This program can be used under the GNU General Public License version 3
# You can find full information here: http://www.zenoss.com/oss
#
##########################################################################

__doc__ = """upsBatteryMap

Gather table information from UPS info Modules based on UPS-MIB (.1.3.6.1.2.1.33).
"""

import Globals
from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap, GetTableMap
from Products.DataCollector.plugins.DataMaps import ObjectMap

class upsBatteryMap(SnmpPlugin):
    """upsBatteryMap"""

    maptype = "upsBatteryMap"
    modname = "ZenPacks.community.upsCS1x1.upsBattery"
    relname = "upsBattery"


    snmpGetMap = GetMap({
                       '.1.3.6.1.2.1.33.1.2.1.0': 'upsBatteryStatus',
                       '.1.3.6.1.2.1.33.1.2.2.0': 'upsSecondsOnBattery',
                       '.1.3.6.1.2.1.33.1.2.3.0': 'upsEstimatedMinutesRemaining',
                       '.1.3.6.1.2.1.33.1.2.4.0': 'upsEstimatedChargeRemaining',
                       '.1.3.6.1.2.1.33.1.2.5.0': 'upsBatteryVoltage',
                       '.1.3.6.1.2.1.33.1.2.6.0': 'upsBatteryCurrent',
                       '.1.3.6.1.2.1.33.1.2.7.0': 'upsBatteryTemperature',
                       '.1.3.6.1.2.1.33.1.7.3.0': 'upsTestResultsSummary',
                    })


    BatteryStatus     = {1: ( 2, 'Unknown'),
                         2: ( 0, 'batteryNormal'),
                         3: ( 4, 'batteryLow'),
                         4: ( 3, 'batteryDepleted'),
                        }

    TestBatteryStatus = {1:'donePass',
                         2:'doneWarning',
                         3:'doneError',
                         4:'aborted',
                         5:'inProgress',
                         6:'noTestsInitiated',
                        }


    def process(self, device, results, log):
        """collect snmp information from this device"""
        log.info('processing %s for device %s', self.name(), device.id)
        getdata, tabledata = results
#        log.info( "Data= %s", getdata )
        rm = self.relMap()

# If no data supplied then simply return
        if not getdata:
            log.warn( 'No SNMP response from %s for the %s plugin', device.id, self.name() )
            log.warn( "Data= %s", getdata )
            return

        om = self.objectMap(getdata)
        try:
                # BatTimeRemaining is in timeticks (1/100 sec) so convert to minutes ?
                index = om.upsBatteryStatus
                om.upsBatteryStatus = self.BatteryStatus[index][0]
                om.upsBatteryStatusText = self.BatteryStatus[index][1]
                om.upsTestResultsSummaryText = self.TestBatteryStatus.get(int(om.upsTestResultsSummary), 'unknown')
                om.id = "Baterry"
                om.id = self.prepId(om.id)
                om.upsBatteryCurrent = float(om.upsBatteryCurrent) / 10
                om.snmpindex = '0'
                rm.append(om)
        except (KeyError, IndexError, AttributeError, TypeError), errorInfo:
                log.warn( ' Error in upsBatteryMap modeler plugin %s', errorInfo)
        return rm
