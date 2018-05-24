/*
 * Based on the configuration in ../../configure.zcml this JavaScript will only
 * be loaded when the user is looking at an ExampleDevice in the web interface.
 */

(function(){

var ZC = Ext.ns('Zenoss.component');

function render_link(ob) {
    if (ob && ob.uid) {
        return Zenoss.render.link(ob.uid);
    } else {
        return ob;
    }
}


ZC.upsBatteryPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'upsBattery',
            alias:['widget.upsBatteryPanel'],
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'severity'},
                {name: 'usesMonitorAttribute'},
                {name: 'upsBatteryStatus'},
                {name: 'upsBatteryStatusText'},
                {name: 'upsTestResultsSummaryText'},
                {name: 'monitor'},
                {name: 'monitored'}
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Object Name'),
                width: 100
            },{
                id: 'upsBatteryStatusText',
                dataIndex: 'upsBatteryStatusText',
                header: _t('Battery Status'),
                sortable: true,
                width: 100,
            },{
                id: 'upsBatteryStatus',
                dataIndex: 'upsBatteryStatus',
                header: _t('Status'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50,
            },{
                id: 'upsTestResultsSummaryText',
                dataIndex: 'upsTestResultsSummaryText',
                header: _t('Battery TestStatus'),
                flex: 1,
                sortable: true,
                width: 150,
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 65
            }]
        });
        ZC.upsBatteryPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('upsBatteryPanel', ZC.upsBatteryPanel);
ZC.registerName('upsBattery', _t('UPS Battery'), _t('UPS Batteries'));

ZC.upsInputPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'upsInput',
            alias:['widget.upsInputPanel'],
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'severity'},
                {name: 'usesMonitorAttribute'},
                {name: 'upsInputVoltage'},
                {name: 'upsInputCurrent'},
                {name: 'upsInputTruePower'},
                {name: 'upsInputFrequency'},
                {name: 'monitor'},
                {name: 'monitored'}
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                flex: 1,
                dataIndex: 'name',
                header: _t('Name'),
                width: 100
            },{
                id: 'upsInputVoltage',
                dataIndex: 'upsInputVoltage',
                header: _t('Input Voltage (V)'),
                sortable: true,
                width: 150,
            },{
                id: 'upsInputCurrent',
                dataIndex: 'upsInputCurrent',
                header: _t('Input Current (A)'),
                sortable: true,
                width: 150,
            },{
                id: 'upsInputTruePower',
                dataIndex: 'upsInputTruePower',
                header: _t('Input Power (W)'),
                sortable: true,
                width: 150,
            },{
                id: 'upsInputFrequency',
                dataIndex: 'upsInputFrequency',
                header: _t('Input Frequency (Hz)'),
                sortable: true,
                width: 150,
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 65
            }]
        });
        ZC.upsInputPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('upsInputPanel', ZC.upsInputPanel);
ZC.registerName('upsInput', _t('UPS Input'), _t('UPS Inputs'));

ZC.upsOutputPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'upsOutput',
            alias:['widget.upsOutputPanel'],
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'severity'},
                {name: 'usesMonitorAttribute'},
                {name: 'upsOutputVoltage'},
                {name: 'upsOutputCurrent'},
                {name: 'upsOutputPower'},
                {name: 'upsOutputPercentLoad'},
                {name: 'monitor'},
                {name: 'monitored'}
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                flex: 1,
                dataIndex: 'name',
                header: _t('Name'),
                width: 100
            },{
                id: 'upsOutputVoltage',
                dataIndex: 'upsOutputVoltage',
                header: _t('Output Voltage (V)'),
                sortable: true,
                width: 150,
            },{
                id: 'upsOutputCurrent',
                dataIndex: 'upsOutputCurrent',
                header: _t('Output Current (A)'),
                sortable: true,
                width: 150,
            },{
                id: 'upsOutputPower',
                dataIndex: 'upsOutputPower',
                header: _t('Output Power (W)'),
                sortable: true,
                width: 150,
            },{
                id: 'upsOutputPercentLoad',
                dataIndex: 'upsOutputPercentLoad',
                header: _t('Percent Load'),
                sortable: true,
                width: 150,
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 65
            }]
        });
        ZC.upsOutputPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('upsOutputPanel', ZC.upsOutputPanel);
ZC.registerName('upsOutput', _t('UPS Output'), _t('UPS Outputs'));

ZC.upsBypassPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'upsBypass',
            alias:['widget.upsBypassPanel'],
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'severity'},
                {name: 'usesMonitorAttribute'},
                {name: 'upsBypassVoltage'},
                {name: 'upsBypassCurrent'},
                {name: 'upsBypassPower'},
                {name: 'monitor'},
                {name: 'monitored'}
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                flex: 1,
                dataIndex: 'name',
                header: _t('Name'),
                width: 100
            },{
                id: 'upsBypassVoltage',
                dataIndex: 'upsBypassVoltage',
                header: _t('Bypass Voltage (V)'),
                sortable: true,
                width: 150,
            },{
                id: 'upsBypassCurrent',
                dataIndex: 'upsBypassCurrent',
                header: _t('Bypass Current (A)'),
                sortable: true,
                width: 150,
            },{
                id: 'upsBypassPower',
                dataIndex: 'upsBypassPower',
                header: _t('Bypass Power (W)'),
                sortable: true,
                width: 150,
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 65
            }]
        });
        ZC.upsBypassPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('upsBypassPanel', ZC.upsBypassPanel);
ZC.registerName('upsBypass', _t('UPS Bypass'), _t('UPS Bypass'));



})();
