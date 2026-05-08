# SetRadius Method (ISheetMetalGaugeTableParameters)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~SetRadius`

Sets the bend radius in this gauge table.
Sets the bend radius in this gauge table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetRadius( _
   ByVal Radius As System.Double, _
   ByVal Override As System.Boolean _
) As System.Boolean
```

```

Dim instance As ISheetMetalGaugeTableParameters
Dim Radius As System.Double
Dim Override As System.Boolean
Dim value As System.Boolean
 
value = instance.SetRadius(Radius, Override)
```

```

System.bool SetRadius( 
   System.double Radius,
   System.bool Override
)
```

```

System.bool SetRadius( 
   System.double Radius,
   System.bool Override
) 
```

#### Parameters

*Radius*
:   Bend radius

*Override*
:   True to override an existing value, false to not (see **Remarks**)

#### Return Value

True if bend radius successfully set, false if not

Remarks

If Override is:

- true, then specify an override bend radius in Radius.
- false, then specify Radius using one of the default bend radii for the current gauge number from the gauge table. Use [ISheetMetalGaugeTableParameters::GetAvailableRadii](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~GetAvailableRadii.md) to choose a value for Radius.

Example

See the [ISheetMetalGaugeTableParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISheetMetalGaugeTableParameters Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters.md)  
[ISheetMetalGaugeTableParameters Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters_members.md)  
[ISheetMetalGaugeTableParameters::OverrideRadius Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~OverrideRadius.md)  
[ISheetMetalGaugeTableParameters::GetCurrentRadius Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~GetCurrentRadius.md)  
[ISheetMetalGaugeTableParameters::GetRadiiCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~GetRadiiCount.md)  
[ISheetMetalGaugeTableParameters::SetThickness Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~SetThickness.md)
