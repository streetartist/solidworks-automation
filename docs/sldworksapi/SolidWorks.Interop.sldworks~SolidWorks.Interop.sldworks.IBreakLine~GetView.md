# GetView Method (IBreakLine)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine~GetView`

Gets the drawing view for this break line.
Gets the drawing view for this break line.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetView() As View
```

```

Dim instance As IBreakLine
Dim value As View
 
value = instance.GetView()
```

```

View GetView()
```

```

View^ GetView(); 
```

#### Return Value

Pointer to the [IView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md) object

Remarks

A drawing view can have several breaks. To get all of the breaks in a drawing view, use [IView::GetBreakLines](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetBreakLines.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBreakLine Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine.md)  
[IBreakLine Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine_members.md)
