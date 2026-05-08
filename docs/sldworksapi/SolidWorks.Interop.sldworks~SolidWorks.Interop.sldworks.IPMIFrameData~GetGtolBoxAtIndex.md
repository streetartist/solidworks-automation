# GetGtolBoxAtIndex Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIFrameData~GetGtolBoxAtIndex`

Gets the specified tolerance box in this Gtol frame.
Gets the specified tolerance box in this Gtol frame.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetGtolBoxAtIndex( _
   ByVal Index As System.Integer _
) As System.Object
```

```

Dim instance As IPMIFrameData
Dim Index As System.Integer
Dim value As System.Object
 
value = instance.GetGtolBoxAtIndex(Index)
```

```

System.object GetGtolBoxAtIndex( 
   System.int Index
)
```

```

System.Object^ GetGtolBoxAtIndex( 
   System.int Index
) 
```

#### Parameters

*Index*
:   0 <= Gtol frame box index <= 2

#### Return Value

[IPMIGtolBoxData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData.md)

Remarks

Use [IPMIFrameData::GetGtolBoxCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIFrameData~GetGtolBoxCount.md) to determine Index.

Example

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPMIFrameData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIFrameData.md)  
[IPMIFrameData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIFrameData_members.md)
