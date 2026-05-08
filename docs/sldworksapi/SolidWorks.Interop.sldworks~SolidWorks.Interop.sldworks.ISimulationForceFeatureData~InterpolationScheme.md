# InterpolationScheme Property (ISimulationForceFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~InterpolationScheme`

Gets the interopolation scheme for this Force feature.
Gets the interopolation scheme for this Force feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property InterpolationScheme As System.Integer
```

```

Dim instance As ISimulationForceFeatureData
Dim value As System.Integer
 
instance.InterpolationScheme = value
 
value = instance.InterpolationScheme
```

```

System.int InterpolationScheme {get; set;}
```

```

property System.int InterpolationScheme {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Interpolation scheme as defined by [swInterpolationType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInterpolationType_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimulationForceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData.md)  
[ISimulationForceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData_members.md)  
[ISimulationForceFeatureData::GetInterpolatedValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~GetInterpolatedValue.md)  
[ISimulationForceFeatureData::FunctionInterpolatedValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~FunctionInterpolatedValues.md)
