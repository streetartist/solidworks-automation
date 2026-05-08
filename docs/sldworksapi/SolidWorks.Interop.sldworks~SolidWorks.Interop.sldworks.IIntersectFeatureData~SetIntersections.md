# SetIntersections Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData~SetIntersections`

Specifies which of the intersect regions to exclude from this intersect feature.
Specifies which of the intersect regions to exclude from this intersect feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetIntersections( _
   ByVal Intersections As System.Object _
) 
```

```

Dim instance As IIntersectFeatureData
Dim Intersections As System.Object
 
instance.SetIntersections(Intersections)
```

```

void SetIntersections( 
   System.object Intersections
)
```

```

void SetIntersections( 
   System.Object^ Intersections
) 
```

#### Parameters

*Intersections*
:   Array of booleans; true indicates to exclude the corresponding intersect region in the array of intersect regions returned by [IIntersectFeatureData::GetIntersections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData~GetIntersections.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IIntersectFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData.md)  
[IIntersectFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData_members.md)
