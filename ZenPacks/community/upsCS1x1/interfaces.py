##########################################################################
# Author:               ValeruS
# Date:                 September 2017
# Revised:
#
# interfaces.py for upsCS1x1 ZenPack
#
# This program can be used under the GNU General Public License version 3
# You can find full information here: http://www.zenoss.com/oss
#
################################################################################

__doc__="""interfaces

describes the form field to the user interface.

"""
from Products.Zuul.form import schema
from Products.Zuul.interfaces.device import IDeviceInfo
from Products.Zuul.interfaces.component import IComponentInfo
from Products.Zuul.utils import ZuulMessageFactory as _t

from Products.ZenModel.ZVersion import VERSION as ZENOSS_VERSION
from Products.ZenUtils.Version import Version

if Version.parse('Zenoss %s' % ZENOSS_VERSION) >= Version.parse('Zenoss 4'):
    SingleLineText = schema.TextLine
    MultiLineText = schema.Text
else:
    SingleLineText = schema.Text
    MultiLineText = schema.TextLine


class IupsBatteryInfo(IComponentInfo):
    """
    Info adapter for upsCS1x1 Battery component
    """
    upsBatteryVoltage             = SingleLineText(title=_t(u"Voltage"))
    upsBatteryCurrent             = SingleLineText(title=_t(u"Current"))
    upsEstimatedChargeRemaining   = SingleLineText(title=_t(u"Capacity %"))
    upsEstimatedMinutesRemaining  = SingleLineText(title=_t(u"TimeRemaining (min)"))
    upsBatteryStatus              = SingleLineText(title=_t(u"Battery Status"))
    upsSecondsOnBattery           = SingleLineText(title=_t(u"On Battery (sec)"))
    upsTestResultsSummary         = SingleLineText(title=_t(u"Battery Test Result"))
    upsBatteryTemperature         = SingleLineText(title=_t(u"Battery Temperature"))

class IupsInputInfo(IComponentInfo):
    """
    Info adapter for upsCS1x1 Inputs component
    """
    upsInputVoltage               = SingleLineText(title=_t(u"Input Voltage"))
    upsInputCurrent               = SingleLineText(title=_t(u"Input Current"))
    upsInputTruePower             = SingleLineText(title=_t(u"Input TruePower"))
    upsInputFrequency             = SingleLineText(title=_t(u"Input Frequency"))

class IupsOutputInfo(IComponentInfo):
    """
    Info adapter for upsCS1x1 Outputs component
    """
    upsOutputVoltage              = SingleLineText(title=_t(u"Output Voltage"))
    upsOutputCurrent              = SingleLineText(title=_t(u"Output Current"))
    upsOutputPower                = SingleLineText(title=_t(u"Output Power"))
    upsOutputPercentLoad          = SingleLineText(title=_t(u"Percent Load"))

class IupsBypassInfo(IComponentInfo):
    """
    Info adapter for upsCS1x1 Bypass component
    """
    upsBypassVoltage              = SingleLineText(title=_t(u"Bypass Voltage"))
    upsBypassCurrent              = SingleLineText(title=_t(u"Bypass Current"))
    upsBypassPower                = SingleLineText(title=_t(u"Bypass Power"))

