# MirrorProfile Property (IStructureSystemMemberProfile)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~MirrorProfile`

Gets and sets whether to flip the profile of this member about an axis.
Gets and sets whether to flip the profile of this member about an axis.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property MirrorProfile As System.Boolean
```

```

Dim instance As IStructureSystemMemberProfile
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

True to flip the profile of the member about an axis, false to not

Remarks

Use [IStructureSystemMemberProfile::ProfileMirrorType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~ProfileMirrorType.md) to specify either the horizontal or vertical axis about which to flip the member profile.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IStructureSystemMemberProfile Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile.md)  
[IStructureSystemMemberProfile Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile_members.md)
