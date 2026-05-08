# LocateProfilePoint Property (IStructuralMemberFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~LocateProfilePoint`

Gets or sets the point to use to locate the profile for this structural member.
Gets or sets the point to use to locate the profile for this structural member.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property LocateProfilePoint As SketchPoint
```

```

Dim instance As IStructuralMemberFeatureData
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

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IStructuralMemberFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData.md)  
[IStructuralMemberFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData_members.md)  
[IStructuralMemberFeatureData::WeldmentProfilePath Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~WeldmentProfilePath.md)
