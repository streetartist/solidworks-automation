# EndDrawing Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~EndDrawing`

Provides faster creation of entities in a drawing when used with IDrawingDoc::StartDrawing.
Provides faster creation of entities in a drawing when used with [IDrawingDoc::StartDrawing](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~StartDrawing.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub EndDrawing() 
```

```

Dim instance As IDrawingDoc
 
instance.EndDrawing()
```

```

void EndDrawing()
```

```

void EndDrawing(); 
```

Remarks

Use [IDrawingDoc::StartDrawing](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~StartDrawing.md) and this method to bound your entity creation statements.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)
