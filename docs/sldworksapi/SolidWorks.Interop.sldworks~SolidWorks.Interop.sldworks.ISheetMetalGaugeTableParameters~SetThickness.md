# SetThickness Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~SetThickness`

Sets the gauge thickness in this gauge table.
Sets the gauge thickness in this gauge table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetThickness( _
   ByVal Thickness As System.Double, _
   ByVal Override As System.Boolean _
) As System.Boolean
```

```

Dim instance As ISheetMetalGaugeTableParameters
Dim Thickness As System.Double
Dim Override As System.Boolean
Dim value As System.Boolean
 
value = instance.SetThickness(Thickness, Override)
```

```

System.bool SetThickness( 
   System.double Thickness,
   System.bool Override
)
```

```

System.bool SetThickness( 
   System.double Thickness,
   System.bool Override
) 
```

#### Parameters

*Thickness*
:   Gauge thickness

*Override*
:   True to override an existing value, false to not (see **Remarks**)

#### Return Value

True if gauge thickness successfully set, false if not

Remarks

If Override is:

- true, then specify Thickness using an override gauge thickness. You should also use [ISheetMetalGaugeTableParameters::SetRadius](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~SetRadius.md) to override the bend radius.
- false, instead of calling this method use [ISheetMetalGaugeTableParameters::GetAvailableGaugeNumbers](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~GetAvailableGaugeNumbers.md) and [ISheetMetalGaugeTableParameters::SetCurrentGaugeNumber](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~SetCurrentGaugeNumber.md) to change the current gauge number. Each gauge number has a default thickness.

Example

See the [ISheetMetalGaugeTableParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISheetMetalGaugeTableParameters Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters.md)  
[ISheetMetalGaugeTableParameters Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters_members.md)  
[ISheetMetalGaugeTableParameters::GetThickness Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~GetThickness.md)  
[ISheetMetalGaugeTableParameters::OverrideThickness Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~OverrideThickness.md)  
[ISheetMetalGaugeTableParameters::ReverseDirection Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~ReverseDirection.md)
