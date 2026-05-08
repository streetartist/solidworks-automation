# GetDraftedEntityCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~GetDraftedEntityCount`

Gets the number of drafted entities for this draft feature.
Gets the number of drafted entities for this draft feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDraftedEntityCount() As System.Short
```

```

Dim instance As IDraftFeatureData2
Dim value As System.Short
 
value = instance.GetDraftedEntityCount()
```

```

System.short GetDraftedEntityCount()
```

```

System.short GetDraftedEntityCount(); 
```

#### Return Value

Number of drafted entities

Remarks

Call this method before calling [IDraftFeatureData2::IGetDraftedEntities](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~IGetDraftedEntities.md) to determine the size of the array for that method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDraftFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2.md)  
[IDraftFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2_members.md)  
[IDraftFeatureData2::GetDraftedEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~GetDraftedEntities.md)
