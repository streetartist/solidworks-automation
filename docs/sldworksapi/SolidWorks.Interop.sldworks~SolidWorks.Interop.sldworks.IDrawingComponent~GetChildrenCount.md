# GetChildrenCount Method (IDrawingComponent)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~GetChildrenCount`

Gets the number of child components for this drawing component.
Gets the number of child components for this drawing component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetChildrenCount() As System.Integer
```

```

Dim instance As IDrawingComponent
Dim value As System.Integer
 
value = instance.GetChildrenCount()
```

```

System.int GetChildrenCount()
```

```

System.int GetChildrenCount(); 
```

#### Return Value

Number of child components for this drawing component

Remarks

Call this method before calling [IDrawingComponent::IGetChildren](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~IGetChildren.md).

Example

[Create Section View at Specified Location (VBA)](Create_Section_View_at_Specified_Location_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent.md)  
[IDrawingComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent_members.md)  
[IDrawingComponent::GetChildren Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~GetChildren.md)
