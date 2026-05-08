# SetDual2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetDual2`

Controls the display of dual dimensions of this display dimension.
Controls the display of dual dimensions of this display dimension.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetDual2( _
   ByVal UseDoc As System.Boolean, _
   ByVal InwardRounding As System.Boolean _
) 
```

```

Dim instance As IDisplayDimension
Dim UseDoc As System.Boolean
Dim InwardRounding As System.Boolean
 
instance.SetDual2(UseDoc, InwardRounding)
```

```

void SetDual2( 
   System.bool UseDoc,
   System.bool InwardRounding
)
```

```

void SetDual2( 
   System.bool UseDoc,
   System.bool InwardRounding
) 
```

#### Parameters

*UseDoc*
:   True uses the document setting, false uses the opposite of the document setting (see **Remarks**)

*InwardRounding*
:   True for inward rounding of secondary unit tolerances, false for current document rounding (see **Remarks**)

Remarks

Dual dimensions can use either the same top, bottom, right, or left setting as the document or an opposite top, bottom, right, or left setting. This method allows you to set a dual dimension to use the current document setting or the opposite setting.

| If InwardRounding is false and an override unit is... | Then... |
| --- | --- |
| Not specified | Current document rounding prevails |
| Specified | Rounding setting under **Override Units** in the Dimensions PropertyManager page prevails |

Use [IDisplayDimension::GetUseDocDual](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUseDocDual.md) to get the current value of this setting.

After using this method, use [IModelDoc2::GraphicsRedraw2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GraphicsRedraw2.md) to redraw the graphics window to see your changes.

Example

[Set Rounding of Decimal Units in Display Dimensions (VBA)](Set_Rounding_of_Decimal_Units_in_Display_Dimensions_Example_VB.htm)  
[Set Rounding of Decimal Units in Display Dimensions (VB.NET)](Set_Rounding_of_Decimal_Units_in_Display_Dimensions_Example_VBNET.htm)  
[Set Rounding of Decimal Units in Display Dimensions (C#)](Set_Rounding_of_Decimal_Units_in_Display_Dimensions_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::Split Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~Split.md)
