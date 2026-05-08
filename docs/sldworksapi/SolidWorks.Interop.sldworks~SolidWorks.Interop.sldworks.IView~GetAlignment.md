# GetAlignment Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetAlignment`

Gets the alignment information of this view.
Gets the alignment information of this view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetAlignment() As System.Integer
```

```

Dim instance As IView
Dim value As System.Integer
 
value = instance.GetAlignment()
```

```

System.int GetAlignment()
```

```

System.int GetAlignment(); 
```

#### Return Value

Alignment information as defined in [swViewAlignment\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swViewAlignment_e.html)

Remarks

The alignment information returned indicates if:

- This view is aligned with a parent view.
- There are child views that are aligned with this view.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::AlignWithView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~AlignWithView.md)  
[IView::RemoveAlignment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~RemoveAlignment.md)  
[IView::UseDefaultAlignment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~UseDefaultAlignment.md)
