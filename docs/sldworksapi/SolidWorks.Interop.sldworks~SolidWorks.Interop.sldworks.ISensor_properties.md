# ISensor Interface Properties

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor_properties`

Allows access to a sensor, which can monitor selected properties of parts and assemblies and alert you when the sensor's values deviate from the specified limits.
For a list of all members of this type, see [ISensor members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor_members.md).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Property | [SensorAlertEnabled](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor~SensorAlertEnabled.md) | Gets or sets whether an alert is triggered when the limits of the sensor deviate from its specified values. |
| Property | [SensorAlertState](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor~SensorAlertState.md) | Gets whether an alert is currently triggered for this sensor. |
| Property | [SensorAlertType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor~SensorAlertType.md) | Gets or sets the type of alert for this sensor. |
| Property | [SensorAlertValue1](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor~SensorAlertValue1.md) | Gets or sets the alert value for this sensor. |
| Property | [SensorAlertValue2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor~SensorAlertValue2.md) | Gets or sets alert value for this sensor; only in effect when [sensor alert type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor~SensorAlertType.md) set to swSensorAlert\_Between. |
| Property | [SensorType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor~SensorType.md) | Gets the type of this sensor. |

[Top](#top)

See Also

#### Reference

[ISensor Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IDimensionSensorData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionSensorData.md)  
[DPartDocEvents\_SensorAlertPreNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_SensorAlertPreNotifyEventHandler.md)  
[DAssemblyDocEvents\_SensorAlertPreNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_SensorAlertPreNotifyEventHandler.md)
