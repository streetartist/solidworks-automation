# StartDrawing Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~StartDrawing`

Provides faster creation of entities within a drawing.
Provides faster creation of entities within a drawing.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub StartDrawing() 
```

```

Dim instance As IDrawingDoc
 
instance.StartDrawing()
```

```

void StartDrawing()
```

```

void StartDrawing(); 
```

Remarks

This method automatically disables inferencing to provide faster geometry creation. Use this method and [IDrawingDoc::EndDrawing](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~EndDrawing.md) to bound your entity creation statements.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)
