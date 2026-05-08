# PiercePointSelectionObject Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~PiercePointSelectionObject`

Gets and sets the selected pierce point object for the sketch of this member profile.
Gets and sets the selected pierce point object for the sketch of this member profile.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PiercePointSelectionObject As System.Object
```

```

Dim instance As IStructureSystemMemberProfile
Dim value As System.Object
 
instance.PiercePointSelectionObject = value
 
value = instance.PiercePointSelectionObject
```

```

System.object PiercePointSelectionObject {get; set;}
```

```

property System.Object^ PiercePointSelectionObject {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

[ISketchPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md)

Remarks

This property is valid only if [IStructureSystemMemberProfile::ProfilePiercePointType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile~ProfilePiercePointType.md) is set to [swStructureProfilePiercePointType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swStructureProfilePiercePointType_e.html).Selection.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IStructureSystemMemberProfile Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile.md)  
[IStructureSystemMemberProfile Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberProfile_members.md)
