# SetFitValues Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~SetFitValues`

Sets the tolerance hole fit and shaft fit values.
Sets the tolerance hole fit and shaft fit values.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetFitValues( _
   ByVal HoleFit As System.String, _
   ByVal ShaftFit As System.String _
) As System.Boolean
```

```

Dim instance As IDimensionTolerance
Dim HoleFit As System.String
Dim ShaftFit As System.String
Dim value As System.Boolean
 
value = instance.SetFitValues(HoleFit, ShaftFit)
```

```

System.bool SetFitValues( 
   System.string HoleFit,
   System.string ShaftFit
)
```

```

System.bool SetFitValues( 
   System.String^ HoleFit,
   System.String^ ShaftFit
) 
```

#### Parameters

*HoleFit*
:   Tolerance hole fit value

*ShaftFit*
:   Tolerance shaft fit value

#### Return Value

True if the setting of the fit values is successful, false if not

Remarks

|  |  |
| --- | --- |
| **To get tolerance...** | **Use...** |
| Hole fit value | [IDimensionTolerance::GetHoleFitValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetHoleFitValue.md) |
| Shaft fit value | [IDimensionTolerance::GetShaftFitValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~GetShaftFitValue.md) |

To see the effects of changing the tolerance fit values, use [IModelDoc2::GraphicsRedraw2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GraphicsRedraw2.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDimensionTolerance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance.md)  
[IDimensionTolerance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance_members.md)  
[IDimensionTolerance::FitType Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance~FitType.md)  
[ICalloutVariable::HoleFit Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~HoleFit.md)  
[ICalloutVariable::ShaftFit Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable~ShaftFit.md)
