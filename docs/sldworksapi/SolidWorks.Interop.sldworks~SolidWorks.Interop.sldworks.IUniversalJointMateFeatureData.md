# IUniversalJointMateFeatureData Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUniversalJointMateFeatureData`

Allows access to a universal joint mate feature.
Allows access to a universal joint mate feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IUniversalJointMateFeatureData 
```

```

Dim instance As IUniversalJointMateFeatureData
```

```

public interface IUniversalJointMateFeatureData 
```

```

public interface class IUniversalJointMateFeatureData 
```

Remarks

A universal joint (U-joint) mate consists of two components where the rotation of one component (the output shaft) about its axis is driven by the rotation of another component (the input shaft) about its axis. An example would be the U-joint between the transmission and the rear drive axle of an automobile.

[IMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateFeatureData.md) is the parent of this mate interface.

To create a universal joint mate:

1. Follow general instructions in the [IAssemblyDoc::CreateMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateMate.md) Remarks.
2. Specify [IUniversalJointMateFeatureData::EntitiesToMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUniversalJointMateFeatureData~EntitiesToMate.md) or use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to pre-select the entities using Mark = 1.
3. Set [IUniversalJointMateFeatureData::DefineJointPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUniversalJointMateFeatureData~DefineJointPoint.md) to true and specify [IUniversalJointMateFeatureData::JointPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUniversalJointMateFeatureData~JointPoint.md) or use IModelDocExtension::SelectByID2 to pre-select the joint point using Mark = 16384.
4. Specify other properties of the UniversalJointMateFeatureData object as required.

To edit a universal joint mate:

1. Access its feature and call [IFeature::GetDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDefinition.md) to get the MateFeatureData object.
2. Cast the MateFeatureData object to a UniversalJointMateFeatureData object.
3. Modify the UniversalJointMateFeatureData object.
4. Call [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.md).

To delete this universal joint mate, use [IModelDocExtension::DeleteSelection2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteSelection2.md).

Example

'VBA  
' \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
' 1. Open *public\_documents***\samples\tutorial\api\MechanicalMates\Universal Joint.sldasm**.  
' 2. Run the macro.  
' 3. Inspect the Mates folder of the FeatureManager design tree.  
' \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
Dim swApp As SldWorks.SldWorks  
Dim Part As SldWorks.ModelDoc2  
Dim boolstatus As Boolean  
Option Explicit

Sub main()

> Set swApp = Application.SldWorks  
> Set Part = swApp.ActiveDoc  
>   
> boolstatus = Part.Extension.SelectByRay(1.88633351534122E-02, 2.88569103901466E-02, 5.46569039595397E-02, -0.879159305813743, -0.399683188478405, -0.259484611969252, 7.73012265648448E-04, 2, True, 1, 0)  
> boolstatus = Part.Extension.SelectByRay(1.86671108039604E-02, 7.47386637118552E-02, 4.19001939717987E-02, -0.879159305813743, -0.399683188478405, -0.259484611969252, 7.73012265648448E-04, 2, True, 1, 0)  
>   
> ' Create UniversalJointMateFeatureData  
> Dim MateData As SldWorks.UniversalJointMateFeatureData  
> Set MateData = Part.**CreateMateData**(19)  
>   
> ' Set the Entities To Mate  
> Dim EntitiesToMate(1) As Object  
> Set EntitiesToMate(0) = Part.SelectionManager.GetSelectedObject6(1, -1)  
> Set EntitiesToMate(1) = Part.SelectionManager.GetSelectedObject6(2, -1)  
> Dim EntitiesToMateVar As Variant  
> EntitiesToMateVar = EntitiesToMate  
> MateData.**EntitiesToMate** = (EntitiesToMateVar)  
>   
> ' Set the Mate DefineJointPoint  
> MateData.**DefineJointPoint** = False  
>   
> ' Create the mate  
> Dim MateFeature As SldWorks.Feature  
> Set MateFeature = Part.**CreateMate**(MateData)  
> Part.ClearSelection2 True  
> Part.EditRebuild3

End Sub

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IUniversalJointMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUniversalJointMateFeatureData_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
