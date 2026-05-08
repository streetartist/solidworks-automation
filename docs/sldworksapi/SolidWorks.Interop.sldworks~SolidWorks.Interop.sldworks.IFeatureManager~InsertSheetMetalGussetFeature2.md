# InsertSheetMetalGussetFeature2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSheetMetalGussetFeature2`

Obsolete. Superseded by IFeatureManager::InsertSheetMetalGussetFeature3.
Obsolete. Superseded by [IFeatureManager::InsertSheetMetalGussetFeature3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSheetMetalGussetFeature3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertSheetMetalGussetFeature2( _
   ByVal BOffset As System.Boolean, _
   ByVal DOffset As System.Double, _
   ByVal BFlipOffsetSide As System.Boolean, _
   ByVal ProfDimType As System.Integer, _
   ByVal DIndentDepth As System.Double, _
   ByVal DLength As System.Double, _
   ByVal BUseAngle As System.Boolean, _
   ByVal DHeight As System.Double, _
   ByVal DAngle As System.Double, _
   ByVal BFlipSides As System.Boolean, _
   ByVal DWidth As System.Double, _
   ByVal DThickness As System.Double, _
   ByVal BDraft As System.Boolean, _
   ByVal DDraftAngle As System.Double, _
   ByVal BInnerCornerFillet As System.Boolean, _
   ByVal DInnerCornerFilletRadius As System.Double, _
   ByVal BOuterCornerFillet As System.Boolean, _
   ByVal DOuterCornerFilletRadius As System.Double, _
   ByVal GussetType As System.Integer, _
   ByVal BEdgeFillet As System.Boolean, _
   ByVal DEdgeFilletRadius As System.Double, _
   ByVal ArrayOfFaces As System.Object, _
   ByVal ArrayRefLines As System.Object, _
   ByVal ArrayRefPoints As System.Object _
) As Feature
```

```

Dim instance As IFeatureManager
Dim BOffset As System.Boolean
Dim DOffset As System.Double
Dim BFlipOffsetSide As System.Boolean
Dim ProfDimType As System.Integer
Dim DIndentDepth As System.Double
Dim DLength As System.Double
Dim BUseAngle As System.Boolean
Dim DHeight As System.Double
Dim DAngle As System.Double
Dim BFlipSides As System.Boolean
Dim DWidth As System.Double
Dim DThickness As System.Double
Dim BDraft As System.Boolean
Dim DDraftAngle As System.Double
Dim BInnerCornerFillet As System.Boolean
Dim DInnerCornerFilletRadius As System.Double
Dim BOuterCornerFillet As System.Boolean
Dim DOuterCornerFilletRadius As System.Double
Dim GussetType As System.Integer
Dim BEdgeFillet As System.Boolean
Dim DEdgeFilletRadius As System.Double
Dim ArrayOfFaces As System.Object
Dim ArrayRefLines As System.Object
Dim ArrayRefPoints As System.Object
Dim value As Feature
 
value = instance.InsertSheetMetalGussetFeature2(BOffset, DOffset, BFlipOffsetSide, ProfDimType, DIndentDepth, DLength, BUseAngle, DHeight, DAngle, BFlipSides, DWidth, DThickness, BDraft, DDraftAngle, BInnerCornerFillet, DInnerCornerFilletRadius, BOuterCornerFillet, DOuterCornerFilletRadius, GussetType, BEdgeFillet, DEdgeFilletRadius, ArrayOfFaces, ArrayRefLines, ArrayRefPoints)
```

```

Feature InsertSheetMetalGussetFeature2( 
   System.bool BOffset,
   System.double DOffset,
   System.bool BFlipOffsetSide,
   System.int ProfDimType,
   System.double DIndentDepth,
   System.double DLength,
   System.bool BUseAngle,
   System.double DHeight,
   System.double DAngle,
   System.bool BFlipSides,
   System.double DWidth,
   System.double DThickness,
   System.bool BDraft,
   System.double DDraftAngle,
   System.bool BInnerCornerFillet,
   System.double DInnerCornerFilletRadius,
   System.bool BOuterCornerFillet,
   System.double DOuterCornerFilletRadius,
   System.int GussetType,
   System.bool BEdgeFillet,
   System.double DEdgeFilletRadius,
   System.object ArrayOfFaces,
   System.object ArrayRefLines,
   System.object ArrayRefPoints
)
```

```

Feature^ InsertSheetMetalGussetFeature2( 
   System.bool BOffset,
   System.double DOffset,
   System.bool BFlipOffsetSide,
   System.int ProfDimType,
   System.double DIndentDepth,
   System.double DLength,
   System.bool BUseAngle,
   System.double DHeight,
   System.double DAngle,
   System.bool BFlipSides,
   System.double DWidth,
   System.double DThickness,
   System.bool BDraft,
   System.double DDraftAngle,
   System.bool BInnerCornerFillet,
   System.double DInnerCornerFilletRadius,
   System.bool BOuterCornerFillet,
   System.double DOuterCornerFilletRadius,
   System.int GussetType,
   System.bool BEdgeFillet,
   System.double DEdgeFilletRadius,
   System.Object^ ArrayOfFaces,
   System.Object^ ArrayRefLines,
   System.Object^ ArrayRefPoints
) 
```

#### Parameters

*BOffset*
:   True to offset the gusset section plane from the selected reference point in ArrayRefPoints, false to not

*DOffset*
:   Value by which to offset the gusset section plane from the selected reference point in ArrayRefPoints; valid only if BOffset is true

*BFlipOffsetSide*
:   True to specify the gusset section plane offset on the opposite side of the selected reference point, false to not; valid only if BOffset is true

*ProfDimType*
:   Type of gusset profile dimensioning scheme as defined in [swSheetMetalGussetProfileDimType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetMetalGussetProfileDimType_e.html)

    (see **Remarks**)

*DIndentDepth*
:   Gusset indent depth; valid only if ProfDimType = 0

*DLength*
:   d1 gusset leg length; length of sheet metal from bend to intersection with first end of gusset; valid only if ProfDimType = 1 (see **Remarks**)

*BUseAngle*
:   True to dimension the angle that is formed by the intersection of the gusset with either face adjacent to the bend; valid only if ProfDimType = 1 (see **Remarks**)

*DHeight*
:   d2 gusset leg length; length of sheet metal from bend to intersection with second end of gusset; valid only if ProfDimType = 1 (see **Remarks**)

*DAngle*
:   Angle formed by intersection of gusset with one face adjacent to the bend; valid only if ProfDimType = 1 and BUseAngle is true (see **Remarks**)

*BFlipSides*
:   True to swap d1 and d2 legs in the dimensioning scheme, false to not; valid only if ProfDimType = 1 (see **Remarks**)

*DWidth*
:   Gusset width

*DThickness*
:   Gusset thickness

*BDraft*
:   True to draft gusset side faces, false to not

*DDraftAngle*
:   Angle by which to draft the gusset side faces; valid only if BDraft is true

*BInnerCornerFillet*
:   True to fillet the gusset inner corners, false to not

*DInnerCornerFilletRadius*
:   Inner corner fillet radius; valid only if BInnerCornerFillet is true

*BOuterCornerFillet*
:   True to fillet the gusset outer corners, false to not

*DOuterCornerFilletRadius*
:   Outer corner fillet radius; valid only if BOuterCornerFilletRadius is true

*GussetType*
:   Type of gusset as defined in [swSheetMetalRibGussetType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetMetalRibGussetType_e.html)

*BEdgeFillet*
:   True to fillet the edges of a flat back gusset, false to not; valid only if GussetType is flat

*DEdgeFilletRadius*
:   Edge fillet radius for the flat back gusset; valid only if BEdgeFillet is true and GussetType is flat

*ArrayOfFaces*
:   Array containing one or two [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)s that are the legs of the gusset feature:

    - Two flat faces adjacent to a bend
    - Two flat faces adjacent to a circular bend
    - One cylindrical bend face
    - One flat face and one non-planar face adjacent to a toroidal bend
    - One toroidal bend face

    (see **Remarks**)

*ArrayRefLines*
:   Array containing one of the following entities that is perpendicular to the gusset section plane:

    - Linear [IEdge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)
    - [ISketchSegment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md)

    (see **Remarks**)

*ArrayRefPoints*
:   Array containing one of the following to position the gusset section plane:

    - [IVertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md)
    - [ISketchPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md)
    - [IRefPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPoint.md)

    (see **Remarks**)

#### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

| If you pass an empty array to... | Then... |
| --- | --- |
| ArrayRefLines | This method assumes the reference line is the bend line adjacent to the entities in ArrayOfFaces. |
| ArrayRefPoints | You must set BOffset to true and specify DOffset for an assumed reference point.  For insertion of the first gusset, the assumed reference point is on the end of the sheet metal bend. For second and subsequent gusset insertions, the assumed reference point is on the edge of the gusset last inserted. |

Instead of calling this method, you can call [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to pre-select the references before calling [IFeatureManager::InsertSheetMetalGussetFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSheetMetalGussetFeature.md).

| If ProfDimType = 1, to dimension the gusset profile using... | Specify... |
| --- | --- |
| Both faces of the bend | - DLength of d1 leg - DHeight of d2 leg - BUseAngle = false - BFlipSides = true to swap d1 and d2 legs during dimensioning |
| One bend face and the angle it forms with the gusset | - DLength of d1 leg - DAngle of angle formed by gusset intersecting d1 leg - BUseAngle = true - BFlipSides = true to swap d1 and d2 legs during dimensioning |
| Opposite bend face and the angle it forms with the gusset | - DHeight of d2 leg - DAngle of angle formed by gusset intersecting d2 leg - BUseAngle = true - BFlipSides = true to swap d1 and d2 legs during dimensioning |

 See the SOLIDWORKS Help for more information about sheet metal gusset features.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[ISMGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.md)
