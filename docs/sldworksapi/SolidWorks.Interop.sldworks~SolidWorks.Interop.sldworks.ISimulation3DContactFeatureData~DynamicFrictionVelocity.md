# DynamicFrictionVelocity Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData~DynamicFrictionVelocity`

Gets or sets the dynamic friction velocity in a 3D Contact feature.
Gets or sets the dynamic friction velocity in a 3D Contact feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DynamicFrictionVelocity As System.Double
```

```

Dim instance As ISimulation3DContactFeatureData
Dim value As System.Double
 
instance.DynamicFrictionVelocity = value
 
value = instance.DynamicFrictionVelocity
```

```

System.double DynamicFrictionVelocity {get; set;}
```

```

property System.double DynamicFrictionVelocity {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Dynamic friction velocity

Remarks

Available only when [ISimulation3DContactFeatureData::FrictionOption](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData~FrictionOption.md) is [swMotionContactFrictionType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMotionContactFrictionType_e.html).swMotionContactFrictionDynamic.

Example

See the [ISimulation3DContactFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimulation3DContactFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData.md)  
[ISimulation3DContactFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData_members.md)  
[ISimulation3DContactFeatureData::DynamicFrictionCoefficient Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData~DynamicFrictionCoefficient.md)
