# Check Property (IFace2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~Check`

Checks whether the face is a valid, and, if not, returns the faults.
Checks whether the face is a valid, and, if not, returns the faults.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Check As FaultEntity
```

```

Dim instance As IFace2
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

[Check Faces for Faults (VBA)](Check_Faces_for_Faults_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)  
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.md)  
[IEdge::Check Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~Check.md)  
[IBody2::Check3 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Check3.md)
