# SetLineWidth Method (IDrawingDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetLineWidth`

Sets the line thickness for a selected edge or sketch entity to a SOLIDWORKS-supplied weight (width).
Sets the line thickness for a selected edge or sketch entity to a SOLIDWORKS-supplied weight (width).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetLineWidth( _
   ByVal Width As System.Integer _
) 
```

```

Dim instance As IDrawingDoc
Dim Width As System.Integer
 
instance.SetLineWidth(Width)
```

```

void SetLineWidth( 
   System.int Width
)
```

```

void SetLineWidth( 
   System.int Width
) 
```

#### Parameters

*Width*
:   Weight for the line as defined in [swLineWeights\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLineWeights_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDrawingDoc::SetLineColor Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetLineColor.md)  
[IDrawingDoc::SetLineStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetLineStyle.md)  
[IDrawingDoc::GetLineFontCount2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetLineFontCount2.md)  
[IDrawingDoc::GetLineFontId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetLineFontId.md)  
[IDrawingDoc::GetLineFontInfo2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetLineFontInfo2.md)  
[IDrawingDoc::GetLineFontName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetLineFontName2.md)  
[IDrawingDoc::SetLineWidthCustom Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetLineWidthCustom.md)
