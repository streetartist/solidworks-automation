# IGetDraftedEntities Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~IGetDraftedEntities`

Gets the drafted entities (faces or edges) for this draft feature.
Gets the drafted entities (faces or edges) for this draft feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetDraftedEntities( _
   ByVal Count As System.Short _
) As Entity
```

```

Dim instance As IDraftFeatureData2
Dim Count As System.Short
Dim value As Entity
 
value = instance.IGetDraftedEntities(Count)
```

```

Entity IGetDraftedEntities( 
   System.short Count
)
```

```

Entity^ IGetDraftedEntities( 
   System.short Count
) 
```

#### Parameters

*Count*
:   Number of entities

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [entities](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.md) of size Count

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Call [IDraftFeatureData2::GetDraftedEntityCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~GetDraftedEntityCount.md) to determine the size of the array.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDraftFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2.md)  
[IDraftFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2_members.md)  
[IDraftFeatureData2::GetDraftedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~GetDraftedEntities.md)
