# GetInterpolatedValue Method (ISimulationMotorFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~GetInterpolatedValue`

Gets the interopolated value at the specified time for this motor feature.
Gets the interopolated value at the specified time for this motor feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetInterpolatedValue( _
   ByVal Time As System.Double _
) As System.Double
```

```

Dim instance As ISimulationMotorFeatureData
Dim Time As System.Double
Dim value As System.Double
 
value = instance.GetInterpolatedValue(Time)
```

```

System.double GetInterpolatedValue( 
   System.double Time
)
```

```

System.double GetInterpolatedValue( 
   System.double Time
) 
```

#### Parameters

*Time*
:   Time for which you want the interpolated value

#### Return Value

Interpolated value at the specfied time

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimulationMotorFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData.md)  
[ISimulationMotorFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData_members.md)  
[ISimulationMotorFeatureData::InterpolatedMotor Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~InterpolatedMotor.md)  
[ISimulationMotorFeatureData::InterpolationScheme Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~InterpolationScheme.md)
