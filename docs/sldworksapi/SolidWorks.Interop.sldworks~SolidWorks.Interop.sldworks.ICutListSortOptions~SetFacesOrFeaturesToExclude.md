# SetFacesOrFeaturesToExclude Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICutListSortOptions~SetFacesOrFeaturesToExclude`

Sets the faces or features to exclude from cut list sorting.
Sets the faces or features to exclude from cut list sorting.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetFacesOrFeaturesToExclude( _
   ByVal Entities As System.Object _
) As System.Integer
```

```

Dim instance As ICutListSortOptions
Dim Entities As System.Object
Dim value As System.Integer
 
value = instance.SetFacesOrFeaturesToExclude(Entities)
```

```

System.int SetFacesOrFeaturesToExclude( 
   System.object Entities
)
```

```

System.int SetFacesOrFeaturesToExclude( 
   System.Object^ Entities
) 
```

#### Parameters

*Entities*
:   Array of [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) or [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) to exclude

#### Return Value

Error code as defined in [swCutListExclusionStatus\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCutListExclusionStatus_e.html)

Remarks

In order to avoid cut list sorting issues using [IBodyFolder::SortCutList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~SortCutList.md), the Entities array must contain entities of selection type BODYFEATURE or FACE.

Faces and features you cannot exclude:

- Chamfers that remove an entire face.
- Suppressed features.
- Features that create new bodies from sketches, such as boss-extrude, revolve, and sweep.
- Certain sheet metal features.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICutListSortOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICutListSortOptions.md)  
[ICutListSortOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICutListSortOptions_members.md)  
[ICutListSortOptions::GetFacesOrFeaturesToExclude Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICutListSortOptions~GetFacesOrFeaturesToExclude.md)
