# GetFacesToDraftCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~GetFacesToDraftCount`

Gets the number of faces that define the draft feature.
Gets the number of faces that define the draft feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFacesToDraftCount() As System.Short
```

```

Dim instance As IDraftFeatureData2
Dim value As System.Short
 
value = instance.GetFacesToDraftCount()
```

```

System.short GetFacesToDraftCount()
```

```

System.short GetFacesToDraftCount(); 
```

#### Return Value

Number of faces that define the draft feature

Remarks

Call this method before calling [IDraftFeatureData2::IGetFacesToDraft](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~ISetFacesToDraft.md) to determine the size of the array for that method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDraftFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2.md)  
[IDraftFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2_members.md)  
[IDraftFeatureData2::FacesToDraft Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~FacesToDraft.md)  
[IDraftFeatureData2::ISetFacesToDraft Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~ISetFacesToDraft.md)
