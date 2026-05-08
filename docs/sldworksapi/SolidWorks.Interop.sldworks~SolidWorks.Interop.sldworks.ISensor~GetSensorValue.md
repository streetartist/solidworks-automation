# GetSensorValue Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor~GetSensorValue`

Gets the value and units of this sensor.
Gets the value and units of this sensor.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSensorValue( _
   ByRef Value As System.Double, _
   ByRef Units As System.String _
) As System.Boolean
```

```

Dim instance As ISensor
Dim Value As System.Double
Dim Units As System.String
Dim value As System.Boolean
 
value = instance.GetSensorValue(Value, Units)
```

```

System.bool GetSensorValue( 
   out System.double Value,
   out System.string Units
)
```

```

System.bool GetSensorValue( 
   [Out] System.double Value,
   [Out] System.String^ Units
) 
```

#### Parameters

*Value*
:   Value of the sensor

*Units*
:   Units of the sensor

#### Return Value

True if successful, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISensor Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor.md)  
[ISensor Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor_members.md)
