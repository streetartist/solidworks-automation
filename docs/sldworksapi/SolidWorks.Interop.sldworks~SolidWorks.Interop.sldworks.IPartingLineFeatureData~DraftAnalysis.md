# DraftAnalysis Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~DraftAnalysis`

Performs draft analysis for the input angle and the direction of pull.
Performs draft analysis for the input angle and the direction of pull.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function DraftAnalysis( _
   ByVal Angle As System.Double _
) As System.Boolean
```

```

Dim instance As IPartingLineFeatureData
Dim Angle As System.Double
Dim value As System.Boolean
 
value = instance.DraftAnalysis(Angle)
```

```

System.bool DraftAnalysis( 
   System.double Angle
)
```

```

System.bool DraftAnalysis( 
   System.double Angle
) 
```

#### Parameters

*Angle*
:   Draft angle

#### Return Value

True if draft analysis is performed, false if not

Remarks

If you want a different pull direction, then use [IPartingLineFeatureData::PullDirectionBase](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~PullDirectionBase.md) to change the direction. Once this method is called, only the information for different faces (negative, positive, and so on) is generated.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartingLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData.md)  
[IPartingLineFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData_members.md)  
[IPartingLineFeatureData::Angle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~Angle.md)  
[IPartingLineFeatureData::GetFacesByType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~GetFacesByType.md)  
[IPartingLineFeatureData::IGetFacesByType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~IGetFacesByType.md)  
[IPartingLineFeatureData::GetFacesByTypeCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~GetFacesByTypeCount.md)  
[IPartingLineFeatureData::PullDirectionType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~PullDirectionType.md)  
[IPartingLineFeatureData::PullDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~PullDirection.md)  
[IPartingLineFeatureData::PullDirectionType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData~PullDirectionType.md)
