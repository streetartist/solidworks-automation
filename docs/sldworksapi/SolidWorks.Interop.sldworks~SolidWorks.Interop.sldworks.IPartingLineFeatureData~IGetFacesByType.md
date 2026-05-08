# IGetFacesByType Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~IGetFacesByType`

Gets the specified faces after performing a draft analysis of the parting line feature.
Gets the specified faces after performing a draft analysis of the parting line feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetFacesByType( _
   ByVal Type As System.Integer, _
   ByVal Count As System.Integer _
) As Face2
```

```

Dim instance As IPartingLineFeatureData
Dim Type As System.Integer
Dim Count As System.Integer
Dim value As Face2
 
value = instance.IGetFacesByType(Type, Count)
```

```

Face2 IGetFacesByType( 
   System.int Type,
   System.int Count
)
```

```

Face2^ IGetFacesByType( 
   System.int Type,
   System.int Count
) 
```

#### Parameters

*Type*
:   Type of face as defined by [swDraftAnalysisFaceType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDraftAnalysisFaceType_e.html)

*Count*
:   Number of faces

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Call [IPartingLineFeatureData::GetFacesByTypeCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~GetFacesByTypeCount.md) before calling this method.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartingLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData.md)  
[IPartingLineFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData_members.md)  
[IPartingLineFeatureData::GetFacesByType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~GetFacesByType.md)  
[IPartingLineFeatureData::DraftAnalysis Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~DraftAnalysis.md)
