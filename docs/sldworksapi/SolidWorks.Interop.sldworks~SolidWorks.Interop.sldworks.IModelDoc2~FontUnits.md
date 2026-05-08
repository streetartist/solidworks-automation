# FontUnits Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FontUnits`

Changes font height (specified in current system units) in the selected notes, dimensions, and GTols.
Changes font height (specified in current system units) in the selected notes, dimensions, and GTols.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub FontUnits( _
   ByVal Units As System.Double _
) 
```

```

Dim instance As IModelDoc2
Dim Units As System.Double
 
instance.FontUnits(Units)
```

```

void FontUnits( 
   System.double Units
)
```

```

void FontUnits( 
   System.double Units
) 
```

#### Parameters

*Units*
:   Specifies the font height in current system units (for example, inches, millimeters, and so on)

Remarks

You can also use [ITextFormat](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat.md) for full control of text formatting. Obtain ITextFormat using the appropriate GetTextFormat method (see index entry GetTextFormat for a list of available GetTextFormat methods).

Example

[Add Watermark to Part (C#)](Add_Watermark_to_Part_Example_CSharp.htm)  
[Add Watermark to Part (VB.NET)](Add_Watermark_to_Part_Example_VBNET.htm)  
[Add Watermark to Part (VBA)](Add_Watermark_to_Part_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::FontBold Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FontBold.md)  
[IModelDoc2::FontFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FontFace.md)  
[IModelDoc2::FontItalic Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FontItalic.md)  
[IModelDoc2::FontPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FontPoints.md)  
[IModelDoc2::FontUnderline Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FontUnderline.md)
