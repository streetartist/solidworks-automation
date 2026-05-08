# SetValues2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~SetValues2`

Sets the tolerance minimum and maximum values of a dimension.
Sets the tolerance minimum and maximum values of a [dimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetValues2( _
   ByVal MinValue As System.Double, _
   ByVal MaxValue As System.Double, _
   ByVal WhichConfigurations As System.Integer, _
   ByVal Config_names As System.Object _
) As System.Boolean
```

```

Dim instance As IDimensionTolerance
Dim MinValue As System.Double
Dim MaxValue As System.Double
Dim WhichConfigurations As System.Integer
Dim Config_names As System.Object
Dim value As System.Boolean
 
value = instance.SetValues2(MinValue, MaxValue, WhichConfigurations, Config_names)
```

```

System.bool SetValues2( 
   System.double MinValue,
   System.double MaxValue,
   System.int WhichConfigurations,
   System.object Config_names
)
```

```

System.bool SetValues2( 
   System.double MinValue,
   System.double MaxValue,
   System.int WhichConfigurations,
   System.Object^ Config_names
) 
```

#### Parameters

*MinValue*
:   Dimension tolerance minimum value

*MaxValue*
:   Dimension tolerance maximum value

*WhichConfigurations*
:   Configurations to which to set the dimension tolerance minimum and maximum values as defined in [swSetValueInConfiguration\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSetValueInConfiguration_e.html)

*Config\_names*
:   Names of the configurations for which to set dimension tolerance values

#### Return Value

True if the dimension tolerance values are set, false if not

Remarks

You cannot set the dimension tolerance values if the [tolerance type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~Type.md) is [swTolType\_e.swTolNONE](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTolType_e.html). Depending on the tolerance type, the dimension tolerance minimum and maximum values might not be visible.

|  |  |
| --- | --- |
| **To get the dimension tolerance...** | **Use...** |
| Minimum value | [IDimensionTolerance::GetMinValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetMinValue.md) |
| Maximum value | [IDimensionTolerance::GetMaxValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetMaxValue.md) |

To see the effects of changing the dimension tolerance values, call [IModelView::GraphicsRedraw](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GraphicsRedraw.md).

Example

[Change Dimension Tolerance in a Configuration (C#)](Change_Dimension_Tolerance_in_Configuration_Example_CSharp.htm)  
[Change Dimension Tolerance in a Configuration (VB.NET)](Change_Dimension_Tolerance_in_Configuration_Example_VBNET.htm)  
[Change Dimension Tolerance in a Configuration (VBA)](Change_Dimension_Tolerance_in_Configuration_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDimensionTolerance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance.md)  
[IDimensionTolerance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance_members.md)
