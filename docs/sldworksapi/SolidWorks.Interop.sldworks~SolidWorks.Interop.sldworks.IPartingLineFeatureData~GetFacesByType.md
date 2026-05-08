# GetFacesByType Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~GetFacesByType`

Gets the specified faces after performing a draft analysis of the parting line feature.
Gets the specified faces after performing a draft analysis of the parting line feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFacesByType( _
   ByVal Type As System.Integer _
) As System.Object
```

```

Dim instance As IPartingLineFeatureData
Dim Type As System.Integer
Dim value As System.Object
 
value = instance.GetFacesByType(Type)
```

```

System.object GetFacesByType( 
   System.int Type
)
```

```

System.Object^ GetFacesByType( 
   System.int Type
) 
```

#### Parameters

*Type*
:   Type of face as defined by [swDraftAnalysisFaceType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDraftAnalysisFaceType_e.html)

#### Return Value

Array of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartingLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData.md)  
[IPartingLineFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData_members.md)  
[IPartingLineFeatureData::IGetFacesByType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~IGetFacesByType.md)  
[IPartingLineFeatureData::GetFacesByTypeCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~GetFacesByTypeCount.md)  
[IPartingLineFeatureData::DraftAnalysis Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~DraftAnalysis.md)
