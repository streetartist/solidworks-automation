# ISweptFlangeFeatureData Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData`

Allows access to a sheet metal swept flange feature.
Allows access to a sheet metal swept flange feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface ISweptFlangeFeatureData 
```

```

Dim instance As ISweptFlangeFeatureData
```

```

public interface ISweptFlangeFeatureData 
```

```

public interface class ISweptFlangeFeatureData 
```

Remarks

For more information about swept flanges, read the **SOLIDWORKS Help > Sheet Metal > Using Sheet Metal Tools > Swept Flange > Swept Flange PropertyManager** topic.

Example

'VBA

'Preconditions: Ensure that the specified part template exists.

'Postconditions:

'1. **Base-Flange1** and **Swept Flange1** are created.  
'2. Inspect the graphics area and the FeatureManager design tree.

'================================================

Dim swApp As SldWorks.SldWorks  
Dim swFeat As SldWorks.Feature  
Dim myFeature As SldWorks.Feature  
Dim swFeatMgr As SldWorks.FeatureManager  
Dim swFeatData As SldWorks.SweptFlangeFeatureData  
Dim customBendAllowanceData As SldWorks.CustomBendAllowance  
Dim swProfileSketch As SldWorks.Feature  
Dim skSegment As SldWorks.SketchSegment  
Dim Part As SldWorks.ModelDoc2  
Dim swPart As PartDoc  
Dim boolstatus As Boolean  
Dim longstatus As Long  
  
Option Explicit  
  
Sub main()

    Set swApp = Application.SldWorks  
        
    Dim swSheetWidth As Double  
    swSheetWidth = 0  
    Dim swSheetHeight As Double  
    swSheetHeight = 0  
    Set Part = swApp.NewDocument("C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\Tutorial\part.prtdot", 0, swSheetWidth, swSheetHeight)  
     
    Set swPart = Part  
    swApp.ActivateDoc2 "Part1", False, longstatus  
    Set Part = swApp.ActiveDoc  
     
    Part.SketchManager.InsertSketch True  
    boolstatus = Part.Extension.SelectByID2("Front", "PLANE", -3.50345417518034E-02, 0.019677523162802, 5.11863136830445E-03, False, 0, Nothing, 0)  
    Part.ClearSelection2 True  
    boolstatus = Part.Extension.SetUserPreferenceToggle(swUserPreferenceToggle\_e.swSketchAddConstToRectEntity, swUserPreferenceOption\_e.swDetailingNoOptionSpecified, False)  
    boolstatus = Part.Extension.SetUserPreferenceToggle(swUserPreferenceToggle\_e.swSketchAddConstLineDiagonalType, swUserPreferenceOption\_e.swDetailingNoOptionSpecified, True)  
    Dim vSkLines As Variant  
    vSkLines = Part.SketchManager.CreateCornerRectangle(-4.20403557341645E-02, 2.75066828701494E-02, 0, 4.75026757367474E-02, -2.20443628675665E-02, 0)  
    Part.ClearSelection2 True

    Part.ShowNamedView2 "\*Trimetric", 8  
    Part.ViewZoomtofit2  
     
    Set customBendAllowanceData = Part.FeatureManager.CreateCustomBendAllowance()  
    customBendAllowanceData.KFactor = 0.5  
     
    Set myFeature = Part.FeatureManager.InsertSheetMetalBaseFlange2(0.0007366, False, 0.0007366, 0.02, 0.01, False, 0, 0, 1, customBendAllowanceData, False, 0, 0.0001, 0.0001, 0.5, True, False, True, True)  
     
    Part.ClearSelection2 True  
    Part.SketchManager.InsertSketch True  
    boolstatus = Part.Extension.SelectByID2("", "FACE", 4.41584745988735E-02, 2.75066828701256E-02, -2.52375262334681E-04, True, 0, Nothing, 0)  
     
    Set skSegment = Part.SketchManager.CreateLine(0.047503, 0#, 0#, 0.047503, -0.015713, 0#)  
    Part.ClearSelection2 True  
    Part.SketchManager.InsertSketch True  
     
    boolstatus = Part.Extension.SelectByID2("Sketch6", "SKETCH", 2.54585357375204E-02, -3.78791126417555E-03, -0.013876316631307, True, 0, Nothing, 0)  
    boolstatus = Part.Extension.SelectByRay(4.72949686339916E-02, 1.33307046879168E-02, 2.07707102561017E-04, -0.499999999999997, -0.707106781186554, -0.499999999999995, 4.23592175091009E-04, 1, True, 0, 0)  
    Part.ClearSelection2 True  
     
    boolstatus = Part.Extension.SelectByID2("Sketch6", "SKETCH", 2.54585357375204E-02, -3.78791126417555E-03, -0.013876316631307, True, 0, Nothing, 0)  
    Set swProfileSketch = Part.SelectionManager.GetSelectedObject6(1, -1)  
    Part.ClearSelection2 True  
     
    Dim swPathObj As Object  
    Dim pathObjsArray(0) As Object  
    boolstatus = Part.Extension.SelectByRay(4.72949686339916E-02, 1.33307046879168E-02, 2.07707102561017E-04, -0.499999999999997, -0.707106781186554, -0.499999999999995, 4.23592175091009E-04, 1, True, 0, 0)  
    Set swPathObj = Part.SelectionManager.GetSelectedObject6(1, -1)  
    Set pathObjsArray(0) = swPathObj  
    Dim pathObjsVar As Variant  
    pathObjsVar = pathObjsArray  
    Part.ClearSelection2 True  
    
    Set swFeatMgr = Part.FeatureManager  
    
    Set swFeatData = swFeatMgr.**CreateDefinition**(swFeatureNameID\_e.swFmSweptFlange)  
    swFeatData.**EndOffset** = 0  
    swFeatData.**FlangePosition** = swSweptFlangePositionType\_MaterialInside  
    swFeatData.**FlattenAlongPath** = False  
    swFeatData.**OverrideDefaultSheetMetalParameters** = False  
    swFeatData.**Path** = pathObjsVar  
    swFeatData.**Profile** = swProfileSketch  
    swFeatData.**ReverseDirection** = False  
    swFeatData.**StartOffset** = 0  
    swFeatData.**TrimSideBends** = False  
    swFeatData.**UseDefaultBendAllowance** = True  
    swFeatData.**UseDefaultBendRelief** = True  
    swFeatData.**UseDefaultRadius** = False  
    swFeatData.**UseGaugeTable** = False  
    swFeatData.**UseMaterialSheetMetalParameters** = False  
    Set swFeat = swFeatMgr.**CreateFeature**(swFeatData)  
    Part.ClearSelection2 True  
     
End Sub

Example

[Create Swept Flange (VB.NET)](Create_Swept_Flange_Example_VBNET.htm)  
[Create Swept Flange (C#)](Create_Swept_Flange_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISweptFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[ISheetMetalGaugeTableParameters Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters.md)
