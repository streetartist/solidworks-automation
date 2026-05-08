# WeldmentProfilePath Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~WeldmentProfilePath`

Gets or sets the path for the profile for this structural member.
Gets or sets the path for the profile for this structural member.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property WeldmentProfilePath As System.String
```

```

Dim instance As IStructuralMemberFeatureData
Dim value As System.String
 
instance.WeldmentProfilePath = value
 
value = instance.WeldmentProfilePath
```

```

System.string WeldmentProfilePath {get; set;}
```

```

property System.String^ WeldmentProfilePath {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Full path and filename for the profile (see Remarks)

Remarks

Weldment profiles are located in *install\_dir*/lang/*lang*/weldment profiles subfolders and are named filename.sldflp.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IStructuralMemberFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData.md)  
[IStructuralMemberFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData_members.md)  
[IStructuralMemberFeatureData::LocateProfilePoint Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData~LocateProfilePoint.md)
