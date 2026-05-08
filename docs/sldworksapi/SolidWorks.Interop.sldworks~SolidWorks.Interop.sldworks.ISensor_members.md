# ISensor Interface Members

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor_members`

Allows access to a sensor, which can monitor selected properties of parts and assemblies and alert you when the sensor's values deviate from the specified limits.
The following tables list the members exposed by [ISensor](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor.md).

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

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [GetSensorFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor~GetSensorFeatureData.md) | Gets a sensor feature data. |
| Method | [GetSensorValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor~GetSensorValue.md) | Gets the value and units of this sensor. |
| Method | [UpdateSensor](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor~UpdateSensor.md) | Updates the sensor. |

[Top](#top)

 

See Also

#### Reference

[ISensor Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IDimensionSensorData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionSensorData.md)  
[DPartDocEvents\_SensorAlertPreNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_SensorAlertPreNotifyEventHandler.md)  
[DAssemblyDocEvents\_SensorAlertPreNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_SensorAlertPreNotifyEventHandler.md)
