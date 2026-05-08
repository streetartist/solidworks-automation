# ProfileAlignmentType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~ProfileAlignmentType`

Gets and sets the axis of alignment for this member profile.
Gets and sets the axis of alignment for this member profile.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ProfileAlignmentType As System.Integer
```

```

Dim instance As IStructureSystemMemberProfile
Dim value As System.Integer
 
instance.ProfileAlignmentType = value
 
value = instance.ProfileAlignmentType
```

```

System.int ProfileAlignmentType {get; set;}
```

```

property System.int ProfileAlignmentType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Profile alignment type as defined by [swStructureProfileAlignmentType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swStructureProfileAlignmentType_e.html)

Remarks

This property is valid only if [IStructureSystemMemberProfile::ProfileAlignmentObject](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~ProfileAlignmentObject.md) is set.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IStructureSystemMemberProfile Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile.md)  
[IStructureSystemMemberProfile Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile_members.md)
