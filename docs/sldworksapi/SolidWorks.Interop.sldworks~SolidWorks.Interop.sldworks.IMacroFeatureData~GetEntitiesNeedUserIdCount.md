# GetEntitiesNeedUserIdCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetEntitiesNeedUserIdCount`

Gets the number of faces and edges that need to be assigned user IDs for the macro feature.
Gets the number of faces and edges that need to be assigned user IDs for the macro feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GetEntitiesNeedUserIdCount( _
   ByVal Body As Body2, _
   ByRef FaceCount As System.Integer, _
   ByRef EdgeCount As System.Integer _
) 
```

```

Dim instance As IMacroFeatureData
Dim Body As Body2
Dim FaceCount As System.Integer
Dim EdgeCount As System.Integer
 
instance.GetEntitiesNeedUserIdCount(Body, FaceCount, EdgeCount)
```

```

void GetEntitiesNeedUserIdCount( 
   Body2 Body,
   out System.int FaceCount,
   out System.int EdgeCount
)
```

```

void GetEntitiesNeedUserIdCount( 
   Body2^ Body,
   [Out] System.int FaceCount,
   [Out] System.int EdgeCount
) 
```

#### Parameters

*Body*
:   [Body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

*FaceCount*
:   Number of faces

*EdgeCount*
:   Number of edges

Remarks

Call this method before calling [IMacroFeatureData::IGetEntitiesNeedUserId](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetEntitiesNeedUserId.md) to determine the size of the array for that method.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.md)  
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.md)  
[IMacroFeatureData::GetEntitiesNeedUserId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetEntitiesNeedUserId.md)  
[IMacroFeatureData::GetFaceIdType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetFaceIdType.md)  
[IMacroFeatureData::GetFaceUserId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetFaceUserId.md)  
[IMacroFeatureData::SetEdgeUserId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetEdgeUserId.md)  
[IMacroFeatureData::SetFaceUserId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetFaceUserId.md)
