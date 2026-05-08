# AlignmentVector Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup~AlignmentVector`

Gets and sets a reference vector for this structural-member group.
Gets and sets a reference vector for this structural-member group.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property AlignmentVector As System.Object
```

```

Dim instance As IStructuralMemberGroup
Dim value As System.Object
 
instance.AlignmentVector = value
 
value = instance.AlignmentVector
```

```

System.object AlignmentVector {get; set;}
```

```

property System.Object^ AlignmentVector {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Object in the model that provides location and direction in aligning this structural-member group

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IStructuralMemberGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup.md)  
[IStructuralMemberGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup_members.md)
