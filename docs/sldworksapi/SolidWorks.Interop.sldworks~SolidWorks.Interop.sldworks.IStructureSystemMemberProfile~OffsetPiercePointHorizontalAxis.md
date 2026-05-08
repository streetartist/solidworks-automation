# OffsetPiercePointHorizontalAxis Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~OffsetPiercePointHorizontalAxis`

Gets and sets the offset value of the pierce point in the horizontal direction.
Gets and sets the offset value of the pierce point in the horizontal direction.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property OffsetPiercePointHorizontalAxis As System.Double
```

```

Dim instance As IStructureSystemMemberProfile
Dim value As System.Double
 
instance.OffsetPiercePointHorizontalAxis = value
 
value = instance.OffsetPiercePointHorizontalAxis
```

```

System.double OffsetPiercePointHorizontalAxis {get; set;}
```

```

property System.double OffsetPiercePointHorizontalAxis {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Horizontal offset of the pierce point

Remarks

This property is valid only if [IStructureSystemMemberProfile::OffsetPiercePoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~OffsetPiercePoint.md) is set to true.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IStructureSystemMemberProfile Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile.md)  
[IStructureSystemMemberProfile Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile_members.md)
