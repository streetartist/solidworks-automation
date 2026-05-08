# CreateConstructionGeometry Method (IDrawingDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateConstructionGeometry`

Sets the selected sketch segments to be construction geometry instead of sketch geometry.
Sets the selected sketch segments to be construction geometry instead of sketch geometry.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub CreateConstructionGeometry() 
```

```

Dim instance As IDrawingDoc
 
instance.CreateConstructionGeometry()
```

```

void CreateConstructionGeometry()
```

```

void CreateConstructionGeometry(); 
```

Remarks

This method ignores construction geometry when it generates the solid body.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[ISketchManager::CreateConstructionGeometry Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateConstructionGeometry.md)
