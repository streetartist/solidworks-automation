# InsertSheetMetalGussetFeature Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSheetMetalGussetFeature`

Obsolete. Superseded by IFeatureManager::InsertSheetMetalGussetFeature3.
Obsolete. Superseded by [IFeatureManager::InsertSheetMetalGussetFeature3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSheetMetalGussetFeature3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertSheetMetalGussetFeature( _
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
   ByVal DEdgeFilletRadius As System.Double _
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
Dim value As Feature
 
value = instance.InsertSheetMetalGussetFeature(BOffset, DOffset, BFlipOffsetSide, ProfDimType, DIndentDepth, DLength, BUseAngle, DHeight, DAngle, BFlipSides, DWidth, DThickness, BDraft, DDraftAngle, BInnerCornerFillet, DInnerCornerFilletRadius, BOuterCornerFillet, DOuterCornerFilletRadius, GussetType, BEdgeFillet, DEdgeFilletRadius)
```

```

Feature InsertSheetMetalGussetFeature( 
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
   System.double DEdgeFilletRadius
)
```

```

Feature^ InsertSheetMetalGussetFeature( 
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
   System.double DEdgeFilletRadius
) 
```

#### Parameters

*BOffset*
:   True to offset the gusset section plane from the selected reference point, false to not

*DOffset*
:   Value by which to offset the gusset section plane from the selected reference point; valid only if BOffset is true

*BFlipOffsetSide*
:   True to specify the gusset section plane offset on the opposite side of the selected reference point, false to not; valid only if BOffset is true

*ProfDimType*
:   Type of gusset profile dimensioning scheme:

    - 0 = indent
    - 1 = profile dimensioning

    (see **Remarks**)

*DIndentDepth*
:   Gusset depth; valid only if ProfDimType = 0

*DLength*
:   d1 gusset leg length; length of sheet metal from bend to intersection with first end of gusset; valid only if ProfDimType = 1 (see **Remarks**)

*BUseAngle*
:   True to dimension the angle that is formed by the intersection of the gusset with either face adjacent to the bend; valid only if ProfDimType = 1 (see **Remarks**)

*DHeight*
:   d2 gusset leg length; length of sheet metal from bend to intersection with second end of gusset; valid only if ProfDimType = 1 (see **Remarks**)

*DAngle*
:   Angle formed by intersection of gusset with one face adjacent to the bend; valid only if ProfDimType = 1 and BUseAngle is true (see **Remarks**)

*BFlipSides*
:   True to swap d1 and d2 in the dimensioning scheme, false to not; valid only if ProfDimType = 1 (see **Remarks**)

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
:   Type of gusset:

    - 0 = rounded back
    - 1 = flat back

*BEdgeFillet*
:   True to fillet the edges of a gusset, false to not; valid only if GussetType = 1

*DEdgeFilletRadius*
:   Edge fillet radius; valid only if BEdgeFillet is true and GussetType = 1

#### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

Before calling this method to create a sheet metal gusset feature, you must pre-select faces, lines, edges, vertices, or points as follows:

| To... | Call [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to select... |
| --- | --- |
| Specify the legs of the gusset feature | - Two flat faces of a bend.   - or -   - Two flat faces adjacent to a cylindrical bend face.   - or -   - One cylindrical bend face.   - or -   - One flat face and one non-planar face adjacent to a toroidal bend.   - or -   - One toroidal bend face. |
| Optionally orient the gusset section plane | One linear edge or sketch segment that is perpendicular to the gusset section plane.  If you do not pre-select either entity, then the method uses the bend line adjacent to the gusset legs as the reference. |
| Optionally position the gusset section plane | One vertex, sketch point, or reference point.  If you do not pre-select any one of these entities, then you must set BOffset to true and specify DOffset for an assumed reference point. For insertion of the first gusset, the assumed reference point is on the end of the sheet metal bend. For second and subsequent gusset insertions, the assumed reference point is on the edge of the gusset last inserted. |

Instead of pre-selecting the references and calling this method, you can pass the references as arrays to [IFeatureManager::InsertSheetMetalGussetFeature2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSheetMetalGussetFeature2.md).

| If ProfDimType = 1, to dimension the gusset profile using... | Specify... |
| --- | --- |
| Both legs of the gusset | - DLength of d1 leg - DHeight of d2 leg - BUseAngle = false - BFlipSides = true to swap d1 and d2 legs during dimensioning |
| d1 leg and the angle it forms with the gusset | - DLength of d1 leg - DAngle of angle formed by gusset intersecting d1 leg - BUseAngle = true - BFlipSides = true to swap d1 and d2 legs during dimensioning |
| d2 leg and the angle it forms with the gusset | - DHeight of d2 leg - DAngle of angle formed by gusset intersecting d2 leg - BUseAngle = true - BFlipSides = true to swap d1 and d2 legs during dimensioning |

See the SOLIDWORKS Help for more information about sheet metal gusset features.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[ISMGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.md)
