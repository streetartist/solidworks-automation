# GetEntitiesNeedUserId Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetEntitiesNeedUserId`

Gets a list of faces and edges that need be assigned user IDs for the macro feature.
Gets a list of faces and edges that need be assigned user IDs for the macro feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GetEntitiesNeedUserId( _
   ByVal Body As System.Object, _
   ByRef Faces As System.Object, _
   ByRef Edges As System.Object _
) 
```

```

Dim instance As IMacroFeatureData
Dim Body As System.Object
Dim Faces As System.Object
Dim Edges As System.Object
 
instance.GetEntitiesNeedUserId(Body, Faces, Edges)
```

```

void GetEntitiesNeedUserId( 
   System.object Body,
   out System.object Faces,
   out System.object Edges
)
```

```

void GetEntitiesNeedUserId( 
   System.Object^ Body,
   [Out] System.Object^ Faces,
   [Out] System.Object^ Edges
) 
```

#### Parameters

*Body*
:   [Body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) containing the faces and edges

*Faces*
:   Array of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

*Edges*
:   Array of [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Example

[Cut Body in Half Using Macro Feature (VBA)](Cut_Body_in_Half_using_Macro_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.md)  
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.md)  
[IMacroFeatureData::GetEdgeIdType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetEdgeIdType.md)  
[IMacroFeatureData::GetEdgeUserId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetEdgeUserId.md)  
[IMacroFeatureData::GetEntitiesNeedUserIdCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetEntitiesNeedUserIdCount.md)  
[IMacroFeatureData::GetFaceIdType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetFaceIdType.md)  
[IMacroFeatureData::GetFaceUserId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetFaceUserId.md)  
[IMacroFeatureData::SetEdgeUserId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetEdgeUserId.md)  
[IMacroFeatureData::SetFaceUserId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetFaceUserId.md)
