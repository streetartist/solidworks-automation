# InsertReferencePoint Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertReferencePoint`

Creates the geometry for the reference points based on any of these selected entities: edges, faces, planes, vertices, or sketch geometry.
Creates the geometry for the reference points based on any of these selected entities: edges, faces, planes, vertices, or sketch geometry.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertReferencePoint( _
   ByVal NRefPointType As System.Integer, _
   ByVal NRefPointAlongCurveType As System.Integer, _
   ByVal DDistance_or_Percent As System.Double, _
   ByVal NumberOfRefPoints As System.Integer _
) As System.Object
```

```

Dim instance As IFeatureManager
Dim NRefPointType As System.Integer
Dim NRefPointAlongCurveType As System.Integer
Dim DDistance_or_Percent As System.Double
Dim NumberOfRefPoints As System.Integer
Dim value As System.Object
 
value = instance.InsertReferencePoint(NRefPointType, NRefPointAlongCurveType, DDistance_or_Percent, NumberOfRefPoints)
```

```

System.object InsertReferencePoint( 
   System.int NRefPointType,
   System.int NRefPointAlongCurveType,
   System.double DDistance_or_Percent,
   System.int NumberOfRefPoints
)
```

```

System.Object^ InsertReferencePoint( 
   System.int NRefPointType,
   System.int NRefPointAlongCurveType,
   System.double DDistance_or_Percent,
   System.int NumberOfRefPoints
) 
```

#### Parameters

*NRefPointType*
:   Type of reference point as defined by [swRefPointType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRefPointType_e.html)

*NRefPointAlongCurveType*
:   Distance, percentage, or evenly distributed as defined by [swRefPointAlongCurveType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRefPointAlongCurveType_e.html)

*DDistance\_or\_Percent*
:   Distance at which to create the reference point on the selected entities or percentage of the length of the selected entities at which to create the reference point if NRefPointAlongCurveType is swRefPointAlongCurveDistance or swRefPointAlongCurvePercentage, respectively

*NumberOfRefPoints*
:   Number of reference points to create and evenly distribute on the selected entities if swRefPointAlongCurveType is swRefPointAlongCurveEvenlyDistributed

#### Return Value

Pointer to the [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) object

Remarks

This method creates one or more reference point features and adds them to the FeatureManager design tree. If the reference point feature is not created, a NULL value is returned.

The NumberOfRefPoints argument must contain a value of 1 to successfully create one reference point feature.

Example

[Insert Reference Points (VBA)](Insert_Reference_Points_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IFeatureManager::IInsertReferencePoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~IInsertReferencePoint.md)  
[IRefPointFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPointFeatureData.md)  
[IFeatureManager::EditReferencePoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~EditReferencePoint.md)
