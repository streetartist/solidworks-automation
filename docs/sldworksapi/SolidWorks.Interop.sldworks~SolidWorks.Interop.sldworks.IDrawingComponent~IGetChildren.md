# IGetChildren Method (IDrawingComponent)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~IGetChildren`

Gets the child components for this drawing component.
Gets the child components for this drawing component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetChildren( _
   ByVal Count As System.Integer _
) As DrawingComponent
```

```

Dim instance As IDrawingComponent
Dim Count As System.Integer
Dim value As DrawingComponent
 
value = instance.IGetChildren(Count)
```

```

DrawingComponent IGetChildren( 
   System.int Count
)
```

```

DrawingComponent^ IGetChildren( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of drawing component objects that are child components of this drawing component

#### Return Value

Array of [IDrawingComponent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent.md) objects that are child components of the drawing component

Remarks

This method traverses the referenced component tree in a given view. Use [IDrawingComponent::Visible](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~Visible.md) to get or set the visibility of individual components in the given view.

Before calling this method, call [IDrawingComponent::GetChildrenCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~GetChildrenCount.md) to determine the size of the array.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent.md)  
[IDrawingComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent_members.md)  
[IDrawingComponent::GetChildren Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~GetChildren.md)
