# GetDraftedEntities Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~GetDraftedEntities`

Gets the drafted entities (faces or edges) for this draft feature.
Gets the drafted entities (faces or edges) for this draft feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDraftedEntities() As System.Object
```

```

Dim instance As IDraftFeatureData2
Dim value As System.Object
 
value = instance.GetDraftedEntities()
```

```

System.object GetDraftedEntities()
```

```

System.Object^ GetDraftedEntities(); 
```

#### Return Value

Array of [entities](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.md)

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Example

[Get Faces Affected by Draft Feature (VBA)](Get_Faces_Affected_by_Draft_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDraftFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2.md)  
[IDraftFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2_members.md)  
[IDraftFeatureData2::IGetDraftedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~IGetDraftedEntities.md)  
[IDraftFeatureData2::GetDraftedEntityCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~GetDraftedEntityCount.md)
