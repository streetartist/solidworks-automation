# OverrideValue Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData~OverrideValue`

Gets whether the bend angle of this sketched bend is overridden by a custom bend angle.
Gets whether the bend angle of this sketched bend is overridden by a custom bend angle.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property OverrideValue As System.Boolean
```

```

Dim instance As ISketchedBendFeatureData
Dim value As System.Boolean
 
value = instance.OverrideValue
```

```

System.bool OverrideValue {get;}
```

```

property System.bool OverrideValue {
   System.bool get();
}
```

#### Property Value

True if the bend angle is overridden by a custom bend angle, false if the bend angle is from a gauge table

Remarks

This property:

- is valid only when a sheet metal gauge table has been selected for a parent sheet metal feature (e.g., lofted bend, swept flange, or base flange).
- cannot be set. Rather, it is calculated from the bend angle value. If the bend angle is in the gauge table, then this property is set to false. If the bend angle is not in the gauge table, then it is considered a custom value, and this property is set to true.

Example

'VBA  
'==========================================================================  
'This example demonstrates how setting BendAngle influences the read-only OverrideValue property.  
'  
'Preconditions:  
'1. Ensure the specified paths exist.  
'2. Open an Immediate window.  
'  
'Postconditions:  
'1. A part with **Sheet-Metal**, **Base-Flange1**, and **Sketched Bend1** features is created.  
'2. Inspect the Immediate window.  
'=============================================================================

Dim swApp As SldWorks.SldWorks  
Dim Part As SldWorks.ModelDoc2  
Dim swPart As SldWorks.PartDoc  
Dim myModelView As SldWorks.ModelView  
Dim vSkLines As Variant  
Dim swFeat As SldWorks.Feature  
Dim swFeatMgr As SldWorks.FeatureManager  
Dim customBendAllowanceData As SldWorks.CustomBendAllowance  
Dim skSegment As SldWorks.SketchSegment  
Dim CBAObject As SldWorks.CustomBendAllowance  
Dim myFeature As SldWorks.Feature  
Dim swFeatData As SldWorks.BaseFlangeFeatureData  
Dim skBendFeatData As SldWorks.SketchedBendFeatureData  
Dim myFeatData As SldWorks.SketchedBendFeatureData  
Dim boolstatus As Boolean  
Dim longstatus As Long, longwarnings As Long  
Dim swSheetWidth As Double  
Dim swSheetHeight As Double  
Option Explicit  
Sub main()

    Set swApp = Application.SldWorks  
     
    swSheetWidth = 0  
    swSheetHeight = 0  
    Set Part = swApp.NewDocument("D:\Program Files\SOLIDWORKS Corp\SOLIDWORKS (2)\DATA\Templates\Part.prtdot", 0, swSheetWidth, swSheetHeight)  
     
    Set swPart = Part  
    swApp.ActivateDoc2 "Part2", False, longstatus  
    Set Part = swApp.ActiveDoc  
     
    Set myModelView = Part.ActiveView  
    myModelView.FrameState = swWindowState\_e.swWindowMaximized  
    boolstatus = Part.Extension.SelectByID2("Front Plane", "PLANE", -6.40395151030158E-02, 5.21578791231543E-02, 4.49083628119237E-03, False, 0, Nothing, 0)  
    Part.SketchManager.InsertSketch True  
    Part.ClearSelection2 True  
    boolstatus = Part.Extension.SelectByID2("Front Plane", "PLANE", -2.96114446516235E-02, 3.44357811398094E-02, 0, False, 0, Nothing, 0)  
    Part.ClearSelection2 True  
    boolstatus = Part.Extension.SetUserPreferenceToggle(swUserPreferenceToggle\_e.swSketchAddConstToRectEntity, swUserPreferenceOption\_e.swDetailingNoOptionSpecified, False)  
    boolstatus = Part.Extension.SetUserPreferenceToggle(swUserPreferenceToggle\_e.swSketchAddConstLineDiagonalType, swUserPreferenceOption\_e.swDetailingNoOptionSpecified, True)  
     
    vSkLines = Part.SketchManager.CreateCornerRectangle(-5.22359192169088E-02, 3.27722168335384E-02, 0, 0.077854809533482, -4.14227512261475E-02, 0)  
    Part.ClearSelection2 True  
    Part.SketchManager.InsertSketch True

    Part.ShowNamedView2 "\*Trimetric", 8  
    Part.ViewZoomtofit2  
    Part.SketchManager.InsertSketch True  
    Part.CloseFamilyTable  
    Set myModelView = Part.ActiveView  
    myModelView.FrameState = swWindowState\_e.swWindowMaximized  
    Set myModelView = Part.ActiveView  
    myModelView.FrameState = swWindowState\_e.swWindowMaximized  
    Set myModelView = Part.ActiveView  
    myModelView.FrameState = swWindowState\_e.swWindowMaximized  
    Set myModelView = Part.ActiveView  
    myModelView.FrameState = swWindowState\_e.swWindowMaximized  
    Set myModelView = Part.ActiveView  
    myModelView.FrameState = swWindowState\_e.swWindowMaximized  
    Set myModelView = Part.ActiveView  
    myModelView.FrameState = swWindowState\_e.swWindowMaximized  
    Set myModelView = Part.ActiveView  
    myModelView.FrameState = swWindowState\_e.swWindowMaximized  
    Part.CloseFamilyTable  
     
    Set customBendAllowanceData = Part.FeatureManager.CreateCustomBendAllowance()  
     
    Set swFeatMgr = Part.FeatureManager

    'Create a sheet metal base flange  
     
    Set swFeatData = swFeatMgr.**CreateDefinition**(swFeatureNameID\_e.swFmBaseFlange)  
    swFeatData.**Initialize** False, True, customBendAllowanceData, True, 1, True, 0.5, 0.0001, 0.0001  
    swFeatData.**BendRadius** = 0.00635  
    swFeatData.**D1EndConditionDistance** = 0.02  
    swFeatData.**D1EndConditionType** = 1  
    swFeatData.**D1ReverseOffset** = False  
    swFeatData.**D2EndConditionDistance** = 0.01  
    swFeatData.**D2EndConditionType** = 1  
    swFeatData.**D2ReverseOffset** = False  
    swFeatData.**OffsetDirections** = 1  
    swFeatData.**ReverseDirection** = False  
    swFeatData.**ReverseThickness** = False  
    swFeatData.**Thickness** = 0.00531368  
    swFeatData.**UseGaugeTable** = True  
    swFeatData.**GaugeTablePath** = "D:\Program Files\SOLIDWORKS Corp\SOLIDWORKS (2)\lang\english\Sheet Metal Gauge Tables\bend allowance mm sample.xlsx"  
    Set swFeat = swFeatMgr.**CreateFeature**(swFeatData)  
    Part.ClearSelection2 True  
    Set myModelView = Part.ActiveView  
    myModelView.FrameState = swWindowState\_e.swWindowMaximized  
    Set myModelView = Part.ActiveView  
    myModelView.FrameState = swWindowState\_e.swWindowMaximized

    Part.GraphicsRedraw2  
    boolstatus = Part.Extension.SelectByRay(-1.81805886692246E-02, 2.58328472214089E-02, 0, -0.400036026779312, -0.515038074910024, -0.758094294050284, 1.07315913654528E-03, 2, False, 0, 0)  
    Part.SketchManager.InsertSketch True  
    Part.ClearSelection2 True  
    boolstatus = Part.Extension.SelectByRay(-3.71158985098665E-02, 2.32231794094294E-02, 0, 0, 0, -1, 6.76279555664225E-04, 2, False, 0, 0)  
    Part.ClearSelection2 True  
     
    Set skSegment = Part.SketchManager.CreateLine(-0.007678, 0.057833, 0#, -0.059393, -0.042615, 0#)  
    Part.ClearSelection2 True  
    Part.SketchManager.InsertSketch True  
    Part.SketchManager.InsertSketch True  
    boolstatus = Part.Extension.SelectByRay(-3.97811503331896E-03, 1.40228554924494E-02, 0, 0, 0, -1, 6.76279555664225E-04, 2, True, 0, 0)

    'Create a sheet metal sketched bend

    Set skBendFeatData = Part.FeatureManager.**CreateDefinition**(swFmSketchBend)  
     
    skBendFeatData.**BendAngle** = 1.6  
    skBendFeatData.**UseDefaultBendRadius** = False  
    skBendFeatData.**BendRadius** = 0.001  
    skBendFeatData.**ReverseDirection** = False

    Set CBAObject = skBendFeatData.**GetCustomBendAllowance**()  
    CBAObject.**BendAllowance** = 0.003  
    Call skBendFeatData.**SetCustomBendAllowance**(CBAObject)  
     
    Set myFeature = Part.FeatureManager.**CreateFeature**(skBendFeatData)  
     
    'Modify feature  
    Set myFeatData = myFeature.**GetDefinition**()  
     
    'Is the bend angle overridden?  
    Debug.Print "Bend angle is overridden? " & myFeatData.**OverrideValue**  
    'If OverrideValue is true, then the bend angle is a custom value not in the current gauge table  
     
    'Set a new value for bend angle in radians  
    myFeatData.**BendAngle** = 1.5707963267949  
     
    boolstatus = myFeature.**ModifyDefinition**(myFeatData, Part, Nothing)  
     
    Set myFeatData = myFeature.**GetDefinition**()  
     
    'Is the bend angle in the gauge table or is it overridden?  
    Debug.Print "Bend angle is overridden? " & myFeatData.**OverrideValue**  
    'If OverrideValue is false, then the bend angle is in the current gauge table

End Sub

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchedBendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData.md)  
[ISketchedBendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData_members.md)  
[ISketchedBendFeatureData::BendAngle Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData~BendAngle.md)
