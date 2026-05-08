# SetEdgeUserId Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetEdgeUserId`

Sets the user-defined IDs for the specified edge for the macro feature.
Sets the user-defined IDs for the specified edge for the macro feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetEdgeUserId( _
   ByVal Edge As Edge, _
   ByVal Id1 As System.Integer, _
   ByVal Id2 As System.Integer _
) As System.Boolean
```

```

Dim instance As IMacroFeatureData
Dim Edge As Edge
Dim Id1 As System.Integer
Dim Id2 As System.Integer
Dim value As System.Boolean
 
value = instance.SetEdgeUserId(Edge, Id1, Id2)
```

```

System.bool SetEdgeUserId( 
   Edge Edge,
   System.int Id1,
   System.int Id2
)
```

```

System.bool SetEdgeUserId( 
   Edge^ Edge,
   System.int Id1,
   System.int Id2
) 
```

#### Parameters

*Edge*
:   [Edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)

*Id1*
:   First ID

*Id2*
:   Second ID

#### Return Value

True if the IDs are valid, false if not

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Example

[Cut Body in Half Using Macro Feature (VBA)](Cut_Body_in_Half_using_Macro_Feature_Example_VB.htm)  
[Create Multibody Macro Feature (VBA)](Create_Multibody_Macro_Feature_Example_VB.htm)  
[Create Multibody Macro Feature (VB.NET)](Create_Multibody_Macro_Feature_Example_VBNET.htm)  
[Create Multibody Macro Feature (C#)](Create_Multibody_Macro_Feature_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.md)  
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.md)  
[IMacroFeatureData::GetEdgeIdType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetEdgeIdType.md)  
[IMacroFeatureData::GetEdgeUserId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetEdgeUserId.md)  
[IMacroFeatureData::GetEntitiesNeedUserId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetEntitiesNeedUserId.md)  
[IMacroFeatureData::GetEntitiesNeedUserIdCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetEntitiesNeedUserIdCount.md)  
[IMacroFeatureData::GetFaceIdType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetFaceIdType.md)  
[IMacroFeatureData::GetFaceUserId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetFaceUserId.md)  
[IMacroFeatureData::IGetEntitiesNeedUserId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetEntitiesNeedUserId.md)  
[IMacroFeatureData::SetFaceUserId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetFaceUserId.md)
