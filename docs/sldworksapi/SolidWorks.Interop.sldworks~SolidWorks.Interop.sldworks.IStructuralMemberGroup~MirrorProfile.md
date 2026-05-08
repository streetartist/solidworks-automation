# MirrorProfile Property (IStructuralMemberGroup)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup~MirrorProfile`

Gets and sets whether to mirror the profile of this structural-member group.
Gets and sets whether to mirror the profile of this structural-member group.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property MirrorProfile As System.Boolean
```

```

Dim instance As IStructuralMemberGroup
Dim value As System.Boolean
 
instance.MirrorProfile = value
 
value = instance.MirrorProfile
```

```

System.bool MirrorProfile {get; set;}
```

```

property System.bool MirrorProfile {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to mirror the profile, false to not

Example

[Insert Structural Weldment (C#)](Insert_Structural_Weldment_Example_CSharp.htm)  
[Insert Structural Weldment (VB.NET)](Insert_Structural_Weldment_Example_VBNET.htm)  
[Insert Structural Weldment (VBA)](Insert_Structural_Weldment_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IStructuralMemberGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup.md)  
[IStructuralMemberGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup_members.md)  
[IStructuralMemberGroup::MirrorProfileAxis Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup~MirrorProfileAxis.md)
