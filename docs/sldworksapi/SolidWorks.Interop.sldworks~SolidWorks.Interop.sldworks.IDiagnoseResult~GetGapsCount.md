# GetGapsCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDiagnoseResult~GetGapsCount`

Gets the number of gaps on the body.
Gets the number of gaps on the body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetGapsCount() As System.Integer
```

```

Dim instance As IDiagnoseResult
Dim value As System.Integer
 
value = instance.GetGapsCount()
```

```

System.int GetGapsCount()
```

```

System.int GetGapsCount(); 
```

#### Return Value

Number of gaps

Remarks

Call this method before calling [IDiagnoseResult::GetCoEdgesAtGap](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDiagnoseResult~GetCoEdgesAtGap.md) and [IDiagnoseResult::IGetCoEdgesAtGap](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDiagnoseResult~IGetCoEdgesAtGap.md).

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
