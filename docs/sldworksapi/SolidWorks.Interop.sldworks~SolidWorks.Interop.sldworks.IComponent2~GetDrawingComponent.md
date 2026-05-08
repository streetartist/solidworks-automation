# GetDrawingComponent Method (IComponent2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetDrawingComponent`

Gets the drawing component for this component.
Gets the drawing component for this component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDrawingComponent( _
   ByVal ViewIn As View _
) As DrawingComponent
```

```

Dim instance As IComponent2
Dim ViewIn As View
Dim value As DrawingComponent
 
value = instance.GetDrawingComponent(ViewIn)
```

```

DrawingComponent GetDrawingComponent( 
   View ViewIn
)
```

```

DrawingComponent^ GetDrawingComponent( 
   View^ ViewIn
) 
```

#### Parameters

*ViewIn*
:   Pointer to [view](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md) from which to get the drawing component

#### Return Value

Pointer to the [IDrawingComponent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent.md) object

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)
