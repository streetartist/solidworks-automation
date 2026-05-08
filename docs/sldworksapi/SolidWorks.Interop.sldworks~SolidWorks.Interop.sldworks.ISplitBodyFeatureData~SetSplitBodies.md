# SetSplitBodies Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~SetSplitBodies`

Obsolete. Superseded by ISplitBodyFeatureData::SetSplitBodies2.
Obsolete. Superseded by [ISplitBodyFeatureData::SetSplitBodies2.](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~SetSplitBodies2.md)

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetSplitBodies( _
   ByVal PathVar As System.Object, _
   ByVal FlagVar As System.Object _
) 
```

```

Dim instance As ISplitBodyFeatureData
Dim PathVar As System.Object
Dim FlagVar As System.Object
 
instance.SetSplitBodies(PathVar, FlagVar)
```

```

void SetSplitBodies( 
   System.object PathVar,
   System.object FlagVar
)
```

```

void SetSplitBodies( 
   System.Object^ PathVar,
   System.Object^ FlagVar
) 
```

#### Parameters

*PathVar*
:   Array of full paths and file names of the split bodies

*FlagVar*
:   Array of Booleans indicating whether to include a body in this split-body feature

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISplitBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData.md)  
[ISplitBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData_members.md)  
[ISplitBodyFeatureData::ISetSplitBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~ISetSplitBodies.md)  
[ISplitBodyFeatureData::GetSplitBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~GetSplitBodies.md)  
[ISplitBodyFeatureData::GetSplitBodiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~GetSplitBodiesCount.md)  
[ISplitBodyFeatureData::IGetSplitBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~IGetSplitBodies.md)
