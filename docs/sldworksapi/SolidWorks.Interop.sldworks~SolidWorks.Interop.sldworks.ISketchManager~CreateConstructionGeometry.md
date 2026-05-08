# CreateConstructionGeometry Method (ISketchManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateConstructionGeometry`

Sets selected sketch segments to be construction geometry instead of sketch geometry.
Sets selected sketch segments to be construction geometry instead of sketch geometry.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub CreateConstructionGeometry() 
```

```

Dim instance As ISketchManager
 
instance.CreateConstructionGeometry()
```

```

void CreateConstructionGeometry()
```

```

void CreateConstructionGeometry(); 
```

Remarks

This method supports all document types, unlike [IDrawingDoc::CreateConstructionGeometry](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateConstructionGeometry.md), which only supports drawing documents. Both methods perform the same functionality.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)
