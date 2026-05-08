# SetSplitBodies2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~SetSplitBodies2`

Edits the current split bodies in this Split feature.
Edits the current split bodies in this Split feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetSplitBodies2( _
   ByVal PathVar As System.Object, _
   ByVal FlagVar As System.Object, _
   ByVal BodyOrigin As System.Object _
) 
```

```

Dim instance As ISplitBodyFeatureData
Dim PathVar As System.Object
Dim FlagVar As System.Object
Dim BodyOrigin As System.Object
 
instance.SetSplitBodies2(PathVar, FlagVar, BodyOrigin)
```

```

void SetSplitBodies2( 
   System.object PathVar,
   System.object FlagVar,
   System.object BodyOrigin
)
```

```

void SetSplitBodies2( 
   System.Object^ PathVar,
   System.Object^ FlagVar,
   System.Object^ BodyOrigin
) 
```

#### Parameters

*PathVar*
:   Array of paths and file names of the part documents to which to save the split bodies in this Split feature

*FlagVar*
:   Array of booleans indicating whether to consume each corresponding PathVar body; true to remove it from the original part, false to not

*BodyOrigin*
:   Array of sketch points, vertices, or reference points indicating the origins of each PathVar body; null elements are also permitted

Remarks

Call this method after calling [ISplitBodyFeatureData::GetSplitBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~GetSplitBodies.md) or [ISplitBodyFeatureData::IGetSplitBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~IGetSplitBodies.md) to change which split bodies to include in this Split feature.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISplitBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData.md)  
[ISplitBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData_members.md)  
[IFeatureManager::PreSplitBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PreSplitBody2.md)  
[IFeatureManager::PostSplitBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PostSplitBody.md)
