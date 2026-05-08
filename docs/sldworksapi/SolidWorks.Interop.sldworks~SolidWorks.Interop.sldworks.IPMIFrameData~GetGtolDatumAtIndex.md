# GetGtolDatumAtIndex Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIFrameData~GetGtolDatumAtIndex`

Gets the specified datum box in this Gtol frame.
Gets the specified datum box in this Gtol frame.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetGtolDatumAtIndex( _
   ByVal Index As System.Integer _
) As System.Object
```

```

Dim instance As IPMIFrameData
Dim Index As System.Integer
Dim value As System.Object
 
value = instance.GetGtolDatumAtIndex(Index)
```

```

System.object GetGtolDatumAtIndex( 
   System.int Index
)
```

```

System.Object^ GetGtolDatumAtIndex( 
   System.int Index
) 
```

#### Parameters

*Index*
:   0 <= Gtol frame datum index <= 2

#### Return Value

[IPMIGtolFrameDatum](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolFrameDatum.md)

Remarks

Use [IPMIFrameData::GetGtolDatumCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIFrameData~GetGtolDatumCount.md) to determine Index.

Example

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPMIFrameData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIFrameData.md)  
[IPMIFrameData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIFrameData_members.md)
