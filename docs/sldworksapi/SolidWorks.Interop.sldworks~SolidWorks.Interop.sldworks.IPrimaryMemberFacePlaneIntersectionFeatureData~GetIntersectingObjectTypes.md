# GetIntersectingObjectTypes Method (IPrimaryMemberFacePlaneIntersectionFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberFacePlaneIntersectionFeatureData~GetIntersectingObjectTypes`

Gets the types of entities that intersect with parameter faces of this structure system member.
Gets the types of entities that intersect with parameter faces of this structure system member.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetIntersectingObjectTypes() As System.Object
```

```

Dim instance As IPrimaryMemberFacePlaneIntersectionFeatureData
Dim value As System.Object
 
value = instance.GetIntersectingObjectTypes()
```

```

System.object GetIntersectingObjectTypes()
```

```

System.Object^ GetIntersectingObjectTypes(); 
```

#### Return Value

Array of intersecting object types as defined by [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSelectType_e.html):

- swSelFACES
- swSelREFFACES
- swSelDATUMPLANES

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPrimaryMemberFacePlaneIntersectionFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberFacePlaneIntersectionFeatureData.md)  
[IPrimaryMemberFacePlaneIntersectionFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberFacePlaneIntersectionFeatureData_members.md)
