# GetCoEdgesAtGap Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDiagnoseResult~GetCoEdgesAtGap`

Gets the coedges at the specified gap.
Gets the coedges at the specified gap.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCoEdgesAtGap( _
   ByVal Index As System.Integer _
) As System.Object
```

```

Dim instance As IDiagnoseResult
Dim Index As System.Integer
Dim value As System.Object
 
value = instance.GetCoEdgesAtGap(Index)
```

```

System.object GetCoEdgesAtGap( 
   System.int Index
)
```

```

System.Object^ GetCoEdgesAtGap( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Index number of the gap to get

#### Return Value

Array of [coedges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge.md)

Remarks

Call [IDiagnoseResult::GetGapsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDiagnoseResult~GetGapsCount.md) before calling this method to determine the index number of the gap to get on this body.

Example

[Get and Fill Gaps in Body (C#)](Get_and_Fill_Gaps_in_Body_Example_CSharp.htm)  
[Get and Fill Gaps in Body (VB.NET)](Get_and_Fill_Gaps_in_Body_Example_VBNET.htm)  
[Get and Fill Gaps in Body (VBA)](Get_and_Fill_Gaps_in_Body_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDiagnoseResult Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDiagnoseResult.md)  
[IDiagnoseResult Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDiagnoseResult_members.md)  
[IDiagnoseResult::GetCoEdgesCountAtGap Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDiagnoseResult~GetCoEdgesCountAtGap.md)  
[IDiagnoseResult::IGetCoEdgesAtGap Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDiagnoseResult~IGetCoEdgesAtGap.md)
