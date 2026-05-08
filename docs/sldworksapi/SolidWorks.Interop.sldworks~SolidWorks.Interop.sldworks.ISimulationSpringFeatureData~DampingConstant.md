# DampingConstant Property (ISimulationSpringFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~DampingConstant`

Gets or sets the damping constant for this simulation spring feature.
Gets or sets the damping constant for this simulation spring feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DampingConstant As System.Double
```

```

Dim instance As ISimulationSpringFeatureData
Dim value As System.Double
 
instance.DampingConstant = value
 
value = instance.DampingConstant
```

```

System.double DampingConstant {get; set;}
```

```

property System.double DampingConstant {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Damping constant

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimulationSpringFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData.md)  
[ISimulationSpringFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData_members.md)  
[ISimulationSpringFeatureData::HasDamper Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~HasDamper.md)  
[ISimulationSpringFeatureData::ExponentOfDamperForceExpression Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~ExponentOfDamperForceExpression.md)
