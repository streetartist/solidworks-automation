# DPartDocEvents_SensorAlertPreNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_SensorAlertPreNotifyEventHandler`

Fired before a sensor's value deviates from its limits in a part document.
Fired before a sensor's value deviates from its limits in a part document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DPartDocEvents_SensorAlertPreNotifyEventHandler( _
   ByVal SensorIn As System.Object, _
   ByVal SensorAlertType As System.Integer _
) As System.Integer
```

```

Dim instance As New DPartDocEvents_SensorAlertPreNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DPartDocEvents_SensorAlertPreNotifyEventHandler( 
   System.object SensorIn,
   System.int SensorAlertType
)
```

```

public delegate System.int DPartDocEvents_SensorAlertPreNotifyEventHandler( 
   System.Object^ SensorIn,
   System.int SensorAlertType
)
```

#### Parameters

*SensorIn*
:   [Sensor](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor.md)

*SensorAlertType*
:   Type of sensor as defined in [swSensorAlertType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSensorAlertType_e.html)

Example

[Get and Set Sensor (C#)](Get_and_Set_Sensor_Example_CSharp.htm)  
[Get and Set Sensor (VB.NET)](Get_and_Set_Sensor_Example_VBNET.htm)  
[Get and Set Sensor (VBA)](Get_and_Set_Sensor_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DPartDocEvents\_SensorAlertPreNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_SensorAlertPreNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[DAssemblyDocEvents\_SensorAlertPreNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_SensorAlertPreNotifyEventHandler.md)
