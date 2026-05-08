# SpecifyMaterial Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData~SpecifyMaterial`

Gets or sets whether to use materials in a 3D Contact feature.
Gets or sets whether to use materials in a 3D Contact feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SpecifyMaterial As System.Boolean
```

```

Dim instance As ISimulation3DContactFeatureData
Dim value As System.Boolean
 
instance.SpecifyMaterial = value
 
value = instance.SpecifyMaterial
```

```

System.bool SpecifyMaterial {get; set;}
```

```

property System.bool SpecifyMaterial {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to use materials, false to not

Remarks

Set to false to modify elastic properties:

- [ISimulation3DContactFeatureData::Stiffness](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData~Stiffness.md)
- [ISimulation3DContactFeatureData::Exponent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData~Exponent.md)
- [ISimulation3DContactFeatureData::MaxDamping](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData~MaxDamping.md)
- [ISimulation3DContactFeatureData::Penetration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData~Penetration.md)

Example

See the [ISimulation3DContactFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimulation3DContactFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData.md)  
[ISimulation3DContactFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData_members.md)  
[ISimulation3DContactFeatureData::MaterialID Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData~MaterialID.md)
