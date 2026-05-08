# IMateControllerFeatureData Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData`

Allows access to a mate controller feature.
Allows access to a mate controller feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IMateControllerFeatureData 
```

```

Dim instance As IMateControllerFeatureData
```

```

public interface IMateControllerFeatureData 
```

```

public interface class IMateControllerFeatureData 
```

Remarks

To create a mate controller feature:

- Use IAssemblyDoc::IsSupportedMatesAvailable to determine whether supportive mates exist for the assembly.

If true:

1. Call [IAssemblyDoc::CollectAllSupportiveMates](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CollectAllSupportiveMates.md).
2. Pre-select the supportive mates to use to create the mate controller. Or call [IMateControllerFeatureData::Initialize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData~Initialize.md), passing in the supportive mates. Mates passed into the Initialize method are given precedence over pre-selected mates. The array passed in must contain IDispatch objects.
3. Call [IFeatureManager::CreateDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateDefinition.md) to create an IMateControllerFeatureData object.
4. Call [IMateControllerFeatureData::AddNewPosition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData~AddNewPosition.md) to add a new mate position to the mate controller.
5. Call [IMateControllerFeatureData::SetValues](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData~SetValues.md) to set the values for all mates in a given mate position. If values are not specified or invalid values are specified, then the mate controller feature is created with default mate values (i.e., values used when the mate was created).
6. Call [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.md), passing in the IMateControllerFeatureData object.
7. Call [IFeatureManager::GetCreateFeatureErrors](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~GetCreateFeatureErrors.md).

To edit a mate controller feature, call:

1. [IFeature::GetDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDefinition.md)
2. [IMateControllerFeatureData::AccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData~AccessSelections.md)
3. [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.md)
4. [IMateControllerFeatureData::ReleaseSelectionAccess](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData~ReleaseSelectionAccess.md)

For more information about the Mate Controller feature, see the **SOLIDWORKS user-interface help > Assemblies > Mates > Mate Controller** topic.

Example

'VBA

'======================================================================================  
' Preconditions: Open an assembly document that contains a mechanical slot feature  
' with a slot mate that has one of these constraints:  
'    - Distance Along Slot  
'    - Percent Along Slot  
'  
' Postconditions:  
' 1. **Mate Controller (Position 3)** is added to the FeatureManager design tree.  
' 2. Inspect the graphics area.  
'  
' =====================================================================================  
Dim swApp As SldWorks.SldWorks

Dim Part As SldWorks.ModelDoc2  
Dim Assem As SldWorks.AssemblyDoc  
Dim boolstatus As Boolean

Option Explicit

Sub main()

    Set swApp = Application.SldWorks  
     
    Set Part = swApp.ActiveDoc  
    Set Assem = Part  
     
    Dim myModelView As Object  
    Set myModelView = Part.ActiveView  
    myModelView.FrameState = swWindowState\_e.swWindowMaximized  
    Part.ClearSelection2 True  
     
    boolstatus = Assem.**IsSupportedMatesAvailable**  
     
    Dim var As Variant  
    var = Assem.**CollectAllSupportiveMates**  
     
    Dim featMgr As SldWorks.FeatureManager  
    Set featMgr = Part.FeatureManager  
     
    Dim mateControllerObj As SldWorks.MateControllerFeatureData  
    Set mateControllerObj = featMgr.**CreateDefinition**(swFmMateController)  
     
    Call mateControllerObj.**Initialize**(var)  
     
    mateControllerObj.**AddNewPosition** ("Position1")  
    mateControllerObj.**AddNewPosition** ("Position2")  
    mateControllerObj.**AddNewPosition** ("Position3")  
     
    Dim position2ValArr(0) As Double  
    position2ValArr(0) = 0.0375  
     
    Call mateControllerObj.**SetValues**("Position2", position2ValArr)  
     
    Dim position3ValArr(0) As Double  
    position3ValArr(0) = 0.0625  
     
    Call mateControllerObj.**SetValues**("Position3", position3ValArr)  
     
    Dim mateContFeat As SldWorks.Feature  
    Set mateContFeat = featMgr.**CreateFeature**(mateControllerObj)  
     
    Dim mcObj2 As SldWorks.MateControllerFeatureData  
    Set mcObj2 = mateContFeat.**GetDefinition**()  
     
    Dim var1 As Variant  
    var1 = mcObj2.**Mates**  
     
    Dim position2ValArr2(0) As Double  
    position2ValArr2(0) = 0.015  
     
    Call mcObj2.**SetValues**("Position2", position2ValArr2)  
     
    Dim position3ValArr2(0) As Double  
    position3ValArr2(0) = 0.085  
     
    Call mcObj2.**SetValues**("Position3", position3ValArr2)  
     
    mateContFeat.**ModifyDefinition** mcObj2, Part, Nothing

End Sub

Example

[Create Mate Controller (VB.NET)](Create_Mate_Controller_Example_VBNET.htm)  
[Create Mate Controller (C#)](Create_Mate_Controller_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMateControllerFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
