# GetPathSegmentsTypes Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPathSegmentFeatureData~GetPathSegmentsTypes`

Gets the types of path segments used to create the structure system member.
Gets the types of path segments used to create the structure system member.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetPathSegmentsTypes() As System.Object
```

```

Dim instance As IPrimaryMemberPathSegmentFeatureData
Dim value As System.Object
 
value = instance.GetPathSegmentsTypes()
```

```

System.object GetPathSegmentsTypes()
```

```

System.Object^ GetPathSegmentsTypes(); 
```

#### Return Value

Array of path segment types as defined by [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSelectType_e.html):

- swSelSKETCHES
- swSelEDGES
- swSelREFCURVES

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPrimaryMemberPathSegmentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPathSegmentFeatureData.md)  
[IPrimaryMemberPathSegmentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPathSegmentFeatureData_members.md)
