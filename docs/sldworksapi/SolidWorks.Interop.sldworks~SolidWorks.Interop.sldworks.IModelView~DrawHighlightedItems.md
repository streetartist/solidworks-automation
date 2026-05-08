# DrawHighlightedItems Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~DrawHighlightedItems`

Draws or redraws the highlighted items.
Draws or redraws the highlighted items.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub DrawHighlightedItems() 
```

```

Dim instance As IModelView
 
instance.DrawHighlightedItems()
```

```

void DrawHighlightedItems()
```

```

void DrawHighlightedItems(); 
```

Remarks

This method is useful in applications that handle repainting if you want highlighting  
to be visible. When called, the currently highlighted items are painted.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.md)  
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.md)
