# GetFacesByTypeCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~GetFacesByTypeCount`

Gets the number of faces of the specified type for this parting line.
Gets the number of faces of the specified type for this parting line.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFacesByTypeCount( _
   ByVal Type As System.Integer _
) As System.Integer
```

```

Dim instance As IPartingLineFeatureData
Dim Type As System.Integer
Dim value As System.Integer
 
value = instance.GetFacesByTypeCount(Type)
```

```

System.int GetFacesByTypeCount( 
   System.int Type
)
```

```

System.int GetFacesByTypeCount( 
   System.int Type
) 
```

#### Parameters

*Type*
:   Type of faces as defined by [swDraftAnalysisFaceType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDraftAnalysisFaceType_e.html)

#### Return Value

Number of faces

Remarks

Call this method before calling [IPartingLineFeatureData::IGetFacesbyType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~IGetFacesByType.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartingLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData.md)  
[IPartingLineFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData_members.md)  
[IPartingLineFeatureData::GetFacesByType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~GetFacesByType.md)
