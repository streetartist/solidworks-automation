# ReferenceComponent Property (ISimulationForceFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData~ReferenceComponent`

Gets or sets the component to serve as a reference frame for the force.
Gets or sets the component to serve as a reference frame for the force.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ReferenceComponent As Component2
```

```

Dim instance As ISimulationForceFeatureData
Dim value As Component2
 
instance.ReferenceComponent = value
 
value = instance.ReferenceComponent
```

```

Component2 ReferenceComponent {get; set;}
```

```

property Component2^ ReferenceComponent {
   Component2^ get();
   void set (    Component2^ value);
}
```

#### Property Value

[Component](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) to serve as a reference frame

Remarks

Specifying a component to serve as a reference frame is optional. If a component is not specified, then the reference frame is the global ground.

Example

[Create Force Feature (VBA)](Create_Force_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimulationForceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData.md)  
[ISimulationForceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData_members.md)
