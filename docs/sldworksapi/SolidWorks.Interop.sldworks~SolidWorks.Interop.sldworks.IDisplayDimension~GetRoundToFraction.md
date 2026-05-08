# GetRoundToFraction Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetRoundToFraction`

Gets whether the displayed dimension value is rounded off so that SOLIDWORKS can display it as a fraction.
Gets whether the displayed dimension value is rounded off so that SOLIDWORKS can display it as a fraction.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetRoundToFraction() As System.Boolean
```

```

Dim instance As IDisplayDimension
Dim value As System.Boolean
 
value = instance.GetRoundToFraction()
```

```

System.bool GetRoundToFraction()
```

```

System.bool GetRoundToFraction(); 
```

#### Return Value

True rounds off the displayed dimension value to a fraction, false does not (see **Remarks**)

Remarks

The unit display settings of a display dimension are controlled by a value that SOLIDWORKS stores in one of two places: on the owning document or on the individual display dimension. Use [IDisplayDimension::GetUseDocUnits](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUseDocUnits.md) to determine whether this IDisplayDimension uses the document default or a specific value set for this IDisplayDimension.

If this display dimension uses local unit information, then the return value indicates whether the displayed value of this dimension is rounded off to a value that SOLIDWORKS can represent as a fraction.

Fraction display is valid only for unit types swINCHES or swFEETINCHES. In all other cases, this method returns -1. Use [IDisplayDimension::SetUnits](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetUnits.md) to set the units settings of a display dimension.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md)  
[IDisplayDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.md)  
[GetFractionBase Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetFractionBase.md)  
[GetFractionValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetFractionValue.md)  
[IDisplayDimension::GetUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUnits.md)  
[IDisplayDimension::GetUseDocUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~GetUseDocUnits.md)  
[IDisplayDimension::SetUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension~SetUnits.md)
