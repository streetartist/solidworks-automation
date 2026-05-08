# Check Property (IEdge)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~Check`

Gets whether the edge is a valid, and, if not, returns the faults.
Gets whether the edge is a valid, and, if not, returns the faults.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Check As FaultEntity
```

```

Dim instance As IEdge
Dim value As FaultEntity
 
value = instance.Check
```

```

FaultEntity Check {get;}
```

```

property FaultEntity^ Check {
   FaultEntity^ get();
}
```

#### Property Value

Pointer to [IFaultEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaultEntity.md) object

Example

[Check Edges for Faults (C#)](Check_Edges_for_Faults_Example_CSharp.htm)  
[Check Edges for Faults (VB.NET)](Check_Edges_for_Faults_Example_VBNET.htm)  
[Check Edges for Faults (VBA)](Check_Edges_for_Faults_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)  
[IEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.md)  
[IFace2::Check Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~Check.md)  
[IBody2::Check3 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Check3.md)
