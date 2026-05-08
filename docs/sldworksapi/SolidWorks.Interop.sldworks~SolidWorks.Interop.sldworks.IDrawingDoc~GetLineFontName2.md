# GetLineFontName2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetLineFontName2`

Gets the name of the specified line font.
Gets the name of the specified line font.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetLineFontName2( _
   ByVal Index As System.Integer _
) As System.String
```

```

Dim instance As IDrawingDoc
Dim Index As System.Integer
Dim value As System.String
 
value = instance.GetLineFontName2(Index)
```

```

System.string GetLineFontName2( 
   System.int Index
)
```

```

System.String^ GetLineFontName2( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Index position of the line font which is within the index range returned by [IDrawingDoc::GetLineFontCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetLineFontCount2.md)

#### Return Value

Line font name

Remarks

This method can return a font name Hidden, Visible, etc.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDrawingDoc::GetLineFontId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetLineFontId.md)  
[IDrawingDoc::GetLineFontInfo2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetLineFontInfo2.md)  
[IDrawingDoc::SetLineColor Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetLineColor.md)  
[IDrawingDoc::SetLineStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetLineStyle.md)  
[IDrawingDoc::SetLineWidth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetLineWidth.md)  
[IDrawingDoc::GetLineFontCount2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetLineFontCount2.md)
