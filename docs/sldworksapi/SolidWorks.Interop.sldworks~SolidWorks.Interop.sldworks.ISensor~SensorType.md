# SensorType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor~SensorType`

Gets the type of this sensor.
Gets the type of this sensor.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SensorType As System.Integer
```

```

Dim instance As ISensor
Dim value As System.Integer
 
instance.SensorType = value
 
value = instance.SensorType
```

```

System.int SensorType {get; set;}
```

```

property System.int SensorType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Type of sensor as defined in [swSensorType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSensorType_e.html)

Example

[Get and Set Sensor (C#)](Get_and_Set_Sensor_Example_CSharp.htm)  
[Get and Set Sensor (VB.NET)](Get_and_Set_Sensor_Example_VBNET.htm)  
[Get and Set Sensor (VBA)](Get_and_Set_Sensor_Example_VB.htm)

Requirements

As of SOLIDWORKS 2009 SP02, only measurement (dimension) sensors of type swSensorType\_e.swSensorDimension are supported.

See Also

#### Reference

[ISensor Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor.md)  
[ISensor Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor_members.md)
