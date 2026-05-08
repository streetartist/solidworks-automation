# LocateProfilePoint Property (IStructuralMemberGroup)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup~LocateProfilePoint`

Gets and sets the point to use to locate the profile for this structural-member group.
Gets and sets the point to use to locate the profile for this structural-member group.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property LocateProfilePoint As SketchPoint
```

```

Dim instance As IStructuralMemberGroup
Dim value As SketchPoint
 
instance.LocateProfilePoint = value
 
value = instance.LocateProfilePoint
```

```

SketchPoint LocateProfilePoint {get; set;}
```

```

property SketchPoint^ LocateProfilePoint {
   SketchPoint^ get();
   void set (    SketchPoint^ value);
}
```

#### Property Value

[Point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md) to use to locate the profile

Remarks

This property can be set only after creating the structural-member group.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IStructuralMemberGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup.md)  
[IStructuralMemberGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup_members.md)
