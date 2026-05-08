# ICamFollowerMateFeatureData Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamFollowerMateFeatureData`

Allows access to a cam-follower mate feature.
Allows access to a cam-follower mate feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface ICamFollowerMateFeatureData 
```

```

Dim instance As ICamFollowerMateFeatureData
```

```

public interface ICamFollowerMateFeatureData 
```

```

public interface class ICamFollowerMateFeatureData 
```

Remarks

A cam-follower mate:

- Allows you to mate a cylinder, plane, or point on a cam-follower part to the tangent faces of a cam part.
- Appears in the FeatureManager design tree as either CamMateCoincident or CamMateTangent.

[IMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateFeatureData.md) is the parent of this mate interface.

To create a cam-follower mate:

1. Follow general instructions in the [IAssemblyDoc::CreateMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateMate.md) Remarks.
2. Specify [ICamFollowerMateFeatureData::EntitiesToMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamFollowerMateFeatureData~EntitiesToMate.md) for each EntityType or use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to pre-select the entities using Mark = 1 for the cam face and Mark = 8 for the cam-follower face or vertex.
3. Specify other properties of the CamFollowerMateFeatureData object.

To edit a cam-follower mate:

1. Access its feature and call [IFeature::GetDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDefinition.md) to get the MateFeatureData object.
2. Cast the MateFeatureData object to a CamFollowerMateFeatureData object.
3. Modify the CamFollowerMateFeatureData object.
4. Call [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.md).

To delete this cam-follower mate, use [IModelDocExtension::DeleteSelection2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteSelection2.md).

Example

'VBA

'\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
' 1. Open *public\_documents***\samples\tutorial\api\MechanicalMates\Cam-Follower.sldasm**.  
' 2. Delete **CamMateCoincident1** from the Mates folder in the FeatureManager design tree.  
' 3. Run the macro.  
' 4. Inspect the Mates folder in the FeatureManager design tree.  
' \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
Dim swApp As SldWorks.SldWorks  
Dim Part As SldWorks.ModelDoc2  
Dim boolstatus As Boolean  
  
Option Explicit

Sub main()

    Set swApp = Application.SldWorks  
    Set Part = swApp.ActiveDoc  
  
    boolstatus = Part.Extension.SelectByRay(-2.29201081452857E-03, 7.61655216381314E-02, 9.81125242168446E-03, -0.577381545199981, -0.577287712085548, -0.577381545199979, 2.88013169157359E-03, 2, True, 1, 0)  
    boolstatus = Part.Extension.SelectByRay(0, 0.0762, 0, -0.577381545199981, -0.577287712085548, -0.577381545199979, 2.88013169157359E-03, 3, True, 8, 0)  
  
    ' Create CamFollowerMateFeatureData  
    Dim MateData As SldWorks.CamFollowerMateFeatureData  
    Set MateData = Part.**CreateMateData**(9)  
  
    ' Set the Entities To Mate  
    Dim FirstEntityToMate As Object  
    Dim SecondEntityToMate As Object  
    Set FirstEntityToMate = Part.SelectionManager.GetSelectedObject6(1, -1)  
    MateData.**EntitiesToMate**(0) = FirstEntityToMate  
    Set SecondEntityToMate = Part.SelectionManager.GetSelectedObject6(2, -1)  
    MateData.**EntitiesToMate**(1) = SecondEntityToMate  
  
    ' Set the Mate Alignment  
    MateData.MateAlignment = 2  
  
    ' Create the mate  
    Dim MateFeature As SldWorks.Feature  
    Set MateFeature = Part.**CreateMate**(MateData)  
    Part.ClearSelection2 True  
    Part.EditRebuild3

End Sub

Example

[Create a Cam-Follower Mate (C#)](Create_Cam_Follower_Mate_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICamFollowerMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamFollowerMateFeatureData_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
