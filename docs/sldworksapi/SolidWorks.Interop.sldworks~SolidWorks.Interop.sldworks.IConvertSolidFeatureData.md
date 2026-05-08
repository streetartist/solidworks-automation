# IConvertSolidFeatureData Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData`

Allows access to a convert solid feature.
Allows access to a convert solid feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IConvertSolidFeatureData 
```

```

Dim instance As IConvertSolidFeatureData
```

```

public interface IConvertSolidFeatureData 
```

```

public interface class IConvertSolidFeatureData 
```

Remarks

To create a ConvertSolid feature:

1. Ensure that the Sheet Metal tab is visible on the CommandManager toolbar.
2. Call [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to select the fixed face (with Mark=0) and bend edges (with Mark=1).
3. Call [IFeatureManager::CreateDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateDefinition.md)(swFmSolidToSheetMetal) to create this feature data object.
4. Instantiate and specify the [ICustomBendAllowance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance.md) object.
5. Call [IConvertSolidFeatureData::Initialize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~Initialize.md).
6. Call [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.md) to create the ConvertSolid feature.

To modify a ConvertSolid feature:

1. Call [IFeature::GetDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDefinition.md) to obtain this feature data object.
2. Call [IConvertSolidFeatureData::AccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~AccessSelections.md).
3. Modify properties as needed.
4. Call [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.md) to finalize any changes or [IConvertSolidFeatureData::ReleaseSelectionAccess](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~ReleaseSelectionAccess.md) if no changes were made.

For more information about converting solids or surface bodies to sheet metal parts, see the **SOLIDWORKS user-interface online help > Sheet Metal > Comparing Sheet Metal Design Methods > Convert to Sheet Metal Tool** topics.

Example

'VBA

'This example demonstrates how to convert a solid to sheet metal.

'------------------------------------------------------------------

'Preconditions:

'1. Open *public\_documents***\SOLIDWORKS\SOLIDWORKS 2025\samples\tutorial\api\sweepcutextrude.sldprt**.

'2. Ensure that the Sheet Metal tab is visible on the Command Manager toolbar.

'3. Open an Immediate window.

'

'Postconditions:

' 1. Creates **Convert-Solid1** and **Sheet-Metal1**.

' 2. Inspect the FeatureManager design tree and the Immediate window.

'

' NOTE: Because the model may be used elsewhere, do not save changes to it.

'-------------------------------------------------------------

Option Explicit

Sub main()

    Dim swApp As SldWorks.SldWorks

    Dim swModel As SldWorks.ModelDoc2

    Dim swFeat As SldWorks.Feature

    Dim FeatMgr As SldWorks.FeatureManager

    Dim swConvertSolidFeatData As SldWorks.ConvertSolidFeatureData

    Dim FeatData As SldWorks.ConvertSolidFeatureData

    Dim boolstatus As Boolean

    Dim cba As SldWorks.CustomBendAllowance

    Dim face As SldWorks.Face2

    Dim faceId As Variant

   

    Set swApp = Application.SldWorks

    Set swModel = swApp.ActiveDoc

    Set FeatMgr = swModel.FeatureManager

   

    boolstatus = swModel.Extension.**SelectByID2**("", "FACE", 4.130570195002E-04, 0.02357994168921, 0.02568415695742, True, 0, Nothing, 0)

    boolstatus = swModel.Extension.**SelectByID2**("", "EDGE", -0.00190522473838, 0.02387533864419, 0.04979931166838, True, 1, Nothing, 0)

    boolstatus = swModel.Extension.**SelectByID2**("", "EDGE", 0.02911271681069, 0.02376277320678, 0.02892436699148, True, 1, Nothing, 0)

    boolstatus = swModel.Extension.**SelectByID2**("", "EDGE", -0.004838857104858, 0.02387396382323, -1.997542986487E-04, True, 1, Nothing, 0)

    'Create a feature data object

    Set swConvertSolidFeatData = FeatMgr.**CreateDefinition**(swFmSolidToSheetMetal)

   

    Set cba = swConvertSolidFeatData.**GetCustomBendAllowance**()

  

    cba.Type = swBendAllowanceKFactor

    cba.KFactor = 0.08

   

    'Initialize the feature data object with custom bend allowance

    swConvertSolidFeatData.**Initialize** True, False, cba

    

    'Create the feature

    Set swFeat = FeatMgr.**CreateFeature**(swConvertSolidFeatData)

   

    Set FeatData = swFeat.**GetDefinition**()

   

    Set cba = swConvertSolidFeatData.**GetCustomBendAllowance**()

  

    Debug.Print "Type of custom bend allowance as defined in swBendAllowanceTypes\_e: " & cba.**Type**

    Debug.Print "K factor: " & cba.**KFactor**

    Debug.Print "SheetMetal thickness : " & FeatData.**SheetThickness**

    Debug.Print "Bend Radius  : " & FeatData.**BendRadius**

    Debug.Print "Reverse thickness : " & FeatData.**ReverseThickness**

    Debug.Print "Keep body : " & FeatData.**KeepBody**

    Debug.Print "Overlap type : " & FeatData.**CornerDefaults**

    Debug.Print "Rip gaps : " & FeatData.**RipGap**

    Debug.Print "Rip overlap ratio : " & FeatData.**RipOverlapRatio**

    Debug.Print "Auto relief type : " & FeatData.**ReliefType**

    Debug.Print "Auto relief ratio : " & FeatData.**ReliefRatio**

   

    FeatData.**AccessSelections** swModel, Nothing

   

    Set face = FeatData.**GetFixedFace**

    faceId = face.**GetFaceId**()

    Debug.Print "Fixed face ID: " & faceId

   

    'Modify initial values

    FeatData.**SheetThickness** = 0.014

    FeatData.**BendRadius** = 0.0006

   

    'Modify the feature definition

    swFeat.**ModifyDefinition** FeatData, swModel, Nothing

    Debug.Print "----------------------------After Setting Values-------------------------------"

   

    Debug.Print "SheetMetal thickness : " & FeatData.**SheetThickness**

    Debug.Print "Bend Radius  : " & FeatData.**BendRadius**

    Debug.Print "Reverse thickness : " & FeatData.**ReverseThickness**

    Debug.Print "Keep body : " & FeatData.**KeepBody**

    Debug.Print "Overlap type : " & FeatData.**CornerDefaults**

    Debug.Print "Rip gaps : " & FeatData.**RipGap**

    Debug.Print "Rip overlap ratio : " & FeatData.**RipOverlapRatio**

    Debug.Print "Auto relief type : " & FeatData.**ReliefType**

    Debug.Print "Auto relief ratio : " & FeatData.**ReliefRatio**

   

End Sub

Example

[Create ConvertSolid Feature (VB.NET)](Create_ConvertSolid_Feature_Example_VBNET.htm)  
[Create ConvertSolid Feature (C#)](Create_ConvertSolid_Feature_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConvertSolidFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
