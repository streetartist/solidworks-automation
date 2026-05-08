# EditReferencePoint Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~EditReferencePoint`

Edits the selected reference points.
Edits the selected reference points.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function EditReferencePoint( _
   ByVal NRefPointType As System.Integer, _
   ByVal NRefPointAlongCurveType As System.Integer, _
   ByVal DDistance_or_Percent As System.Double, _
   ByVal NumberOfRefPoints As System.Integer _
) As System.Boolean
```

```

Dim instance As IFeatureManager
Dim NRefPointType As System.Integer
Dim NRefPointAlongCurveType As System.Integer
Dim DDistance_or_Percent As System.Double
Dim NumberOfRefPoints As System.Integer
Dim value As System.Boolean
 
value = instance.EditReferencePoint(NRefPointType, NRefPointAlongCurveType, DDistance_or_Percent, NumberOfRefPoints)
```

```

System.bool EditReferencePoint( 
   System.int NRefPointType,
   System.int NRefPointAlongCurveType,
   System.double DDistance_or_Percent,
   System.int NumberOfRefPoints
)
```

```

System.bool EditReferencePoint( 
   System.int NRefPointType,
   System.int NRefPointAlongCurveType,
   System.double DDistance_or_Percent,
   System.int NumberOfRefPoints
) 
```

#### Parameters

*NRefPointType*
:   :   Type of reference point as defined by [swRefPointType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRefPointType_e.html)

*NRefPointAlongCurveType*
:   Distance, percentage, or evenly distributed as defined by [swRefPointAlongCurveType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRefPointAlongCurveType_e.html)

*DDistance\_or\_Percent*
:   :   Distance at which to create the reference point on the selected entities or percentage of the length of the selected entities at which to create the reference point if NRefPointAlongCurveType is swRefPointAlongCurveDistance or swRefPointAlongCurvePercentage, respectively

*NumberOfRefPoints*
:   :   Number of reference points to create and evenly distribute on the selected entities if swRefPointAlongCurveType is swRefPointAlongCurveEvenlyDistributed

#### Return Value

True if the operation succeeds, false if not

Remarks

A reference point is a feature. To programatically create a reference point feature, you can use [IFeatureManager::InsertReferencePoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertReferencePoint.md) or [IFeatureManager::IInsertReferencePoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~IInsertReferencePoint.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IRefPointFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPointFeatureData.md)
