# SetText Method (IDisplayDimension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetText`

Sets the text above the dimension line in a display dimension.
Sets the text above the dimension line in a display dimension.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetText( _
   ByVal WhichText As System.Integer, _
   ByVal Text As System.String _
) 
```

```

Dim instance As IDisplayDimension
Dim WhichText As System.Integer
Dim Text As System.String
 
instance.SetText(WhichText, Text)
```

```

void SetText( 
   System.int WhichText,
   System.string Text
)
```

```

void SetText( 
   System.int WhichText,
   System.String^ Text
) 
```

#### Parameters

*WhichText*
:   Aspect of the text to get as defined in [swDimensionTextParts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDimensionTextParts_e.html) (see **Remarks**)

*Text*
:   Text to create above the dimension line

Remarks

Use swDimensionTextParts\_e.swDimensionTextAll to create or replace the entire dimension text. SOLIDWORKS places the input text in the prefix portion of the dimension text, clears the suffix and callout texts, and turns off the dimension value (see [IDisplayDimension::ShowDimensionValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~ShowDimensionValue.md)).

After using this method, use [IModelDoc2::GraphicsRedraw2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GraphicsRedraw2.md) to redraw the graphics window to see your changes.

**NOTE:** This method does not support [hole callouts](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~IsHoleCallout.md).

Example

[Display Grid Bubble (VBA)](Display_Grid_Bubble_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::GetText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetText.md)  
[IDisplayDimension::SetLowerText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetLowerText.md)  
[IDisplayDimension::GetLowerText Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetLowerText.md)
