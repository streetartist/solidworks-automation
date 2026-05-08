# GetMinValue2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetMinValue2`

Gets the tolerance minimum value.
Gets the tolerance minimum value.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetMinValue2( _
   ByRef ToleranceValue As System.Double _
) As System.Integer
```

```

Dim instance As IDimensionTolerance
Dim ToleranceValue As System.Double
Dim value As System.Integer
 
value = instance.GetMinValue2(ToleranceValue)
```

```

System.int GetMinValue2( 
   out System.double ToleranceValue
)
```

```

System.int GetMinValue2( 
   [Out] System.double ToleranceValue
) 
```

#### Parameters

*ToleranceValue*
:   Tolerance minimum value

#### Return Value

Status of tolerance minimum value as defined in [swDimensionToleranceWarning\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swDimensionToleranceWarning_e.html)

Remarks

Depending on the [tolerance type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~Type.md), the tolerance minimum and maximum values might not be visible.

To:

- get the tolerance maximum value, use [IDimensionTolerance::GetMaxValue2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetMaxValue2.md).
- set the tolerance values, use [IDimensionTolerance::SetValues2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~SetValues2.md).

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
