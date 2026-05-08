# FunctionInterpolatedValues Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~FunctionInterpolatedValues`

Gets or sets the interpolated values for this Force feature.
Gets or sets the interpolated values for this Force feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FunctionInterpolatedValues As System.Object
```

```

Dim instance As ISimulationForceFeatureData
Dim value As System.Object
 
instance.FunctionInterpolatedValues = value
 
value = instance.FunctionInterpolatedValues
```

```

System.object FunctionInterpolatedValues {get; set;}
```

```

property System.Object^ FunctionInterpolatedValues {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of interpolated values (time and force)

Remarks

SOLIDWORKS interpolates a spline betweeen the data points.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimulationForceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData.md)  
[ISimulationForceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData_members.md)  
[ISimulationForceFeatureData::GetInterpolatedValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~GetInterpolatedValue.md)  
[ISimulationForceFeatureData::InterpolationScheme Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~InterpolationScheme.md)
