# RemoveAlignment Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~RemoveAlignment`

Removes the alignment from this drawing view.
Removes the alignment from this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub RemoveAlignment() 
```

```

Dim instance As IView
 
instance.RemoveAlignment()
```

```

void RemoveAlignment()
```

```

void RemoveAlignment(); 
```

Remarks

Using this method on a view only removes the alignment information from that view. It does not remove the alignments any child views have with this view.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::AlignWithView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~AlignWithView.md)  
[IView::UseDefaultAlignment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~UseDefaultAlignment.md)  
[IView::GetAlignment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetAlignment.md)
