# SetFont Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~SetFont`

Sets the tolerance font values.
Sets the tolerance font values.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetFont( _
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
 
value = instance.SetFont(UseDimension, UseScale, Value)
```

```

System.bool SetFont( 
   System.bool UseDimension,
   System.bool UseScale,
   System.double Value
)
```

```

System.bool SetFont( 
   System.bool UseDimension,
   System.bool UseScale,
   System.double Value
) 
```

#### Parameters

*UseDimension*
:   True if the tolerance font should be the same size as the dimension font, false if not

*UseScale*
:   True if the tolerance font size should be scaled based on the dimension font size, false if the tolerance font size is an absolute height value

*Value*
:   Scale ratio if UseScale is true or height value if UseScale is false

#### Return Value

True if the tolerance font is set, false if not

Remarks

|  |  |
| --- | --- |
| **If UseDimension is...** | **Then...** |
| True | - The other arguments are ignored. - UseScale is True. - Value is 1.0. |
| false | UseScale determines how Value is interpreted.   |  |  | | --- | --- | | If UseScale is... | Then Value is assumed to be the... | | True | scale value to use, and the height value is not changed. | | false | height value to use, and the scale value is not changed. | |

To get the tolerance font information, use [IDimensionTolerance::GetFontUseDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFitFontUseDimension.md), [IDimensionTolerance::GetFontUseScale](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFontUseScale.md), [IDimensionTolerance::GetFontScale](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFontScale.md), and [IDimensionTolerance::GetFontHeight](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFontHeight.md).

This method deals with the tolerance font information, not the fit tolerance font information. To get or set fit tolerance information, use [IDimensionTolerance::GetFitFontUseDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFitFontUseDimension.md), [IDimensionTolerance::GetFitFontUseScale](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFitFontUseScale.md), [IDimensionTolerance::GetFitFontScale](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFitFontScale.md), [IDimensionTolerance::GetFitFontHeight](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetFitFontHeight.md), and [IDimensionTolerance::SetFitFont](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~SetFitFont.md).

To see the effects of changing the tolerance font information, use [IModelDoc2::GraphicsRedraw2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GraphicsRedraw2.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDimensionTolerance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance.md)  
[IDimensionTolerance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance_members.md)
