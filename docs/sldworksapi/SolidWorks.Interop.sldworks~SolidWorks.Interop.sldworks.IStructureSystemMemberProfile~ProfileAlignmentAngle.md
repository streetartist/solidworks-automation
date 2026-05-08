# ProfileAlignmentAngle Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~ProfileAlignmentAngle`

Gets and sets the angle of alignment between this member profile and a specified entity.
Gets and sets the angle of alignment between this member profile and a specified entity.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ProfileAlignmentAngle As System.Double
```

```

Dim instance As IStructureSystemMemberProfile
Dim value As System.Double
 
instance.ProfileAlignmentAngle = value
 
value = instance.ProfileAlignmentAngle
```

```

System.double ProfileAlignmentAngle {get; set;}
```

```

property System.double ProfileAlignmentAngle {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Alignment angle in radians

Remarks

The angle is measured between an axis of the profile member as defined by [IStructureSystemMemberProfile::ProfileAlignmentType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~ProfileAlignmentType.md) and an entity specified by [IStructureSystemMemberProfile::ProfileAlignmentObject](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~ProfileAlignmentObject.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IStructureSystemMemberProfile Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile.md)  
[IStructureSystemMemberProfile Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile_members.md)
