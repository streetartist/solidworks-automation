# LoadReferences Property (ISimulationSpringFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~LoadReferences`

Gets or sets the load references for this simulation spring feature.
Gets or sets the load references for this simulation spring feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property LoadReferences As System.Object
```

```

Dim instance As ISimulationSpringFeatureData
Dim value As System.Object
 
instance.LoadReferences = value
 
value = instance.LoadReferences
```

```

System.object LoadReferences {get; set;}
```

```

property System.Object^ LoadReferences {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Load-bearing [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimulationSpringFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData.md)  
[ISimulationSpringFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData_members.md)
