# ILibraryFormToolFeatureData Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData`

Allows access to library forming tool feature data.
Allows access to library forming tool feature data.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface ILibraryFormToolFeatureData 
```

```

Dim instance As ILibraryFormToolFeatureData
```

```

public interface ILibraryFormToolFeatureData 
```

```

public interface class ILibraryFormToolFeatureData 
```

Remarks

To create a library forming tool feature:

1. Ensure that the Sheet Metal tab is visible on the CommandManager toolbar.
2. Call [IModelDocExtension::SelectByRay](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByRay.md) to select a flat face (with Mark = 0) on which to use a forming tool.
3. Call [IFeatureManager::CreateDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateDefinition.md)(swFmFormToolInstance) to create this feature data object.
4. Call [ILibraryFormToolFeatureData::OverrideDocumentSettings](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData~OverrideDocumentSettings.md) to specify flat pattern visibility options.
5. Specify the forming tool and its rotation angle for placement using [ILibraryFormToolFeatureData::FormToolConfiguration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData~FormToolConfiguration.md), [FormToolPath](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData~FormToolPath.md), [LinkToFormTool](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData~LinkToFormTool.md), and [RotationAngle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData~RotationAngle.md).
6. Call [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.md) to create the feature.

To modify a library form tool feature:

1. Select a new location by clicking on a flat face in the graphics area where to re-position and/or replace the forming tool.
2. Call [IFeature::GetDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDefinition.md) to obtain this feature data object.
3. Call [ILibraryFormToolFeatureData::AccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData~AccessSelections.md).
4. Specify [ILibraryFormToolFeatureData::SetPlacementFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData~SetPlacementFace.md) to re-position the forming tool.
5. Call ILibraryFormToolFeatureData::OverrideDocumentSettings to change the flat pattern visibility options.
6. Modify ILibraryFormToolFeatureData::FormToolConfiguration, FormToolPath (a change to FormToolPath changes the feature name), LinkToFormTool, and RotationAngle.
7. Call [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.md) to finalize any changes or [ILibraryFormToolFeatureData::ReleaseSelectionAccess](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData~ReleaseSelectionAccess.md) if no changes were made.

Forming tools are dies that dent, bend, stretch, or otherwise form sheet metal. For more information about forming tools, see the **SOLIDWORKS user-interface online help > Sheet Metal > Using Forming Tools with Sheet Metal** topics.

Example

'VBA

'This example demonstrates how to insert a design library forming tool into a sheet metal part and reposition and replace it with another forming tool.

'----------------------------------------------------------------------------

' Preconditions:

' 1. Open *public\_documents***\samples\tutorial\sheetmetal\formtools\cover.sldprt**.

' 2. Ensure that the two specified formtoolpath locations exist.

' 3. Ensure that the Sheet Metal tab is visible on the CommandManager toolbar.

' 4. Run macro.

' 5. At the pause, inspect the FeatureManager design tree and the graphics area for the drafted rectangular emboss forming tool.

'    Then select a flat face where to re-position (and replace) the forming tool.

' 6. Press F5 finish.

'

' Postconditions:

' 1. A dimple emboss replaces the drafted rectangular emboss.

' 2. Inspect the FeatureManager design tree, graphics area, and the Immediate window.

'

' NOTE: Do not save the part as it may be used elsewhere.

' ---------------------------------------------------------------------------

Dim swApp As SldWorks.SldWorks

Dim swModel As ModelDoc2

Dim featMgr As FeatureManager

Dim boolstatus As Boolean

Option Explicit

Sub main()

    Set swApp = Application.SldWorks

    Set swModel = swApp.ActiveDoc

   

    'Select a flat face where to insert an emboss forming tool

    boolstatus = swModel.Extension.SelectByRay(5.53557395141979E-02, 3.03381093343091E-02, 2.66948404126879E-02, -0.707061513640545, -0.415946801562901, -0.57188484347632, 5.32844353755021E-04, 2, False, 0, 0)

   

    Set featMgr = swModel.FeatureManager

   

    Dim LibFormToolFeatureData As LibraryFormToolFeatureData

    Set LibFormToolFeatureData = featMgr.**CreateDefinition**(swFmFormToolInstance)

   

    LibFormToolFeatureData.**LinkToFormTool** = True

    LibFormToolFeatureData.**FormToolPath** = "*install\_dir***\data\Design Library\forming tools\embosses\drafted rectangular emboss.sldftp**"

    Call LibFormToolFeatureData.**OverrideDocumentSettings**(True, True, True, True)

    LibFormToolFeatureData.**RotationAngle** = 0.**5**

    Dim swFeat As Feature

    Set swFeat = featMgr.**CreateFeature**(LibFormToolFeatureData)

   

    **Stop** ' Inspect the graphics area and FeatureManager design tree; select a flat face where to re-position (and replace) the forming tool

   

    Dim selMgr As SelectionMgr

    Set selMgr = swModel.SelectionManager

   

    Dim face2 As face2

    Set face2 = selMgr.GetSelectedObject6(1, -1)

   

    Dim pickPt As Variant

    pickPt = selMgr.GetSelectionPoint2(1, -1)

   

    Dim MU As MathUtility

    Set MU = swApp.GetMathUtility()

   

    Dim mathPt As MathPoint

    Set mathPt = MU.CreatePoint(pickPt)

   

    swModel.ClearSelection2 (True)

   

    Dim swLibFormFeatData1 As LibraryFormToolFeatureData

    Set swLibFormFeatData1 = swFeat.**GetDefinition**()

   

    Debug.Print swLibFormFeatData1.**GetPunchID**()

    Debug.Print swLibFormFeatData1.**FormToolConfiguration**

    Debug.Print swLibFormFeatData1.**FormToolPath**

    Debug.Print swLibFormFeatData1.**LinkToFormTool**

    Debug.Print swLibFormFeatData1.**RotationAngle**

   

    Debug.Print swLibFormFeatData1.**AccessSelections**(swModel, Nothing)

   

    Dim face As face2

    Set face = swLibFormFeatData1.**PlacementFace**

   

    swLibFormFeatData1.**RotationAngle** = 0.7833

    Call swLibFormFeatData1.**OverrideDocumentSettings**(True, True, True, True)

    swLibFormFeatData1.**FormToolConfiguration** = "Default"

    swLibFormFeatData1.**FormToolPath** = "*install\_dir***\data\Design Library\forming tools\embosses\dimple.SLDFTP**"

    swLibFormFeatData1.**LinkToFormTool** = True

    Dim ent As Entity

    Set ent = face

    Call ent.Select4(True, Nothing)

    Call swLibFormFeatData1.**SetPlacementFace**(face2, mathPt)

   

    Debug.Print swFeat.**ModifyDefinition**(swLibFormFeatData1, swModel, Nothing)

   

    Dim face1 As face2

    Set face1 = swLibFormFeatData1.**PlacementFace**

End Sub

Example

[Create Forming Tool Feature (VB.NET)](Create_Forming_Tool_Feature_Example_VBNET.htm)  
[Create Forming Tool Feature (C#)](Create_Forming_Tool_Feature_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILibraryFormToolFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IFeatureManager::CreateFormTool2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFormTool2.md)  
[IView::InsertPunchTable Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~InsertPunchTable.md)
