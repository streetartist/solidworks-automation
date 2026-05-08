# ISetFacesToDraft Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~ISetFacesToDraft`

Sets the faces to which to apply the draft feature.
Sets the faces to which to apply the draft feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetFacesToDraft( _
   ByVal Count As System.Short, _
   ByRef FaceArray As Face2 _
) 
```

```

Dim instance As IDraftFeatureData2
Dim Count As System.Short
Dim FaceArray As Face2
 
instance.ISetFacesToDraft(Count, FaceArray)
```

```

void ISetFacesToDraft( 
   System.short Count,
   ref Face2 FaceArray
)
```

```

void ISetFacesToDraft( 
   System.short Count,
   Face2^% FaceArray
) 
```

#### Parameters

*Count*
:   Number of faces

*FaceArray*
:   - in-process, unmanaged C++: Pointer to an array of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) of size Count

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDraftFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2.md)  
[IDraftFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2_members.md)  
[IDraftFeatureData2::GetFacesToDraftCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~GetFacesToDraftCount.md)  
[IDraftFeatureData2::IGetFacesToDraft Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~IGetFacesToDraft.md)  
[IDraftFeatureData2::FacesToDraft Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2~FacesToDraft.md)
