# GetView Method (IDetailCircle)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~GetView`

Gets the the drawing view that displays this detail circle.
Gets the the drawing view that displays this detail circle.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetView() As View
```

```

Dim instance As IDetailCircle
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

Pointer to the [IView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md) object

Remarks

This is the owning drawing view from which the detail view was derived.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDetailCircle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle.md)  
[IDetailCircle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle_members.md)
