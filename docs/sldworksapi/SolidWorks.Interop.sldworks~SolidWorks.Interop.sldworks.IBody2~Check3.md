# Check3 Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Check3`

Gets whether the body is a valid and returns an IFaultEntity object if any faults exist.
Gets whether the body is a valid and returns an [IFaultEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaultEntity.md) object if any faults exist.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Check3 As FaultEntity
```

```

Dim instance As IBody2
Dim value As FaultEntity
 
value = instance.Check3
```

```

FaultEntity Check3 {get;}
```

```

property FaultEntity^ Check3 {
   FaultEntity^ get();
}
```

#### Property Value

Pointer to [IFaultEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaultEntity.md) object

Example

[Check Bodies for Faults (VBA)](Check_Bodies_for_Faults_Example_VB.htm)  
[Get and Fill Gaps in Body (C#)](Get_and_Fill_Gaps_in_Body_Example_CSharp.htm)  
[Get and Fill Gaps in Body (VB.NET)](Get_and_Fill_Gaps_in_Body_Example_VBNET.htm)  
[Get and Fill Gaps in Body (VBA)](Get_and_Fill_Gaps_in_Body_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IEdge::Check Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~Check.md)  
[IFace2::Check Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~Check.md)
