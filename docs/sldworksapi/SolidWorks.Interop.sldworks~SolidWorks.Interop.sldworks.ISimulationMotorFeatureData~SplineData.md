# SplineData Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~SplineData`

Gets or sets the spline data points for this motor feature.
Gets or sets the spline data points for this motor feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SplineData As System.Object
```

```

Dim instance As ISimulationMotorFeatureData
Dim value As System.Object
 
instance.SplineData = value
 
value = instance.SplineData
```

```

System.object SplineData {get; set;}
```

```

property System.Object^ SplineData {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of spline data points

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimulationMotorFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData.md)  
[ISimulationMotorFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData_members.md)  
[ISimulationMotorFeatureData::LoadSplineData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData~LoadSplineData.md)
