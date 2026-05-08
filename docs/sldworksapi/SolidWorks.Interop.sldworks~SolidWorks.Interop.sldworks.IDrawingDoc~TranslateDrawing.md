# TranslateDrawing Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~TranslateDrawing`

Translates the entire drawing.
Translates the entire drawing.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub TranslateDrawing( _
   ByVal DeltaX As System.Double, _
   ByVal DeltaY As System.Double _
) 
```

```

Dim instance As IDrawingDoc
Dim DeltaX As System.Double
Dim DeltaY As System.Double
 
instance.TranslateDrawing(DeltaX, DeltaY)
```

```

void TranslateDrawing( 
   System.double DeltaX,
   System.double DeltaY
)
```

```

void TranslateDrawing( 
   System.double DeltaX,
   System.double DeltaY
) 
```

#### Parameters

*DeltaX*
:   Delta X value for the translation operation

*DeltaY*
:   Delta Y value for the translation operation

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)
