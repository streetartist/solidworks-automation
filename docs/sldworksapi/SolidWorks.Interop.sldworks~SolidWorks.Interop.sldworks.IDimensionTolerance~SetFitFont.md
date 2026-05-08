# SetFitFont Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~SetFitFont`

Sets the fit tolerance font values.
Sets the fit tolerance font values.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetFitFont( _
   ByVal UseDimension As System.Boolean, _
   ByVal UseScale As System.Boolean, _
   ByVal Value As System.Double _
) As System.Boolean
```

```

Dim instance As IDimensionTolerance
Dim UseDimension As System.Boolean
Dim UseScale As System.Boolean
Dim Value As System.Double
Dim value As System.Boolean
 
value = instance.SetFitFont(UseDimension, UseScale, Value)
```

```

System.bool SetFitFont( 
   System.bool UseDimension,
   System.bool UseScale,
   System.double Value
)
```

```

System.bool SetFitFont( 
   System.bool UseDimension,
   System.bool UseScale,
   System.double Value
) 
```

#### Parameters

*UseDimension*
:   True if the fit tolerance font should be the same size as the dimension font, false if not

*UseScale*
:   True if the fit tolerance font should be scaled based on the dimension font, false if the fit tolerance font size is an absolute height value

*Value*
:   Scale ratio if UseScale is true or height value if UseScale is false

#### Return Value

True if the fit tolerance font is set, false if not

Remarks

|  |  |
| --- | --- |
| **If UseDimension is...** | **Then...** |
| True | - The other arguments are ignored. - UseScale is true. - Value is 1.0. |
| False | UseScale determines how Value is interpreted.   |  |  | | --- | --- | | **If UseScale is...** | **Then Value is assumed to be...** | | True | Scale value to use, and the height value is not changed. | | False | Height value to use, and the scale value is not changed. | |

To get the fit tolerance font information, use [IDimensionTolerance::GetFitFontUseDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFitFontUseDimension.md), [IDimensionTolerance::GetFitFontUseScale](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFitFontUseScale.md), [IDimensionTolerance::GetFitFontScale](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFitFontScale.md), and [IDimensionTolerance::GetFitFontHeight](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFitFontHeight.md).

This method deals with the fit tolerance font information, not the tolerance font information. To get or set tolerance information, use [IDimensionTolerance::GetFontUseDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFontUseDimension.md), [IDimensionTolerance::GetFontUseScale](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFontUseScale.md), [IDimensionTolerance::GetFontScale](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFontScale.md), [IDimensionTolerance::GetFontHeight](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFontHeight.md), and [IDimensionTolerance::SetFont](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~SetFont.md).

To see the effects of changing the fit tolerance font information, use [IModelDoc2::GraphicsRedraw2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GraphicsRedraw2.md).

Example

[Get Dimension Tolerance (C#)](Get_Dimension_Tolerance_Example_CSharp.htm)  
[Get Dimension Tolerance (VB.NET)](Get_Dimension_Tolerance_Example_VBNET.htm)  
[Get Dimension Tolerance (VBA)](Get_Dimension_Tolerance_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDimensionTolerance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance.md)  
[IDimensionTolerance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance_members.md)  
[IDimensionTolerance::FitDisplayStyle Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~FitDisplayStyle.md)  
[IDimensionTolerance::FitType Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~FitType.md)
