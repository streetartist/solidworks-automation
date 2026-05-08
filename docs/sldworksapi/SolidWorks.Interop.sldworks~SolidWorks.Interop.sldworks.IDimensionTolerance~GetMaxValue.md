# GetMaxValue Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetMaxValue`

Obsolete. Superseded by IDimensionTolerance::GetMaxValue2.
Obsolete. Superseded by [IDimensionTolerance::GetMaxValue2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetMaxValue2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetMaxValue() As System.Double
```

```

Dim instance As IDimensionTolerance
Dim value As System.Double
 
value = instance.GetMaxValue()
```

```

System.double GetMaxValue()
```

```

System.double GetMaxValue(); 
```

#### Return Value

Tolerance maximum value

Remarks

Depending on the [tolerance type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~Type.md), the tolerance minimum and maximum values might not be visible.

To:

- get the tolerance minimum value, use [IDimensionTolerance::GetMinValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetMinValue.md).
- set the tolerance values, use [IDimensionTolerance::SetValues](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~SetValues.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDimensionTolerance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance.md)  
[IDimensionTolerance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance_members.md)
