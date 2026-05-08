# GetSplitBodies Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~GetSplitBodies`

Gets the split bodies in this Split feature.
Gets the split bodies in this Split feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GetSplitBodies( _
   ByRef BodyVar As System.Object, _
   ByRef PathVar As System.Object, _
   ByRef FlagVar As System.Object _
) 
```

```

Dim instance As ISplitBodyFeatureData
Dim BodyVar As System.Object
Dim PathVar As System.Object
Dim FlagVar As System.Object
 
instance.GetSplitBodies(BodyVar, PathVar, FlagVar)
```

```

void GetSplitBodies( 
   out System.object BodyVar,
   out System.object PathVar,
   out System.object FlagVar
)
```

```

void GetSplitBodies( 
   [Out] System.Object^ BodyVar,
   [Out] System.Object^ PathVar,
   [Out] System.Object^ FlagVar
) 
```

#### Parameters

*BodyVar*
:   Array of split [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

*PathVar*
:   Array of paths and file names of the part documents to which BodyVar bodies are saved; empty string if not saved

*FlagVar*
:   Array of booleans indicating whether corresponding BodyVar bodies are consumed; true if removed from the original part, false if not

Remarks

Call this method before calling [ISplitBodyFeatureData::SetSplitBodies2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~SetSplitBodies2.md) to change which split bodies to include in this Split feature.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISplitBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData.md)  
[ISplitBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData_members.md)  
[ISplitBodyFeatureData::IGetSplitBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~IGetSplitBodies.md)  
[ISplitBodyFeatureData::GetSplitBodiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~GetSplitBodiesCount.md)  
[IFeatureManager::PostSplitBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PostSplitBody.md)  
[IFeatureManager::PreSplitBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PreSplitBody.md)
