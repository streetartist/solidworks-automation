# ProfileAlignmentObject Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~ProfileAlignmentObject`

Gets and sets the entity with which to align an axis of this member profile.
Gets and sets the entity with which to align an axis of this member profile.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ProfileAlignmentObject As System.Object
```

```

Dim instance As IStructureSystemMemberProfile
Dim value As System.Object
 
instance.ProfileAlignmentObject = value
 
value = instance.ProfileAlignmentObject
```

```

System.object ProfileAlignmentObject {get; set;}
```

```

property System.Object^ ProfileAlignmentObject {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Direction entity with which to align an axis of the member profile, e.g.:

- [IBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)
- [IEdge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)
- [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)
- [IRefAxis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.md)
- [IRefPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md)
- [ISketchLine](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine.md)
- [ISketchSegment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md)
- [ISurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)

Remarks

Use:

- [IStructureSystemMemberProfile::ProfileAlignmentObjectType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~ProfileAlignmentObjectType.md) to specify the type of this entity.
- [IStructureSystemMemberProfile::ProfileAlignmentType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~ProfileAlignmentType.md) to specify to which axis of the member profile to align the entity specified by this property.
- [IStructureSystemMemberProfile::ProfileAlignmentAngle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~ProfileAlignmentAngle.md) to specify the angle of alignment with the specified entity and member axis.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IStructureSystemMemberProfile Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile.md)  
[IStructureSystemMemberProfile Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile_members.md)
