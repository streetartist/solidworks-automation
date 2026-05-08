# SensorAlertValue2 Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor~SensorAlertValue2`

Gets or sets alert value for this sensor; only in effect when sensor alert type set to swSensorAlert_Between.
Gets or sets alert value for this sensor; only in effect when [sensor alert type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor~SensorAlertType.md) set to swSensorAlert\_Between.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SensorAlertValue2 As System.Double
```

```

Dim instance As ISensor
Dim value As System.Double
 
instance.SensorAlertValue2 = value
 
value = instance.SensorAlertValue2
```

```

System.double SensorAlertValue2 {get; set;}
```

```

property System.double SensorAlertValue2 {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Alert value

Example

[Get and Set Sensor (C#)](Get_and_Set_Sensor_Example_CSharp.htm)  
[Get and Set Sensor (VB.NET)](Get_and_Set_Sensor_Example_VBNET.htm)  
[Get and Set Sensor (VBA)](Get_and_Set_Sensor_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISensor Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor.md)  
[ISensor Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor_members.md)  
[ISensor::SensorAlertValue1 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor~SensorAlertValue1.md)  
[ISensor::SensorAlertState Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor~SensorAlertState.md)  
[ISensor::SensorAlertEnabled Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor~SensorAlertEnabled.md)
