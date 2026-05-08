# GetInterpolatedValue Method (ISimulationForceFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~GetInterpolatedValue`

Gets the interpolated value at the specified time for this Force feature.
Gets the interpolated value at the specified time for this Force feature.

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

Dim instance As ISimulationForceFeatureData
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
:   Time at which to get the interpolated value

#### Return Value

Interpolated value

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimulationForceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData.md)  
[ISimulationForceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData_members.md)  
[ISimulationForceFeatureData::InterpolationScheme Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~InterpolationScheme.md)  
[ISimulationForceFeatureData::FunctionInterpolatedValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~FunctionInterpolatedValues.md)
