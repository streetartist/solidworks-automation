# ProfilePiercePointType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~ProfilePiercePointType`

Gets and sets the type of pierce point used to define the sketch of this structure system member profile.
Gets and sets the type of pierce point used to define the sketch of this structure system member profile.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ProfilePiercePointType As System.Integer
```

```

Dim instance As IStructureSystemMemberProfile
Dim value As System.Integer
 
instance.ProfilePiercePointType = value
 
value = instance.ProfilePiercePointType
```

```

System.int ProfilePiercePointType {get; set;}
```

```

property System.int ProfilePiercePointType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Type of pierce point as defined by [swStructureProfilePiercePointType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swStructureProfilePiercePointType_e.html)

Remarks

Gets and sets the type of pierce point for the sketch of this member profile.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IStructureSystemMemberProfile Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile.md)  
[IStructureSystemMemberProfile Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile_members.md)
