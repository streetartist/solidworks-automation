# SetUnits2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetUnits2`

Sets the unit display characteristics of this display dimension.
Sets the unit display characteristics of this display dimension.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetUnits2( _
   ByVal UseDoc As System.Boolean, _
   ByVal UType As System.Integer, _
   ByVal FractBase As System.Integer, _
   ByVal FractDenom As System.Integer, _
   ByVal RoundToFraction As System.Boolean, _
   ByVal DecimalRounding As System.Integer _
) As System.Integer
```

```

Dim instance As IDisplayDimension
Dim UseDoc As System.Boolean
Dim UType As System.Integer
Dim FractBase As System.Integer
Dim FractDenom As System.Integer
Dim RoundToFraction As System.Boolean
Dim DecimalRounding As System.Integer
Dim value As System.Integer
 
value = instance.SetUnits2(UseDoc, UType, FractBase, FractDenom, RoundToFraction, DecimalRounding)
```

```

System.int SetUnits2( 
   System.bool UseDoc,
   System.int UType,
   System.int FractBase,
   System.int FractDenom,
   System.bool RoundToFraction,
   System.int DecimalRounding
)
```

```

System.int SetUnits2( 
   System.bool UseDoc,
   System.int UType,
   System.int FractBase,
   System.int FractDenom,
   System.bool RoundToFraction,
   System.int DecimalRounding
) 
```

#### Parameters

*UseDoc*
:   True to use the document settings for units, false to use the setting values passed to this method (see **Remarks**)

*UType*
:   Unit display setting as defined in [swLengthUnit\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLengthUnit_e.html) or [swAngleUnit\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAngleUnit_e.html); valid only if UseDoc is false

*FractBase*
:   Decimal or fraction display setting as defined in [swFractionDisplay\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFractionDisplay_e.html); valid only if UseDoc is false

*FractDenom*
:   Denominator for fraction display; valid only if UseDoc is false

*RoundToFraction*
:   True to round values to the nearest fraction, false to display fractions only if the values are exact; valid only if UseDoc is false

*DecimalRounding*
:   Decimal rounding as defined by [swUnitsDecimalRounding\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUnitsDecimalRounding_e.html); valid only if FractBase is swFractionDisplay\_e.swDECIMAL and UseDoc is false

#### Return Value

Return status (see Remarks)

Remarks

The unit display settings of a display dimension are controlled by a value stored in one of two places: in the owning document or in the individual display dimension. This method allows you to determine which setting to use, the document default or the values specified by UType, FractBase, FractDenom, RoundToFraction, and DecimalRounding.

If UseDoc is true, then the display dimension unit information follows the document settings, and SOLIDWORKS ignores the remaining arguments. SOLIDWORKS also removes any local settings so that if you switch back to the local settings, they are set to default values.

UType indicates the units. Depending on the type of dimension (angular or linear), this parameter takes a value from [swLengthUnit\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLengthUnit_e.html) or [swAngleUnit\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAngleUnit_e.html). If the specified value is invalid, SOLIDWORKS does not change the existing setting, and this method returns an error.

FractBase indicates whether the dimension is displayed as a fraction or a decimal. SOLIDWORKS displays the dimension as a fraction only if it can precisely represent the dimension as a fraction based on the FractDenom setting. However, if the RoundToFraction argument is true, then SOLIDWORKS displays the dimension rounded to the nearest fraction.

FractDenom indicates the fraction precision by specifying the largest fraction denominator used (for example, 4 for 1/4 or 32 for 1/32). Fraction display is valid only if UType is swINCHES or swFEETINCHES.

The return value indicates the success or failure of this method as follows:

| If Return Value is... | Then this method... |
| --- | --- |
| 2 | Failed because UType is invalid |
| 1 | Failed for an unknown reason |
| 0 | Succeeded |

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
[IDisplayDimension::GetUnits Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUnits.md)  
[IDisplayDimension::GetUseDocUnits Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUseDocUnits.md)
