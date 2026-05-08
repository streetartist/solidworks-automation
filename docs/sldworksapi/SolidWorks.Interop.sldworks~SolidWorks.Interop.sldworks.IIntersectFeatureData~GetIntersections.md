# GetIntersections Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData~GetIntersections`

Gets the intersect regions in this intersect feature.
Gets the intersect regions in this intersect feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetIntersections( _
   ByRef Excluded As System.Object _
) As System.Object
```

```

Dim instance As IIntersectFeatureData
Dim Excluded As System.Object
Dim value As System.Object
 
value = instance.GetIntersections(Excluded)
```

```

System.object GetIntersections( 
   out System.object Excluded
)
```

```

System.Object^ GetIntersections( 
   [Out] System.Object^ Excluded
) 
```

#### Parameters

*Excluded*
:   Array of booleans; true indicates that the corresponding intersect region in the array of returned intersect regions is excluded from this intersect feature

#### Return Value

Array of [intersect regions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IIntersectFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData.md)  
[IIntersectFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData_members.md)  
[IIntersectFeatureData::SetIntersections Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData~SetIntersections.md)  
[IIntersectFeatureData::GetIntersectionsCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData~GetIntersectionsCount.md)
