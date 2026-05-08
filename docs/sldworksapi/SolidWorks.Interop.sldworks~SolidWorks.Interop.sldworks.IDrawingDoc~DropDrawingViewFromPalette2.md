# DropDrawingViewFromPalette2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~DropDrawingViewFromPalette2`

Moves the specified drawing view from the View Palette to the current drawing sheet.
Moves the specified drawing view from the View Palette to the current drawing sheet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function DropDrawingViewFromPalette2( _
   ByVal PaletteViewName As System.String, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As View
```

```

Dim instance As IDrawingDoc
Dim PaletteViewName As System.String
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As View
 
value = instance.DropDrawingViewFromPalette2(PaletteViewName, X, Y, Z)
```

```

View DropDrawingViewFromPalette2( 
   System.string PaletteViewName,
   System.double X,
   System.double Y,
   System.double Z
)
```

```

View^ DropDrawingViewFromPalette2( 
   System.String^ PaletteViewName,
   System.double X,
   System.double Y,
   System.double Z
) 
```

#### Parameters

*PaletteViewName*
:   Name of the drawing view to move to the drawing sheet

*X*
:   x coordinate where to drop the drawing view

*Y*
:   y coordinate where to drop the drawing view

*Z*
:   z coordinate where to drop the drawing view; this coordinate is always 0

#### Return Value

[View](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)

Remarks

The x, y, and z coordinates are in paper space. Thus, the drawing sheet scale is irrelevant.

Example

[Drop Drawing Views from View Palette (VBA)](Drop_Drawing_Views_from_View_Palette_Example_VB.htm)  
[Drop First Drawing View from View Palette (VBA)](Drop_First_Drawing_View_from_View_Palette_Example_VB.htm)  
[Get the Number of Lines in Flat-pattern Drawing View's Boundary-box Sketch (C#)](Get_Number_of_Lines_Flat-pattern_Drawing_View_Boundary-box_Sketch_Example_CSharp.htm)  
[Get the Number of Lines in Flat-pattern Drawing View's Boundary-box Sketch (VB.NET)](Get_Number_of_Lines_Flat-pattern_Drawing_View_Boundary-box_Sketch_Example_VBNET.htm)  
[Get the Number of Lines in Flat-pattern Drawing View's Boundary-box Sketch (VBA)](Get_Number_of_Lines_Flat-pattern_Drawing_View_Boundary-box_Sketch_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDrawingDoc::GenerateViewPaletteViews Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GenerateViewPaletteViews.md)  
[IDrawingDoc::GetDrawingPaletteViewNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetDrawingPaletteViewNames.md)
