##########################################################################
# Author:               ValeruS
# Date:                 September 2017
# Revised:
#
# info.py for upsCS1x1 ZenPack
#
# This program can be used under the GNU General Public License version 3
# You can find full information here: http://www.zenoss.com/oss
#
################################################################################

__doc__="""info.py

Representation of upsCS1x1 components.

"""


from zope.interface import implements

from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.device import DeviceInfo
from Products.Zuul.infos.component import ComponentInfo
from Products.Zuul.decorators import info

from ZenPacks.community.upsCS1x1 import interfaces



class upsBatteryInfo(ComponentInfo):
    implements(interfaces.IupsBatteryInfo)

    upsBatteryStatus              = ProxyProperty("upsBatteryStatus")
    upsBatteryStatusText          = ProxyProperty("upsBatteryStatusText")
    upsSecondsOnBattery           = ProxyProperty("upsSecondsOnBattery")
    upsEstimatedMinutesRemaining  = ProxyProperty("upsEstimatedMinutesRemaining")
    upsEstimatedChargeRemaining   = ProxyProperty("upsEstimatedChargeRemaining")
    upsBatteryVoltage             = ProxyProperty("upsBatteryVoltage")
    upsBatteryCurrent             = ProxyProperty("upsBatteryCurrent")
    upsBatteryTemperature         = ProxyProperty("upsBatteryTemperature")
    upsTestResultsSummary         = ProxyProperty("upsTestResultsSummary")
    upsTestResultsSummaryText     = ProxyProperty("upsTestResultsSummaryText")

class upsInputInfo(ComponentInfo):
    implements(interfaces.IupsInputInfo)

    upsInputLineIndexText         = ProxyProperty("upsInputLineIndexText")
    upsInputFrequency             = ProxyProperty("upsInputFrequency")
    upsInputVoltage               = ProxyProperty("upsInputVoltage")
    upsInputCurrent               = ProxyProperty("upsInputCurrent")
    upsInputTruePower             = ProxyProperty("upsInputTruePower")

class upsOutputInfo(ComponentInfo):
    implements(interfaces.IupsOutputInfo)

    upsOutputLineIndexText        = ProxyProperty("upsOutputLineIndexText")
    upsOutputVoltage              = ProxyProperty("upsOutputVoltage")
    upsOutputCurrent              = ProxyProperty("upsOutputCurrent")
    upsOutputPower                = ProxyProperty("upsOutputPower")
    upsOutputPercentLoad          = ProxyProperty("upsOutputPercentLoad")

class upsBypassInfo(ComponentInfo):
    implements(interfaces.IupsBypassInfo)

    upsBypassLineIndexText        = ProxyProperty("upsBypassLineIndexText")
    upsBypassVoltage              = ProxyProperty("upsBypassVoltage")
    upsBypassCurrent              = ProxyProperty("upsBypassCurrent")
    upsBypassPower                = ProxyProperty("upsBypassPower")

