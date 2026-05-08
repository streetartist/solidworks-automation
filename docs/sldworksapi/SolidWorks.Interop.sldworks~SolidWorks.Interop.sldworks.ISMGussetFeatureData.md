# ISMGussetFeatureData Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData`

Allows access to a sheet metal gusset feature.
Allows access to a sheet metal gusset feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface ISMGussetFeatureData 
```

```

Dim instance As ISMGussetFeatureData
```

```

public interface ISMGussetFeatureData 
```

```

public interface class ISMGussetFeatureData 
```

Remarks

To create a sheet metal gusset feature:

1. Call [IFeatureManager::CreateDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateDefinition.md) to instantiate this feature data object.
2. Pre-select faces, lines, edges, vertices, or points as follows:

   | To... | Call [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to select... |
   | --- | --- |
   | Specify the legs of the gusset feature | - Two flat faces of a bend. - or -  - Two flat faces adjacent to a cylindrical bend face. - or -  - One cylindrical bend face. - or -  - One flat face and one non-planar face adjacent to a toroidal bend. - or -  - One toroidal bend face. |
   | Optionally orient the gusset section plane | One linear edge or sketch segment that is perpendicular to the gusset section plane.  If you do not pre-select either entity, then the bend line adjacent to the gusset legs is used as the reference. |
   | Optionally position the gusset section plane | One vertex, sketch point, or reference point.  If you do not pre-select any of these entities, then you must set [ISMGussetFeatureData::UseOffset](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~UseOffset.md) to true and specify [ISMGussetFeatureData::OffsetDistance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~OffsetDistance.md) to define the reference point. For insertion of the first gusset, the assumed reference point is on the end of the sheet metal bend. For second and subsequent gusset insertions, the assumed reference point is on the edge of the gusset last inserted. |
3. Specify [ISMGussetFeatureData::ProfileDimensionScheme](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~ProfileDimensionScheme.md) and modify other properties on this feature data object as follows:

   | If ISMGussetFeatureData::ProfileDimensionScheme=  [swSheetMetalGussetProfileDimType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetMetalGussetProfileDimType_e.html).  swSheetMetalGussetProfileDimType\_ProfileDimensions, to dimension the gusset profile using... | Specify ISMGussetFeatureData::... |
   | --- | --- |
   | Both legs of the gusset | - [ProfileLengthDim](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~ProfileLengthDim.md) for d1 leg - [ProfileHeightDim](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~ProfileHeightDim.md) for d2 leg - [UseAngleDimForProfile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~UseAngleDimForProfile.md) = false - [FlipDimSides](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~FlipDimSides.md) = true to swap d1 and d2 legs during dimensioning |
   | d1 leg and the angle it forms with the gusset | - ProfileLengthDim for d1 leg - [ProfileAngleDim](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~ProfileAngleDim.md) of angle formed by gusset intersecting d1 leg - UseAngleDimForProfile = true - FlipDimSides = true to swap d1 and d2 legs during dimensioning |
   | d2 leg and the angle it forms with the gusset | - ProfileHeightDim for d2 leg - ProfileAngleDim of angle formed by gusset intersecting d2 leg - UseAngleDimForProfile = true - FlipDimSides = true to swap d1 and d2 legs during dimensioning |
4. Call [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.md).

For more information, see the **SOLIDWORKS user-interface help > Sheet Metal > Using Sheet Metal Tools > Adding Sheet Metal Gussets > Sheet Metal Gusset PropertyManager** topic.

Example

'VBA

'----------------------------------------------------------------------------  
' Preconditions:  
' 1. Open *public\_documents***\samples\tutorial\api\SMGussetAPI.sldprt**.  
' 2. Open an Immediate window.  
'  
' Postconditions:  
' 1. Inserts **Sheet Metal Gusset1**.  
' 2. Press F5 and observe the modified gusset.  
' 3. Inspect the Immediate window for the flatten settings of the gusset.  
' 4. Expand Flat-Pattern in the FeatureManager design tree, right-click  
'    **Flat-Pattern(1),** and click Unsuppress.  
' 5. Observe the center mark and profile of the gusset in its  
'    flattened state.  
'  
' NOTE: Because the model is used elsewhere, do not save changes.  
' ---------------------------------------------------------------------------  
Dim swApp As SldWorks.SldWorks  
Dim Part As SldWorks.ModelDoc2  
Dim myFeature As SldWorks.Feature  
Dim swFeat As SldWorks.Feature  
Dim swFeatData As SldWorks.SMGussetFeatureData  
Dim boolstatus As Boolean  
Option Explicit  
Sub main()  
    Set swApp = Application.SldWorks  
    Set Part = swApp.ActiveDoc  
     
    boolstatus = Part.Extension.SelectByID2("", "FACE", -5.38403893476698E-02, 3.6701308754914E-03, 0.05530817474488, False, 0, Nothing, 0)  
    boolstatus = Part.Extension.SelectByID2("", "FACE", -1.77780871801474E-02, -3.07393226379986E-02, 3.41128529187245E-02, True, 0, Nothing, 0)  
     
    Set swFeatData = Part.FeatureManager.**CreateDefinition**(swFeatureNameID\_e.swFmSMGusset)  
    swFeatData.**UseOffset** = True  
    swFeatData.**OffsetDistance** = 0.05  
    swFeatData.**FlipOffset** = False  
    swFeatData.**ProfileDimensionScheme** = swSheetMetalGussetProfileDimType\_e.swSheetMetalGussetProfileDimType\_IndentDepth  
    swFeatData.**IndentDepth** = 0.01  
    swFeatData.**ProfileLengthDim** = 0#  
    swFeatData.**UseAngleDimForProfile** = False  
    swFeatData.**ProfileHeightDim** = 0#  
    swFeatData.**ProfileAngleDim** = 0#  
    swFeatData.**FlipDimSides** = False  
    swFeatData.**IndentWidth** = 0.01  
    swFeatData.**GussetThickness** = 0.003  
    swFeatData.**DraftAngle** = 3 \* 0.0175  
    swFeatData.**DraftSideFaces** = True  
    swFeatData.**FilletInnerCorners** = True  
    swFeatData.**InnerCornerFilletRadius** = 0.002  
    swFeatData.**FilletOuterCorners** = True  
    swFeatData.**OuterCornerFilletRadius** = 0.001  
    swFeatData.**GussetType** = swSheetMetalRibGussetType\_e.swSheetMetalRibGussetType\_Rounded  
    swFeatData.**FilletGussetEdges** = False  
    swFeatData.**EdgeFilletRadius** = 0#  
    swFeatData.**OverrideDocSettings** = True  
    swFeatData.**ShowProfile** = True  
    swFeatData.**ShowCenter** = True  
     
    Set myFeature = Part.FeatureManager.**CreateFeature**(swFeatData)  
    Part.ClearSelection2 True  
     
    Stop  
     
    'Modify type, draft, and outer corner fillet properties of the gusset  
    boolstatus = Part.Extension.SelectByID2("Sheet Metal Gusset1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)  
    Set swFeat = Part.SelectionManager.GetSelectedObject6(1, -1)  
         
    Set swFeatData = swFeat.**GetDefinition**  
    swFeatData.**AccessSelections** Part, Nothing  
    swFeatData.**GussetType** = swSheetMetalRibGussetType\_e.swSheetMetalRibGussetType\_Flat  
    swFeatData.**DraftSideFaces** = False  
    swFeatData.**FilletOuterCorners** = False  
    Debug.Print "Sheet Metal Gusset1 Flatten Settings"  
    Debug.Print "  Override document flat pattern properties? " & swFeatData.**OverrideDocSettings**  
    Debug.Print "  Show center marks of the gusset in its flattened state? " & swFeatData.**ShowCenter**  
    Debug.Print "  Show profile of the gusset in its flattened state? " & swFeatData.**ShowProfile**  
         
    swFeat.**ModifyDefinition** swFeatData, Part, Nothing  
    swFeatData.**ReleaseSelectionAccess**

End Sub

Example

[Create Sheet Metal Gusset (VB.NET)](Create_Sheet_Metal_Gusset_Example_VBNET.htm)  
[Create Sheet Metal Gusset (C#)](Create_Sheet_Metal_Gusset_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISMGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IFeatureManager::InsertSheetMetalGussetFeature Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSheetMetalGussetFeature.md)  
[IFeatureManager::InsertSheetMetalGussetFeature2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSheetMetalGussetFeature2.md)
