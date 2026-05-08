# GetMinValue Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetMinValue`

Obsolete. Superseded by IDimensionTolerance::GetMinValue2.
Obsolete. Superseded by [IDimensionTolerance::GetMinValue2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetMinValue2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetMinValue() As System.Double
```

```

Dim instance As IDimensionTolerance
Dim value As System.Double
 
value = instance.GetMinValue()
```

```

System.double GetMinValue()
```

```

System.double GetMinValue(); 
```

#### Return Value

Tolerance minimum value

Remarks

Depending on the [tolerance type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~Type.md), the tolerance minimum and maximum values might not be visible.

To:

- get the tolerance maximum value, use [IDimensionTolerance::GetMaxValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetMaxValue.md).
- set the tolerance values, use [IDimensionTolerance::SetValues](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~SetValues.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDimensionTolerance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance.md)  
[IDimensionTolerance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance_members.md)
