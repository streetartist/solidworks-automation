# SetValues Method (IDimensionTolerance)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~SetValues`

Obsolete. Superseded by IDimensionTolerance::SetValues2.
Obsolete. Superseded by [IDimensionTolerance::SetValues2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~SetValues2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetValues( _
   ByVal MinValue As System.Double, _
   ByVal MaxValue As System.Double _
) As System.Boolean
```

```

Dim instance As IDimensionTolerance
Dim MinValue As System.Double
Dim MaxValue As System.Double
Dim value As System.Boolean
 
value = instance.SetValues(MinValue, MaxValue)
```

```

System.bool SetValues( 
   System.double MinValue,
   System.double MaxValue
)
```

```

System.bool SetValues( 
   System.double MinValue,
   System.double MaxValue
) 
```

#### Parameters

*MinValue*
:   Tolerance minimum value

*MaxValue*
:   Tolerance maximum value

#### Return Value

True if the minimum and maximum tolerance values are set, false if not

Remarks

You cannot set the dimension tolerance values if the [tolerance type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~Type.md) is [swTolType\_e.swTolNONE](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTolType_e.html). Depending on the tolerance type, the dimension tolerance minimum and maximum values might not be visible.

|  |  |
| --- | --- |
| **To get tolerance...** | **Use...** |
| Minimum value | [IDimensionTolerance::GetMinValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetMinValue.md) |
| Maximum value | [IDimensionTolerance::GetMaxValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetMaxValue.md) |

To see the effects of changing the tolerance values, call [IModelDoc2::GraphicsRedraw2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GraphicsRedraw2.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDimensionTolerance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance.md)  
[IDimensionTolerance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance_members.md)
