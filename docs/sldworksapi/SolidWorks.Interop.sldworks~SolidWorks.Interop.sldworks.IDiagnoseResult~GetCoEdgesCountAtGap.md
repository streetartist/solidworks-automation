# GetCoEdgesCountAtGap Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDiagnoseResult~GetCoEdgesCountAtGap`

Gets the number of coedges at the specified gap.
Gets the number of coedges at the specified gap.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCoEdgesCountAtGap( _
   ByVal Index As System.Integer _
) As System.Integer
```

```

Dim instance As IDiagnoseResult
Dim Index As System.Integer
Dim value As System.Integer
 
value = instance.GetCoEdgesCountAtGap(Index)
```

```

System.int GetCoEdgesCountAtGap( 
   System.int Index
)
```

```

System.int GetCoEdgesCountAtGap( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Index number of the gap to get

#### Return Value

Number of coedges at that gap

Example

Call this method before calling [IDiagnoseResult::IGetCoEdgesAtGap](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDiagnoseResult~IGetCoEdgesAtGap.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDiagnoseResult Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDiagnoseResult.md)  
[IDiagnoseResult Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDiagnoseResult_members.md)
