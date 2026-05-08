# GetStartAndEndReferences Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData~GetStartAndEndReferences`

Gets the start and end reference entities that are used to define the length of this structure system member.
Gets the start and end reference entities that are used to define the length of this structure system member.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetStartAndEndReferences() As System.Object
```

```

Dim instance As IPrimaryMemberRefPlaneFeatureData
Dim value As System.Object
 
value = instance.GetStartAndEndReferences()
```

```

System.object GetStartAndEndReferences()
```

```

System.Object^ GetStartAndEndReferences(); 
```

#### Return Value

Array of two parallel entities ([IRefPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md)s and/or [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)s)

Remarks

The parallel entities returned by this method must be perpendicular and intersect the reference axes.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPrimaryMemberRefPlaneFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData.md)  
[IPrimaryMemberRefPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData_members.md)
