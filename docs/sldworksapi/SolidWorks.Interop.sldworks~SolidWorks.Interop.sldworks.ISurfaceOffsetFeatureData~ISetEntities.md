# ISetEntities Method (ISurfaceOffsetFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData~ISetEntities`

Sets the offset surfaces or faces for this surface offset feature.
Sets the offset surfaces or faces for this surface offset feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetEntities( _
   ByVal Count As System.Integer, _
   ByRef EntityArray As System.Object _
) 
```

```

Dim instance As ISurfaceOffsetFeatureData
Dim Count As System.Integer
Dim EntityArray As System.Object
 
instance.ISetEntities(Count, EntityArray)
```

```

void ISetEntities( 
   System.int Count,
   ref System.object EntityArray
)
```

```

void ISetEntities( 
   System.int Count,
   System.Object^% EntityArray
) 
```

#### Parameters

*Count*
:   Number of offset surfaces or faces

*EntityArray*
:   - in-process, unmanaged C++: Pointer to an array of offset surface or face feature [entities](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.md) of size Count

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurfaceOffsetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData.md)  
[ISurfaceOffsetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData_members.md)  
[ISurfaceOffsetFeatureData::Entities Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData~Entities.md)  
[ISurfaceOffsetFeatureData::IGetEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData~IGetEntities.md)  
[ISurfaceOffsetFeatureData::GetEntitiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData~GetEntitiesCount.md)
