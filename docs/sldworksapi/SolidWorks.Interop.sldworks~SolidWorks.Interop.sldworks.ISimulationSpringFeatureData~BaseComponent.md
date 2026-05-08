# BaseComponent Property (ISimulationSpringFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData~BaseComponent`

Gets or sets the base component for this simulation spring feature.
Gets or sets the base component for this simulation spring feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property BaseComponent As Component2
```

```

Dim instance As ISimulationSpringFeatureData
Dim value As Component2
 
instance.BaseComponent = value
 
value = instance.BaseComponent
```

```

Component2 BaseComponent {get; set;}
```

```

property Component2^ BaseComponent {
   Component2^ get();
   void set (    Component2^ value);
}
```

#### Property Value

[Base component](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimulationSpringFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData.md)  
[ISimulationSpringFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData_members.md)
