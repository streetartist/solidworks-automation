# LoadSplineData Method (ISimulationMotorFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~LoadSplineData`

Loads the spline data from the specified file for this motor feature.
Loads the spline data from the specified file for this motor feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function LoadSplineData( _
   ByVal Value As System.String _
) As System.Boolean
```

```

Dim instance As ISimulationMotorFeatureData
Dim Value As System.String
Dim value As System.Boolean
 
value = instance.LoadSplineData(Value)
```

```

System.bool LoadSplineData( 
   System.string Value
)
```

```

System.bool LoadSplineData( 
   System.String^ Value
) 
```

#### Parameters

*Value*
:   File from which to load the spline data point values

#### Return Value

True if the operation succeeds, false if it fails

Remarks

The file should contain one data point per line. The data point consists of two values:

- Time
- Value at that time

Use commas or spaces as separators between the values.

Example

[Create Linear Motor Feature (VBA)](Create_Linear_Motor_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimulationMotorFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData.md)  
[ISimulationMotorFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData_members.md)  
[ISimulationMotorFeatureData::SplineData Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~SplineData.md)
