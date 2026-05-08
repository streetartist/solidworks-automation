# GetStructureSystemMembers Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileGroupFolder~GetStructureSystemMembers`

Gets the structure system members in this profile group folder.
Gets the structure system members in this profile group folder.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetStructureSystemMembers() As System.Object
```

```

Dim instance As IProfileGroupFolder
Dim value As System.Object
 
value = instance.GetStructureSystemMembers()
```

```

System.object GetStructureSystemMembers()
```

```

System.Object^ GetStructureSystemMembers(); 
```

#### Return Value

Array of [IStructureSystemMemberFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberFeatureData.md)s

Example

See the [IPrimaryMemberFacePlaneIntersectionFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberFacePlaneIntersectionFeatureData.md) examples.

See the [IPrimaryMemberPointLengthFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IProfileGroupFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileGroupFolder.md)  
[IProfileGroupFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileGroupFolder_members.md)
