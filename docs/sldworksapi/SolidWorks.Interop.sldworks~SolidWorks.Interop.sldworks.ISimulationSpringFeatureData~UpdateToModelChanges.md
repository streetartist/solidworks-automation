# UpdateToModelChanges Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~UpdateToModelChanges`

Gets or sets whether to have the free length dynamically update model changes while the PropertyManager page is open.
Gets or sets whether to have the [free length](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~FreeLength.md) dynamically update model changes while the PropertyManager page is open.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UpdateToModelChanges As System.Boolean
```

```

Dim instance As ISimulationSpringFeatureData
Dim value As System.Boolean
 
instance.UpdateToModelChanges = value
 
value = instance.UpdateToModelChanges
```

```

System.bool UpdateToModelChanges {get; set;}
```

```

property System.bool UpdateToModelChanges {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

Ture to have the free length dynamically update model changes while the PropertyManager page is open, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimulationSpringFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData.md)  
[ISimulationSpringFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData_members.md)
