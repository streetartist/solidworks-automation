# InsertSheetMetalLoftedBend2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSheetMetalLoftedBend2`

Inserts a lofted bend in a sheet metal part.
Inserts a lofted bend in a sheet metal part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertSheetMetalLoftedBend2( _
   ByVal ThickDirType As System.Integer, _
   ByVal Thickness As System.Double, _
   ByVal BFormed As System.Boolean, _
   ByVal DRadius As System.Double, _
   ByVal BReferToEndPoint As System.Boolean, _
   ByVal EFacetOption As System.Integer, _
   ByVal DChordTol As System.Double, _
   ByVal INumBends As System.Integer, _
   ByVal DSegLength As System.Double, _
   ByVal DSegAngle As System.Double _
) As Feature
```

```

Dim instance As IFeatureManager
Dim ThickDirType As System.Integer
Dim Thickness As System.Double
Dim BFormed As System.Boolean
Dim DRadius As System.Double
Dim BReferToEndPoint As System.Boolean
Dim EFacetOption As System.Integer
Dim DChordTol As System.Double
Dim INumBends As System.Integer
Dim DSegLength As System.Double
Dim DSegAngle As System.Double
Dim value As Feature
 
value = instance.InsertSheetMetalLoftedBend2(ThickDirType, Thickness, BFormed, DRadius, BReferToEndPoint, EFacetOption, DChordTol, INumBends, DSegLength, DSegAngle)
```

```

Feature InsertSheetMetalLoftedBend2( 
   System.int ThickDirType,
   System.double Thickness,
   System.bool BFormed,
   System.double DRadius,
   System.bool BReferToEndPoint,
   System.int EFacetOption,
   System.double DChordTol,
   System.int INumBends,
   System.double DSegLength,
   System.double DSegAngle
)
```

```

Feature^ InsertSheetMetalLoftedBend2( 
   System.int ThickDirType,
   System.double Thickness,
   System.bool BFormed,
   System.double DRadius,
   System.bool BReferToEndPoint,
   System.int EFacetOption,
   System.double DChordTol,
   System.int INumBends,
   System.double DSegLength,
   System.double DSegAngle
) 
```

#### Parameters

*ThickDirType*
:   Toggles the thickening direction:

    - 0 = outside
    - 1 = inside (default value)

*Thickness*
:   Thickness of the bend

*BFormed*
:   True to insert a formed lofted bend; false to insert a bent lofted bend (default)

*DRadius*
:   Bend radius; valid only if BFormed is false

*BReferToEndPoint*
:   True to calculate facet transitions using theoretical vertexes, false to calculate facet transitions using the smallest possible arcs that avoid interference between bend areas; valid only if BFormed is false

*EFacetOption*
:   Faceting option as defined in [swLoftedBendFacetOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLoftedBendFacetOptions_e.html); valid only if BFormed is false

*DChordTol*
:   Chord tolerance or maximum distance between the arc and linear segment of a chord; valid only if EFacetOption is set to swLoftedBendFacetOptions\_e.swChordTolerance and BFormed is false

*INumBends*
:   Maximum number of bends per transition segment; valid only if EFacetOption is set to swLoftedBendFacetOptions\_e.swBendsPerTransitionSegment and BFormed is false

*DSegLength*
:   Maximum length of the linear segment; valid only if EFacetOption is set to swLoftedBendFacetOptions\_e.swSegmentLength and BFormed is false

*DSegAngle*
:   Maximum angle between adjacent linear segments; valid only if EFacetOption is set to swLoftedBendFacetOptions\_e.swSegmentAngle and BFormed is false

#### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

Before calling this method, you must select at least two sketch profiles that are on parallel planes. You can either multi-select them in the graphics area or call [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) with Mark = 1 for each sketch profile you want to select.

Example

[Insert Lofted Bend Feature (VBA)](Insert_Lofted_Bend_Feature_Example_VB.htm)  
[Insert Lofted Bend Feature (VB.NET)](Insert_Lofted_Bend_Feature_Example_VBNET.htm)  
[Insert Lofted Bend Feature (C#)](Insert_Lofted_Bend_Feature_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[ILoftedBendsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData.md)  
[ILoftFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData.md)  
[ISheetMetalFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.md)
