# IsSmartComponent Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsSmartComponent`

Gets whether this component is a Smart Component.
Gets whether this component is a Smart Component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsSmartComponent() As System.Boolean
```

```

Dim instance As IComponent2
Dim value As System.Boolean
 
value = instance.IsSmartComponent()
```

```

System.bool IsSmartComponent()
```

```

System.bool IsSmartComponent(); 
```

#### Return Value

True if a Smart Component, false if not

Example

[Activate Smart Features in an Assembly (C#)](Activate_Smart_Features_in_an_Assembly_Example_CSharp.htm)  
[Activate Smart Features in an Assembly (VB.NET)](Activate_Smart_Features_in_an_Assembly_Example_VBNET.htm)  
[Activate Smart Features in an Assembly (VBA)](Activate_Smart_Features_in_an_Assembly_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IComponent2::GetSmartComponentData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetSmartComponentData.md)  
[IComponent2::SetSmartComponentData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetSmartComponentData.md)  
[ISmartComponentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISmartComponentFeatureData.md)  
[IAssemblyDoc::CreateSmartComponent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateSmartComponent.md)  
[IAssemblyDoc::AddSmartComponent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddSmartComponent.md)
