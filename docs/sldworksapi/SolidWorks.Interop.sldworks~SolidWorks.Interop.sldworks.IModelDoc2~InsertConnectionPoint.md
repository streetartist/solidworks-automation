# InsertConnectionPoint Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertConnectionPoint`

Adds a connection point based on the selected point and selected planar item.
Adds a connection point based on the selected point and selected planar item.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub InsertConnectionPoint() 
```

```

Dim instance As IModelDoc2
 
instance.InsertConnectionPoint()
```

```

void InsertConnectionPoint()
```

```

void InsertConnectionPoint(); 
```

Remarks

If the selection set is not complete, then the Insert Connection Point dialog is displayed.

The connection point is the point on the fitting that defines where the connection to other pipe items begins or ends.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
