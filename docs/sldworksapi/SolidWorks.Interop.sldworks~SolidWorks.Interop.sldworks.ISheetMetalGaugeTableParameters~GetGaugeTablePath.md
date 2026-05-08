# GetGaugeTablePath Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~GetGaugeTablePath`

Gets the full path name of this gauge table.
Gets the full path name of this gauge table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetGaugeTablePath( _
   ByRef GaugeTablePath As System.String _
) As System.Boolean
```

```

Dim instance As ISheetMetalGaugeTableParameters
Dim GaugeTablePath As System.String
Dim value As System.Boolean
 
value = instance.GetGaugeTablePath(GaugeTablePath)
```

```

System.bool GetGaugeTablePath( 
   out System.string GaugeTablePath
)
```

```

System.bool GetGaugeTablePath( 
   [Out] System.String^ GaugeTablePath
) 
```

#### Parameters

*GaugeTablePath*
:   Full path name of the gauge table

#### Return Value

True if gauge table path successfully retrieved, false if not

Example

See the [ISheetMetalGaugeTableParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISheetMetalGaugeTableParameters Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters.md)  
[ISheetMetalGaugeTableParameters Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters_members.md)  
[ISheetMetalGaugeTableParameters::SetGaugeTablePath Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters~SetGaugeTablePath.md)
