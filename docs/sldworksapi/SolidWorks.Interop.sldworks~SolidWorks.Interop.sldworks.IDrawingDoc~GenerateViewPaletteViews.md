# GenerateViewPaletteViews Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GenerateViewPaletteViews`

Adds the specified document's predefined drawing views to the View Palette.
Adds the specified document's predefined drawing views to the View Palette.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GenerateViewPaletteViews( _
   ByVal FileName As System.String _
) As System.Boolean
```

```

Dim instance As IDrawingDoc
Dim FileName As System.String
Dim value As System.Boolean
 
value = instance.GenerateViewPaletteViews(FileName)
```

```

System.bool GenerateViewPaletteViews( 
   System.string FileName
)
```

```

System.bool GenerateViewPaletteViews( 
   System.String^ FileName
) 
```

#### Parameters

*FileName*
:   Path and file name of the document from which to add the predefined drawing views to the View Palette

#### Return Value

True if the drawing views are added to the View Palette, false if not

Example

[Get and Set Whether to Hide Cutting Line Shoulders (C#)](Get_and_Set_Whether_to_Hide_Cutting_Line_Shoulders_Example_CSharp.htm)  
[Get and Set Whether to Hide Cutting Line Shoulders (VB.NET)](Get_and_Set_Whether_to_Hide_Cutting_Line_Shoulders_Example_VBNET.htm)  
[Get and Set Whether to Hide Cutting Line Shoulders (VBA)](Get_and_Set_Whether_to_Hide_Cutting_Line_Shoulders_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDrawingDoc::DropDrawingViewFromPalette2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~DropDrawingViewFromPalette2.md)  
[IDrawingDoc::GetDrawingPaletteViewNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetDrawingPaletteViewNames.md)
