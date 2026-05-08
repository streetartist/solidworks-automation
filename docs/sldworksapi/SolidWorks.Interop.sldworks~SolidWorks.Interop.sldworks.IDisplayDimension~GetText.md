# GetText Method (IDisplayDimension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetText`

Gets the text above the dimension line in a display dimension.
Gets the text above the dimension line in a display dimension.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetText( _
   ByVal WhichText As System.Integer _
) As System.String
```

```

Dim instance As IDisplayDimension
Dim WhichText As System.Integer
Dim value As System.String
 
value = instance.GetText(WhichText)
```

```

System.string GetText( 
   System.int WhichText
)
```

```

System.String^ GetText( 
   System.int WhichText
) 
```

#### Parameters

*WhichText*
:   Aspect of the text to get as defined in [swDimensionTextParts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDimensionTextParts_e.html) (see **Remarks**)

#### Return Value

Text above the dimension line

Remarks

swDimensionTextParts\_e.swDimensionTextAll is not a valid value for the WhichText parameter for this method.

**NOTE:** This method does not support [hole callouts](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~IsHoleCallout.md).

Example

[Get Block Information (VBA)](Get_Block_Information_Example_VB.htm)  
[Get Dimension Values in Drawing (VBA)](Get_Dimension_Values_in_Drawing_Example_VB.htm)  
[Get Whether Display Dimension is a Hole Callout (VBA)](Get_Whether_Display_Dimension_is_a_Hole_Callout_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::SetText Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetText.md)  
[IDisplayDimension::GetLowerText Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetLowerText.md)  
[IDisplayDimension::SetLowerText Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetLowerText.md)
