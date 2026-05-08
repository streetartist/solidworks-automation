# HasDamper Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~HasDamper`

Gets or sets whether this simulation spring feature has damper.
Gets or sets whether this simulation spring feature has damper.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property HasDamper As System.Boolean
```

```

Dim instance As ISimulationSpringFeatureData
Dim value As System.Boolean
 
instance.HasDamper = value
 
value = instance.HasDamper
```

```

System.bool HasDamper {get; set;}
```

```

property System.bool HasDamper {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if this simulation spring feature has damper, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimulationSpringFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData.md)  
[ISimulationSpringFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData_members.md)  
[ISimulationSpringFeatureData::DampingConstant Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~DampingConstant.md)  
[ISimulationSpringFeatureData::ExponentOfDamperForceExpression Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~ExponentOfDamperForceExpression.md)
