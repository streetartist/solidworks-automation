# Stiffness Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData~Stiffness`

Gets or sets the stiffness at the boundary of interaction between the two parts in a 3D Contact feature.
Gets or sets the stiffness at the boundary of interaction between the two parts in a 3D Contact feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Stiffness As System.Double
```

```

Dim instance As ISimulation3DContactFeatureData
Dim value As System.Double
 
instance.Stiffness = value
 
value = instance.Stiffness
```

```

System.double Stiffness {get; set;}
```

```

property System.double Stiffness {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Stiffness at the boundary of interaction

Remarks

Available only when [ISimulation3DContactFeatureData::UseRestitutionCoefficient](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData~UseRestitutionCoefficient.md) and [ISimulation3DContactFeatureData::SpecifyMaterial](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData~SpecifyMaterial.md) are both false.

Example

See the [ISimulation3DContactFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimulation3DContactFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData.md)  
[ISimulation3DContactFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData_members.md)
