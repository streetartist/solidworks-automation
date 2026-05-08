# AlignDimensions Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AlignDimensions`

Obsolete. Superseded by IModelDocExtension::AlignDimensions.
Obsolete. Superseded by [IModelDocExtension::AlignDimensions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AlignDimensions.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub AlignDimensions() 
```

```

Dim instance As IModelDoc2
 
instance.AlignDimensions()
```

```

void AlignDimensions()
```

```

void AlignDimensions(); 
```

Remarks

This method attempts to sort the selected dimensions into three groups: linear, ordinate, and angular. Within the linear group, it sorts by measured direction. Each of these dimensions are then aligned with the other like dimensions. These are then updated and dragged together.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::AlignOrdinate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AlignOrdinate.md)  
[IModelDoc2::AlignParallelDimensions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AlignParallelDimensions.md)  
[IModelDoc2::BreakDimensionAlignment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~BreakDimensionAlignment.md)
