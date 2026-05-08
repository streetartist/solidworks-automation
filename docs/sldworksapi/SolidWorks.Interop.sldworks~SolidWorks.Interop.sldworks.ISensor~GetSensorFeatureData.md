# GetSensorFeatureData Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor~GetSensorFeatureData`

Gets a sensor feature data.
Gets a sensor feature data.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSensorFeatureData() As System.Object
```

```

Dim instance As ISensor
Dim value As System.Object
 
value = instance.GetSensorFeatureData()
```

```

System.object GetSensorFeatureData()
```

```

System.Object^ GetSensorFeatureData(); 
```

#### Return Value

[Sensor feature data](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionSensorData.md) (see **Remarks**)

Remarks

Currently only Measurement (dimension) sensors are supported.

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
