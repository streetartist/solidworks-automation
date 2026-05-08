# IBaseFlangeFeatureData Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData`

Allows access to a sheet metal base flange feature.
Allows access to a sheet metal base flange feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IBaseFlangeFeatureData 
```

```

Dim instance As IBaseFlangeFeatureData
```

```

public interface IBaseFlangeFeatureData 
```

```

public interface class IBaseFlangeFeatureData 
```

Remarks

For general information about sheet metal base flanges, see the **SOLIDWORKS user-interface help > Sheet Metal > Using Sheet Metal Tools > Base Flange/Tab > Base Flange PropertyManager** topic.

Example

'VBA

'===========================================================  
'Preconditions:  
'1. Ensure the specified part template exists.  
'2. Open the Immediate window.  
'  
'Postconditions:  
'1. Creates a flange profile sketch.  
'2. Creates **Base-Flange1** in the FeatureManager design tree.  
'3. Inspect the Immediate window, graphics area,  
'   and FeatureManager design tree.  
'==================================================  
Dim swApp As SldWorks.SldWorks  
Dim Part As SldWorks.ModelDoc2  
Dim swPart As PartDoc  
Dim swModel As SldWorks.ModelDoc2  
Dim swSKFeat As SldWorks.Feature  
Dim skSegment As SldWorks.SketchSegment  
Dim swBaseFlangeFeat As SldWorks.BaseFlangeFeatureData  
Dim baseFlangeFeatData As SldWorks.BaseFlangeFeatureData  
Dim cba As SldWorks.CustomBendAllowance  
Dim var As Variant  
Dim parent As SldWorks.Feature  
Dim SHFeat As SldWorks.Feature  
Dim smFeatData As SldWorks.SheetMetalFeatureData  
Dim cba1 As SldWorks.CustomBendAllowance  
Dim boolstatus As Boolean  
Dim longstatus As Long, longwarnings As Long  
  
Option Explicit

Sub main()

    Set swApp = Application.SldWorks  
    Set Part = swApp.ActiveDoc

    Dim swSheetWidth As Double  
    swSheetWidth = 0  
    Dim swSheetHeight As Double  
    swSheetHeight = 0  
     
    Set Part = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2022\templates\Part.prtdot", 0, swSheetWidth, swSheetHeight)  
    Set swPart = Part  
    Set swModel = swApp.ActiveDoc  
     
    boolstatus = Part.Extension.SelectByID2("Top", "PLANE", -5.98881514598713E-02, 3.93749830258702E-02, 4.85137895479469E-03, False, 0, Nothing, 0)  
    Part.SketchManager.InsertSketch True  
    Part.ClearSelection2 True  
    
    Set skSegment = Part.SketchManager.CreateLine(-0.140779, 0.050824, 0#, -0.106481, -0.06735, 0#)  
    Set skSegment = Part.SketchManager.CreateLine(-0.106481, -0.06735, 0#, 0.084966, -0.049265, 0#)  
    Set skSegment = Part.SketchManager.CreateLine(0.084966, -0.049265, 0#, 0.143274, 0.063608, 0#)  
    Part.ClearSelection2 True  
    Part.SketchManager.InsertSketch True  
     
    Set swSKFeat = swModel.SelectionManager.GetSelectedObject6(1, -1)  
    Debug.Print "Flange profile name : " & swSKFeat.Name & " and type : " & swSKFeat.GetTypeName2  
     
    Set swBaseFlangeFeat = swModel.FeatureManager.**CreateDefinition**(swFmBaseFlange)  
   
    Set cba = swBaseFlangeFeat.**GetCustomBendAllowance**()  
     
    cba.**Type** = swBendAllowanceDirect  
    cba.**BendAllowance** = 0.05  
     
    swBaseFlangeFeat.**D1EndConditionType** = 1  
    swBaseFlangeFeat.**D1EndConditionDistance** = 0.02  
    swBaseFlangeFeat.**ReverseDirection** = True  
    swBaseFlangeFeat.**OffsetDirections** = 2  
    swBaseFlangeFeat.**D2EndConditionType** = 1  
    swBaseFlangeFeat.**D2EndConditionDistance** = 0.05  
    swBaseFlangeFeat.**OverrideDefaultSheetMetalParameters** = True  
    swBaseFlangeFeat.**Thickness** = 0.035  
  
    'Initialize the base flange feature  
    'Initialize(  
    'UseMaterialSheetMetalParameters=False,  
    'UseDefaultBendAllowance=False,  
    'CustomBendAllowance,  
    'UseDefaultBendRelief=False,  
    'ReliefType=swSheetMetalReliefTypes\_e.swSheetMetalReliefRectangular,  
    'UseReliefRatio=True,  
    'ReliefRatio=0.8m,  
    'ReliefWidth,  
    'ReliefDepth)

    Call swBaseFlangeFeat.**Initialize**(False, False, cba, False, swSheetMetalReliefRectangular, True, 0.8, 0#, 0#)  
     
    Set SHFeat = swModel.FeatureManager.**CreateFeature**(swBaseFlangeFeat)

    Set baseFlangeFeatData = SHFeat.**GetDefinition**()  
  
    Debug.Print "Use material sheet metal parameters? " & baseFlangeFeatData.**UseMaterialSheetMetalParameters**  
    Debug.Print "Use default bend allowance? " & baseFlangeFeatData.**UseDefaultBendAllowance**  
    Debug.Print "Use default bend relief? " & baseFlangeFeatData.**UseDefaultBendRelief**  
    Debug.Print "Use relief ratio? " & baseFlangeFeatData.**UseReliefRatio**  
    Debug.Print "Relief type as defined by swSheetMetalReliefTypes\_e: " & baseFlangeFeatData.**ReliefType**  
    Debug.Print "Relief width: " & baseFlangeFeatData.**ReliefWidth**  
    Debug.Print "Relief depth: " & baseFlangeFeatData.**ReliefDepth**  
    Debug.Print "Relief ratio: " & baseFlangeFeatData.**ReliefRatio**  
     
    'Modify the relief ratio and override default AutoRelief in the parent sheet metal feature  
    var = SHFeat.GetParents()  
    Set parent = var(1)  
    Debug.Print "Parent type: " & parent.GetTypeName2()

    Set smFeatData = parent.**GetDefinition**()

    Set cba1 = smFeatData.**GetCustomBendAllowance**()  
     
    Debug.Print "Custom bend allowance type as defined in swBendAllowanceTypes\_e: " & cba1.**Type**  
    Debug.Print "Bend allowance: " & cba1.**BendAllowance**  
    Debug.Print "Result code for override of AutoRelief as defined by swSheetMetalModifierError\_e: " & smFeatData.**SetOverrideDefaultParameter2**(swSheetMetalOverrideDefaultParameters\_AutoRelief, True)  
    smFeatData.**ReliefRatio** = 0.7  
     
    Debug.Print "Base flange successfully modified? " & parent.**ModifyDefinition**(smFeatData, swModel, Nothing)  
    Debug.Print "Base flange feature name : " & SHFeat.Name & " and type : " & SHFeat.GetTypeName2

End Sub

Example

[Get All Sheet Metal Feature Data (VBA)](Get_All_Sheet_Metal_Feature_Data_Example_VB.htm)  
[Get All Sheet Metal Feature Data (VB.NET)](Get_All_Sheet_Metal_Feature_Data_Example_VBNET.htm)  
[Get All Sheet Metal Feature Data (C#)](Get_All_Sheet_Metal_Feature_Data_Example_CSharp.htm)  
[Create Base Flange Feature (VB.NET)](Create_Base_Flange_Feature_Example_VBNET.htm)  
[Create Base Flange Feature (C#)](Create_Base_Flange_Feature_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBaseFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[ISheetMetalFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.md)
