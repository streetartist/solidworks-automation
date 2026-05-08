# View Property (IDrawingComponent)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~View`

Gets the drawing view on which this component resides.
Gets the drawing view on which this component resides.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property View As View
```

```

Dim instance As IDrawingComponent
Dim value As View
 
value = instance.View
```

```

View View {get;}
```

```

property View^ View {
   View^ get();
}
```

#### Property Value

Pointer to the [IView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md) object on which this component resides

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent.md)  
[IDrawingComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent_members.md)
