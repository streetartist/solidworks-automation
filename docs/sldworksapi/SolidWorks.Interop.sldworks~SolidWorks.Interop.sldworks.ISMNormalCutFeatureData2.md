# ISMNormalCutFeatureData2 Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2`

Allows access to a sheet metal normal cut feature.
Allows access to a sheet metal normal cut feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface ISMNormalCutFeatureData2 
```

```

Dim instance As ISMNormalCutFeatureData2
```

```

public interface ISMNormalCutFeatureData2 
```

```

public interface class ISMNormalCutFeatureData2 
```

Remarks

Extruded cuts that pierce models at an angle have non-normal side walls. To make these side walls normal, you create a normal cut feature.

To create a normal cut feature:

1. Open a sheet metal part that has a cut-extrude with non-normal side walls.
2. Call IFeatureManager::CreateDefinition(swFmNormalCut) to access this interface.
3. Set non-entity properties on this interface.
4. Use [IModelDocExtension::SelectByRay](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByRay.md) or [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) with Mark = 4 to select the offset plane, only if [ISMNormalCutFeatureData2::NormalCutParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2~NormalCutParameters.md) is set to [swNormalCutParameters\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swNormalCutParameters_e.html).swNormalCutOffsetPlane.
5. Use IModelDocExtension::SelectByRay or IModelDocExtension::SelectByID2 with Mark = 8 to select the direction of the normal cut, only if ISMNormalCutFeatureData2::NormalCutParameters is set to swNormalCutParameters\_e.swNormalCutExtent.
6. Use IModelDocExtension::SelectByRay or IModelDocExtension::SelectByID2 with Mark = 1 to select each non-normal face in the group. If [ISMNormalCutFeatureData2::AutoPropagation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2~AutoPropagation.md) is set to true, then all faces tangent to a selected face are automatically added to the face group.
7. Call [ISMNormalCutFeatureData2::CreateGroup](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2~CreateGroup.md) to access [ISMNormalCutGroupData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutGroupData.md).
8. Repeat steps 6 and 7 as many times as you have face groups. Call [IModelDoc2::ClearSelection2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ClearSelection2.md) after each face group is created.
9. Call [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.md).

To edit a normal cut feature:

1. Call IFeature::GetDefinition to get this feature data object for a selected normal cut feature.
2. Call [ISMNormalCutFeatureData2::AccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2~AccessSelections.md). **Note:** **Any selections made \**before\** this call are invalid. To edit the properties of this feature, you must re-select their entities during the editing session, i.e., after calling ISMNormalCutFeatureData2::AccessSelections. (See step 5.)**
3. Call [ISMNormalCutFeatureData2::GetGroupNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2~GetGroupNames.md) and [ISMNormalCutFeatureData2::GetGroupByName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2~GetGroupByName.md) to access ISMNormalCutGroupData for an existing face group.
4. Call ISMNormalCutFeatureData2::CreateGroup to create another face group if needed.
5. Modify [cut direction](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2~CutDirection.md), [offset plane reference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2~OffsetPlaneReference.md), or other properties on ISMNormalCutFeatureData2 as needed. To select property entities, use IModelDocExtension::SelectByRay or IModelDocExtension::SelectByID2 followed by [ISelectionMgr::GetSelectedObject6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject6.md). You can also use [IEntity::Select4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~Select4.md).
6. Call [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.md) if you modifed the feature or [ISMNormalCutFeatureData2::ReleaseSelectionAccess](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2~ReleaseSelectionAccess.md) if you did not.

Example

'VBA

'\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

'1. Open **c:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\whatsnew\sheet metal\normal\_cut.sldprt**.  
'2. Open the Immediate window.  
'3. Run the macro.  
'4. Creates **Normal Cut1** in the FeatureManager design tree.  
'5. Edits the feature by specifying a normal cut direction entity.  
'6. Inspect the Immediate window.

'\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Option Explicit  
Dim swApp As SldWorks.SldWorks  
Dim swModel As SldWorks.ModelDoc2  
Dim swModelDocExt As SldWorks.ModelDocExtension  
Dim swFeatMgr As SldWorks.FeatureManager  
Dim swFeat As SldWorks.Feature  
Dim swNormalCutFeatData As SldWorks.SMNormalCutFeatureData2  
Dim grpData As SldWorks.SMNormalCutGroupData  
Dim swSelMgr As SldWorks.SelectionMgr  
Dim swCutDirectionFace As SldWorks.Face2  
Dim errCode As Long  
Dim boolstatus As Boolean  
Dim varGrpNames As Variant  
Dim i As Long  
Dim j As Long  
Dim Name As String  
Dim Face As SldWorks.Face2

Sub main()

    Set swApp = Application.SldWorks  
    Set swModel = swApp.**ActiveDoc**  
    Set swModelDocExt = swModel.**Extension**  
    Set swFeatMgr = swModel.**FeatureManager**  
    Set swNormalCutFeatData = swFeatMgr.**CreateDefinition**(swFmNormalCut)  
    swNormalCutFeatData.**AutoPropagation** = True  
    swNormalCutFeatData.**OptimizeGeometry** = True  
    swNormalCutFeatData.**NormalCutParameters** = swNormalCutExtent

    ' Select the face(s) to make normal

    boolstatus = swModel.**Extension**.**SelectByRay**(4.71296104838217E-02, 1.42054003862171E-02, -6.68923799798904E-03, -0.13322686545804, 0.182153484913837, 0.974202602261958, 6.19874904830013E-04, 2, True, 1, 0)

    Set grpData = swNormalCutFeatData.**CreateGroup**(errCode)  
     
    ' Create the normal cut feature  
  
    Set swFeat = swFeatMgr.**CreateFeature**(swNormalCutFeatData)

    ' Modify the normal cut feature  
  
    Set swNormalCutFeatData = swFeat.**GetDefinition**()  
    swNormalCutFeatData.**AccessSelections** swModel, Nothing  
    varGrpNames = swNormalCutFeatData.**GetGroupNames**()

    For i = 0 To UBound(varGrpNames)  
        Name = varGrpNames(i)  
        Debug.Print "GroupName: " & Name  
        Set grpData = swNormalCutFeatData.**GetGroupByName**(Name)  
        Dim varFaces As Variant  
        varFaces = grpData.**Faces**  
        For j = 0 To UBound(varFaces)  
            Set Face = varFaces(j)  
            Debug.Print "Face " & j & " area: " & Face.**GetArea**  
        Next j  
        Debug.Print "--------------------"  
    Next i  
     
    'Specify the cut direction  
  
    Set swSelMgr = swModel.**SelectionManager**  
    boolstatus = swModel.**Extension**.**SelectByRay**(-0.149999999999892, 2.58556514245498E-02, -4.63505465353364E-03, 0.393242668518252, 0.12460738379391, -0.910951811876282, 1.22626958447854E-03, 2, False, 0, 0)  
    Set swCutDirectionFace = Nothing  
    Set swCutDirectionFace = swSelMgr.**GetSelectedObject6**(1, -1)  
     
    Dim swSelectEnt As SldWorks.Entity  
    Set swSelectEnt = swCutDirectionFace  
    boolstatus = swSelectEnt.**Select4**(False, Nothing)  
    swNormalCutFeatData.**CutDirection** = swCutDirectionFace

    Dim isModified As Boolean  
    isModified = swFeat.**ModifyDefinition**(swNormalCutFeatData, swModel, Nothing)  
     
End Sub

Example

[Create Normal Cut Feature (C#)](Create_Normal_Cut_Feature_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISMNormalCutFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
