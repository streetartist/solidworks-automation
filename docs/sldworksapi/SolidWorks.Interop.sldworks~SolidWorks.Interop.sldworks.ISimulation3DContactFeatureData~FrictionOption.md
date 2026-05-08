# FrictionOption Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData~FrictionOption`

Gets or sets whether contact friction is off, full (static), or dynamic in a 3D Contact feature.
Gets or sets whether contact friction is off, full (static), or dynamic in a 3D Contact feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FrictionOption As System.Integer
```

```

Dim instance As ISimulation3DContactFeatureData
Dim value As System.Integer
 
instance.FrictionOption = value
 
value = instance.FrictionOption
```

```

System.int FrictionOption {get; set;}
```

```

property System.int FrictionOption {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Friction as defined in [swMotionContactFrictionType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMotionContactFrictionType_e.html)

Example

See the [ISimulation3DContactFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimulation3DContactFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData.md)  
[ISimulation3DContactFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData_members.md)  
[ISimulation3DContactFeatureData::DynamicFrictionCoefficient Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData~DynamicFrictionCoefficient.md)  
[ISimulation3DContactFeatureData::DynamicFrictionVelocity Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData~DynamicFrictionVelocity.md)  
[ISimulation3DContactFeatureData::StaticFrictionCoefficient Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData~StaticFrictionCoefficient.md)  
[ISimulation3DContactFeatureData::StaticFrictionVelocity Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData~StaticFrictionVelocity.md)
