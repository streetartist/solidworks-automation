# GetFrameAtIndex Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolData~GetFrameAtIndex`

Gets the data of the frame at the specified index of this PMI Gtol.
Gets the data of the frame at the specified index of this PMI Gtol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFrameAtIndex( _
   ByVal Index As System.Integer _
) As System.Object
```

```

Dim instance As IPMIGtolData
Dim Index As System.Integer
Dim value As System.Object
 
value = instance.GetFrameAtIndex(Index)
```

```

System.object GetFrameAtIndex( 
   System.int Index
)
```

```

System.Object^ GetFrameAtIndex( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Zero-based index of the frame to get

#### Return Value

[IPMIFrameData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIFrameData.md)

Remarks

Use [IPMIGtolData::GetFrameCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolData~GetFrameCount.md) to determine Index.

Example

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPMIGtolData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolData.md)  
[IPMIGtolData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolData_members.md)
