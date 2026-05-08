# DragCorrected Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~DragCorrected`

Gets whether or not the drag operation was corrected.
Gets whether or not the drag operation was corrected.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property DragCorrected As System.Boolean
```

```

Dim instance As IDragOperator
Dim value As System.Boolean
 
value = instance.DragCorrected
```

```

System.bool DragCorrected {get;}
```

```

property System.bool DragCorrected {
   System.bool get();
}
```

#### Property Value

True if remedial action occurred, false if not

Remarks

If the desired orientation set by [IDragOperator::Drag](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~Drag.md) or [IDragOperator::IDrag](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~IDrag.md) was not honored and remedial action occurred, then this property is set. This property is not set by [IDragOperator::DragAsUI](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~DragAsUI.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDragOperator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator.md)  
[IDragOperator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator_members.md)
