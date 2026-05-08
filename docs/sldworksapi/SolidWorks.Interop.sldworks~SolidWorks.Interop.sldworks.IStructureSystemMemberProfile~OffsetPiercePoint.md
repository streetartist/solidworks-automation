# OffsetPiercePoint Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~OffsetPiercePoint`

Gets and sets whether to offset the pierce point of this member profile.
Gets and sets whether to offset the pierce point of this member profile.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property OffsetPiercePoint As System.Boolean
```

```

Dim instance As IStructureSystemMemberProfile
Dim value As System.Boolean
 
instance.OffsetPiercePoint = value
 
value = instance.OffsetPiercePoint
```

```

System.bool OffsetPiercePoint {get; set;}
```

```

property System.bool OffsetPiercePoint {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to offset the pierce point, false to not

Remarks

If this property is true, use [IStructureSystemMemberProfile::OffsetPiercePointHorizontalAxis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~OffsetPiercePointHorizontalAxis.md) and [IStructureSystemMemberProfile::OffsetPiercePointVerticalAxis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~OffsetPiercePointVerticalAxis.md) to specify the offsets.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IStructureSystemMemberProfile Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile.md)  
[IStructureSystemMemberProfile Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile_members.md)
