# IGetEntitiesNeedUserId Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetEntitiesNeedUserId`

Gets a list of faces and edges that need be assigned user IDs for the macro feature.
Gets a list of faces and edges that need be assigned user IDs for the macro feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub IGetEntitiesNeedUserId( _
   ByVal Body As Body2, _
   ByVal FaceCount As System.Integer, _
   ByRef Faces As Face2, _
   ByVal EdgeCount As System.Integer, _
   ByRef Edges As Edge _
) 
```

```

Dim instance As IMacroFeatureData
Dim Body As Body2
Dim FaceCount As System.Integer
Dim Faces As Face2
Dim EdgeCount As System.Integer
Dim Edges As Edge
 
instance.IGetEntitiesNeedUserId(Body, FaceCount, Faces, EdgeCount, Edges)
```

```

void IGetEntitiesNeedUserId( 
   Body2 Body,
   System.int FaceCount,
   out Face2 Faces,
   System.int EdgeCount,
   out Edge Edges
)
```

```

void IGetEntitiesNeedUserId( 
   Body2^ Body,
   System.int FaceCount,
   [Out] Face2^ Faces,
   System.int EdgeCount,
   [Out] Edge^ Edges
) 
```

#### Parameters

*Body*
:   [Body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) containing the faces and edges

*FaceCount*
:   Number of faces

*Faces*
:   - in-process, unmanaged C++: Pointer to an array of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

*EdgeCount*
:   Number of edges

*Edges*
:   - in-process, unmanaged C++: Pointer to an array of [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [IMacroFeatureData::GetEntitiesNeedUserIdCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetEntitiesNeedUserIdCount.md) to determine the size of the arrays.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.md)  
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.md)  
[IMacroFeatureData::GetEdgeIdType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetEdgeIdType.md)  
[IMacroFeatureData::GetEdgeUserId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetEdgeUserId.md)  
[IMacroFeatureData::GetEntitiesNeedUserId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetEntitiesNeedUserId.md)  
[IMacroFeatureData::GetFaceIdType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetFaceIdType.md)  
[IMacroFeatureData::GetFaceUserId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetFaceUserId.md)  
[IMacroFeatureData::SetEdgeUserId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetEdgeUserId.md)  
[IMacroFeatureData::SetFaceUserId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetFaceUserId.md)
