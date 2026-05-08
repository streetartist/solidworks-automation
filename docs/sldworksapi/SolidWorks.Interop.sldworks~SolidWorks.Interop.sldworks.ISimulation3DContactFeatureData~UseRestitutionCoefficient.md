# UseRestitutionCoefficient Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData~UseRestitutionCoefficient`

Gets or sets whether to use the restitution coefficient instead of impact force in a 3D Contact feature.
Gets or sets whether to use the restitution coefficient instead of impact force in a 3D Contact feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UseRestitutionCoefficient As System.Boolean
```

```

Dim instance As ISimulation3DContactFeatureData
Dim value As System.Boolean
 
instance.UseRestitutionCoefficient = value
 
value = instance.UseRestitutionCoefficient
```

```

System.bool UseRestitutionCoefficient {get; set;}
```

```

property System.bool UseRestitutionCoefficient {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to use the restitution coefficient, false to use impact force

Example

See the [ISimulation3DContactFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimulation3DContactFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData.md)  
[ISimulation3DContactFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData_members.md)  
[ISimulation3DContactFeatureData::MaxDamping Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData~MaxDamping.md)  
[ISimulation3DContactFeatureData::Exponent Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData~Exponent.md)  
[ISimulation3DContactFeatureData::Penetration Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData~Penetration.md)  
[ISimulation3DContactFeatureData::RestitutionCoefficient Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData~RestitutionCoefficient.md)  
[ISimulation3DContactFeatureData::Stiffness Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData~Stiffness.md)
