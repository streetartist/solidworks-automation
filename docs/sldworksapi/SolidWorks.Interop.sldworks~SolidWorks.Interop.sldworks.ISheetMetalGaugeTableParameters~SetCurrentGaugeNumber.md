# SetCurrentGaugeNumber Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~SetCurrentGaugeNumber`

Sets the current gauge number in this gauge table.
Sets the current gauge number in this gauge table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetCurrentGaugeNumber( _
   ByVal GaugeNumber As System.String _
) As System.Boolean
```

```

Dim instance As ISheetMetalGaugeTableParameters
Dim GaugeNumber As System.String
Dim value As System.Boolean
 
value = instance.SetCurrentGaugeNumber(GaugeNumber)
```

```

System.bool SetCurrentGaugeNumber( 
   System.string GaugeNumber
)
```

```

System.bool SetCurrentGaugeNumber( 
   System.String^ GaugeNumber
) 
```

#### Parameters

*GaugeNumber*
:   Gauge number string (see **Remarks**)

#### Return Value

True if current gauge number successfully set, false if not

Remarks

Use [ISheetMetalGaugeTableParameters::GetAvailableGaugeNumbers](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~GetAvailableGaugeNumbers.md) to determine GaugeNumber.

Example

See the [ISheetMetalGaugeTableParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISheetMetalGaugeTableParameters Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters.md)  
[ISheetMetalGaugeTableParameters Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters_members.md)  
[ISheetMetalGaugeTableParameters::GetCurrentGaugeNumber Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~GetCurrentGaugeNumber.md)  
[ISheetMetalGaugeTableParameters::GetGaugeNumberCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~GetGaugeNumberCount.md)  
[ISheetMetalGaugeTableParameters::SetThickness Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~SetThickness.md)
