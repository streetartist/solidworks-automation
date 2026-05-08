# SetUnits Method (IDisplayDimension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetUnits`

Obsolete. Superseded by IDisplayDimension::SetUnits2.
Obsolete. Superseded by [IDisplayDimension::SetUnits2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetUnits2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetUnits( _
   ByVal UseDoc As System.Boolean, _
   ByVal UType As System.Integer, _
   ByVal FractBase As System.Integer, _
   ByVal FractDenom As System.Integer, _
   ByVal RoundToFraction As System.Boolean _
) As System.Integer
```

```

Dim instance As IDisplayDimension
Dim UseDoc As System.Boolean
Dim UType As System.Integer
Dim FractBase As System.Integer
Dim FractDenom As System.Integer
Dim RoundToFraction As System.Boolean
Dim value As System.Integer
 
value = instance.SetUnits(UseDoc, UType, FractBase, FractDenom, RoundToFraction)
```

```

System.int SetUnits( 
   System.bool UseDoc,
   System.int UType,
   System.int FractBase,
   System.int FractDenom,
   System.bool RoundToFraction
)
```

```

System.int SetUnits( 
   System.bool UseDoc,
   System.int UType,
   System.int FractBase,
   System.int FractDenom,
   System.bool RoundToFraction
) 
```

#### Parameters

*UseDoc*
:   True uses the document settings for units, false uses the setting values passed to the arguments (see **Remarks**)

*UType*
:   Unit display setting as defined in [swLengthUnits\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLengthUnit_e.html) or [swAngleUnits\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAngleUnit_e.html)

*FractBase*
:   Decimal or fraction display setting as defined in [swFractionDisplay\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFractionDisplay_e.html)

*FractDenom*
:   Denominator for fraction display

*RoundToFraction*
:   True rounds values to the nearest fraction, false displays fractions only if the values are exact

#### Return Value

Return status (see Remarks)

Remarks

The unit display settings of a display dimension are controlled by a value stored in one of two places: on the owning document, or on the individual display dimension. This method allows you to determine which setting to use, the document default or the values specified by UType, FractBase, FractDenom, and RoundToFraction.

If the UseDoc argument is true, then the display dimension unit information follows the document settings, and SOLIDWORKS ignores the remaining arguments. SOLIDWORKS also removes any local settings so that if you switch back to the local settings, they are set to default values.

The UType argument indicates the units. Depending on the type of dimension (angular or linear), this parameter takes a value from [swLengthUnits\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLengthUnit_e.html) or [swAngleUnits\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAngleUnit_e.html). If the specified value is invalid, SOLIDWORKS does not change the existing setting and returns an error in the return value.

The FractBase argument indicates whether the dimension is displayed as a fraction or a decimal. This must take a value from [swFractionDisplay\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFractionDisplay_e.html). SOLIDWORKS displays this value as a fraction only if it can be precisely represented as a fraction based on the fraction denominator setting specified in FractDenom. However, if the RoundToFraction argument is true, then SOLIDWORKS forces fraction display by rounding the value to the nearest fraction.

The FractDenom argument indicates the fraction precision by specifying the largest fraction denominator used (for example, 4 for 1/4 or 32 for 1/32). Fraction display is valid only if UType is swINCHES or swFEETINCHES.

The return value indicates the success or failure of this function. It may take one of the following values:

|  |  |
| --- | --- |
| -2 | Command failed because UType is invalid |
| -1 | Command failed for an unknown reason |
| 0 | Command was successful |

After using this method, use [IModelDoc2::GraphicsRedraw2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GraphicsRedraw2.md) to redraw the graphics window to see your changes.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[IDisplayDimension::GetUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUnits.md)  
[IDisplayDimension::GetUseDocUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUseDocUnits.md)
