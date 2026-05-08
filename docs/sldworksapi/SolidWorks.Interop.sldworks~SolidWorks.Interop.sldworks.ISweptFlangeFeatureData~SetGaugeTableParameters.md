# SetGaugeTableParameters Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~SetGaugeTableParameters`

Sets the gauge table parameters object.
Sets the gauge table parameters object.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetGaugeTableParameters( _
   ByVal DispIn As System.Object _
) 
```

```

Dim instance As ISweptFlangeFeatureData
Dim DispIn As System.Object
 
instance.SetGaugeTableParameters(DispIn)
```

```

void SetGaugeTableParameters( 
   System.object DispIn
)
```

```

void SetGaugeTableParameters( 
   System.Object^ DispIn
) 
```

#### Parameters

*DispIn*
:   [ISheetMetalGaugeTableParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters.md)

Remarks

This method is valid only if [ISweptFlangeFeatureData::UseGaugeTable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~UseGaugeTable.md) is true.

Use [ISweptFlangeFeatureData::GetGaugeTableParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~GetGaugeTableParameters.md) to specify DispIn.

Example

See the [ISheetMetalGaugeTableParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISweptFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.md)  
[ISweptFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData_members.md)
