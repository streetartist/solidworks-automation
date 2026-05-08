# PrimaryMemberType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryStructuralMemberFeatureData~PrimaryMemberType`

Gets the type of this primary structure system member.
Gets the type of this primary structure system member.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property PrimaryMemberType As System.Integer
```

```

Dim instance As IPrimaryStructuralMemberFeatureData
Dim value As System.Integer
 
value = instance.PrimaryMemberType
```

```

System.int PrimaryMemberType {get;}
```

```

property System.int PrimaryMemberType {
   System.int get();
}
```

#### Property Value

Primary structure system member type as defined by [swStructureSystemMemberCreationType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swStructureSystemMemberCreationType_e.html)

Example

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.md) examples.

See the [IPrimaryMemberFacePlaneIntersectionFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberFacePlaneIntersectionFeatureData.md) examples.

See the [IPrimaryMemberPointLengthFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPrimaryStructuralMemberFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryStructuralMemberFeatureData.md)  
[IPrimaryStructuralMemberFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryStructuralMemberFeatureData_members.md)
