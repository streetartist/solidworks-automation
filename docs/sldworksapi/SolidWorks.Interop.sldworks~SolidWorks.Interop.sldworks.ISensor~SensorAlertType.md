# SensorAlertType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor~SensorAlertType`

Gets or sets the type of alert for this sensor.
Gets or sets the type of alert for this sensor.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SensorAlertType As System.Integer
```

```

Dim instance As ISensor
Dim value As System.Integer
 
instance.SensorAlertType = value
 
value = instance.SensorAlertType
```

```

System.int SensorAlertType {get; set;}
```

```

property System.int SensorAlertType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Type of sensor as defined by [swSensorAlertType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSensorAlertType_e.html)

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
[ISensor::SensorAlertEnabled Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor~SensorAlertEnabled.md)  
[ISensor::SensorAlertState Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor~SensorAlertState.md)  
[ISensor::SensorAlertValue1 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor~SensorAlertValue1.md)  
[ISensor::SensorAlertValue2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor~SensorAlertValue2.md)
