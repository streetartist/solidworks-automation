# Diagnose Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Diagnose`

Gets the IDiagnoseResult object for this body.
Gets the [IDiagnoseResult](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDiagnoseResult.md) object for this body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Diagnose() As DiagnoseResult
```

```

Dim instance As IBody2
Dim value As DiagnoseResult
 
value = instance.Diagnose()
```

```

DiagnoseResult Diagnose()
```

```

DiagnoseResult^ Diagnose(); 
```

#### Return Value

Pointer to the [IDiagnoseResult](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDiagnoseResult.md) object

Remarks

Use the [IDiagnoseResult](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDiagnoseResult.md) object to get the gaps and coedges in each gap on this body.

Example

[Get and Fill Gaps in Body (C#)](Get_and_Fill_Gaps_in_Body_Example_CSharp.htm)  
[Get and Fill Gaps in Body (VB.NET)](Get_and_Fill_Gaps_in_Body_Example_VBNET.htm)  
[Get and Fill Gaps in Body (VBA)](Get_and_Fill_Gaps_in_Body_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)
