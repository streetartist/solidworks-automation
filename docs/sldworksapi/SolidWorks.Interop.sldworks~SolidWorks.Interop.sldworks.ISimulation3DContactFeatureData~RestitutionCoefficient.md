# RestitutionCoefficient Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData~RestitutionCoefficient`

Gets or sets the coefficient of restitution in a 3D Contact feature.
Gets or sets the coefficient of restitution in a 3D Contact feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property RestitutionCoefficient As System.Double
```

```

Dim instance As ISimulation3DContactFeatureData
Dim value As System.Double
 
instance.RestitutionCoefficient = value
 
value = instance.RestitutionCoefficient
```

```

System.double RestitutionCoefficient {get; set;}
```

```

property System.double RestitutionCoefficient {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Coefficient of restitution

Remarks

Available only when [ISimulation3DContactFeatureData::UseRestitutionCoefficient](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData~UseRestitutionCoefficient.md) is true.

The restitution coefficient is the ratio of relative velocities of two elastic spheres before and after impact.

Example

See the [ISimulation3DContactFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimulation3DContactFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData.md)  
[ISimulation3DContactFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData_members.md)
