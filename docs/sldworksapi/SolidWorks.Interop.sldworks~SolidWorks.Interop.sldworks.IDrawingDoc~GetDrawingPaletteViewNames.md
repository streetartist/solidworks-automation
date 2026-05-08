# GetDrawingPaletteViewNames Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetDrawingPaletteViewNames`

Gets the names of drawing views in the View Palette for the active drawing sheet.
Gets the names of drawing views in the View Palette for the active drawing sheet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDrawingPaletteViewNames() As System.Object
```

```

Dim instance As IDrawingDoc
Dim value As System.Object
 
value = instance.GetDrawingPaletteViewNames()
```

```

System.object GetDrawingPaletteViewNames()
```

```

System.Object^ GetDrawingPaletteViewNames(); 
```

#### Return Value

Array of the names of the drawing views in the View Palette for the active drawing sheet

Remarks

|  |  |
| --- | --- |
| If... | Then this method... |
| a part or assembly was not pre-selected for the View Palette (i.e., the View Palette is empty) | returns an empty array. |
| an end-user moves a drawing view from the View Palette to the drawing sheet (either through the user-interface or via an API) | does not include that drawing name the next time this method is called. |

Example

[Drop Drawing Views from View Palette (VBA)](Drop_Drawing_Views_from_View_Palette_Example_VB.htm)  
[Drop First Drawing View from View Palette (VBA)](Drop_Drawing_Views_from_View_Palette_Example_VB.htm)  
[Get Number of Lines in Flat-pattern Drawing View's Boundary-box Sketch (C#)](Get_Number_of_Lines_Flat-pattern_Drawing_View_Boundary-box_Sketch_Example_CSharp.htm)  
[Get Number of Lines in Flat-pattern Drawing View's Boundary-box Sketch (VB.NET)](Get_Number_of_Lines_Flat-pattern_Drawing_View_Boundary-box_Sketch_Example_VBNET.htm)  
[Get Number of Lines in Flat-pattern Drawing View's Boundary-box Sketch (VBA)](Get_Number_of_Lines_Flat-pattern_Drawing_View_Boundary-box_Sketch_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDrawingDoc::DropDrawingViewFromPalette2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~DropDrawingViewFromPalette2.md)  
[IDrawingDoc::GenerateViewPaletteViews Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GenerateViewPaletteViews.md)
