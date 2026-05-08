# ProfileMirrorType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~ProfileMirrorType`

Gets and sets the axis about which to flip this member profile.
Gets and sets the axis about which to flip this member profile.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ProfileMirrorType As System.Integer
```

```

Dim instance As IStructureSystemMemberProfile
Dim value As System.Integer
 
instance.ProfileMirrorType = value
 
value = instance.ProfileMirrorType
```

```

System.int ProfileMirrorType {get; set;}
```

```

property System.int ProfileMirrorType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Axis about which to flip this member profile as defined by [swStructureProfileMirrorType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swStructureProfileMirrorType_e.html)

Remarks

This property is valid only if [IStructureSystemMemberProfile::MirrorProfile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~MirrorProfile.md) is true.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IStructureSystemMemberProfile Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile.md)  
[IStructureSystemMemberProfile Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile_members.md)
