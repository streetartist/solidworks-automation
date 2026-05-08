# IEdgeFlangeFeatureData Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData`

Allows access to a sheet metal edge flange feature.
Allows access to a sheet metal edge flange feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IEdgeFlangeFeatureData 
```

```

Dim instance As IEdgeFlangeFeatureData
```

```

public interface IEdgeFlangeFeatureData 
```

```

public interface class IEdgeFlangeFeatureData 
```

Remarks

For more information, see the **SOLIDWORKS user-interface help > Sheet Metal > Using Sheet Metal Tools > Edge Flanges > Edge-Flange PropertyManager** topic.

Example

'VBA

'-----------------------------------------------------  
' Preconditions: Open *install\_dir**\*****samples\tutorial\sheetmetal\formtools\cover.sldprt**.  
'  
' Postconditions: Creates **Edge-Flange1** in the FeatureManager design tree.  
'------------------------------------------------------

Option Explicit

Sub main()

    Dim swApp As SldWorks.SldWorks  
    Dim swModel          As SldWorks.ModelDoc2  
    Dim bValue           As Boolean  
    Dim swEdge           As SldWorks.Edge  
    Dim dAngle           As Double  
    Dim dLength          As Double  
    Dim swFeature        As SldWorks.Feature  
    Dim swEntity         As SldWorks.Entity  
    Dim swSketch         As SldWorks.Sketch  
    Dim vSketchSegments  As Variant  
    Dim swSketchLine     As SldWorks.SketchLine  
    Dim swStartPoint     As SldWorks.SketchPoint  
    Dim swEndPoint       As SldWorks.SketchPoint  
    Dim dSize            As Double  
    Dim dFactor1         As Double  
    Dim dFactor2         As Double  
    Dim aFlangeEdges(0)  As SldWorks.Edge  
    Dim vFlangeEdges     As Variant  
    Dim aSketchFeats(0)  As SldWorks.Sketch  
    Dim vSketchFeats     As Variant  
    Dim FeatData         As EdgeFlangeFeatureData  
    Dim edgeFlangeFeat   As SldWorks.Feature  
    Dim PBendData As SldWorks.CustomBendAllowance

    Set swApp = Application.SldWorks  
    Set swModel = swApp.ActiveDoc

    ' Flange angle  
    dAngle = (90# / 180#) \* 3.1415926535897  
  
    ' Flange length  
    dLength = 0.02

    swModel.ShowNamedView2 "\*Back", -1  
    swModel.ViewZoomtofit2

    ' Select edge  
    bValue = swModel.Extension.SelectByRay(3.53852695288734E-02, 5.27495553160953E-02, 4.85267999999905E-02, 0, 0, 1, 2.83299018635423E-04, 1, False, 0, 0)  
    Set swEdge = swModel.SelectionManager.GetSelectedObject6(1, -1)

    ' Insert a sketch of the edge flange  
    Set swFeature = swModel.**InsertSketchForEdgeFlange**(swEdge, dAngle, False)  
    bValue = swFeature.Select2(False, 0)

    swModel.EditSketch  
    Set swSketch = swModel.GetActiveSketch2

    Set swEntity = swEdge

    ' Select edge  
    bValue = swEntity.Select4(False, Nothing)

    ' Use the edge in the sketch  
    bValue = swModel.SketchManager.SketchUseEdge(False)

    ' Get the created sketch line  
    vSketchSegments = swSketch.GetSketchSegments  
    Set swSketchLine = vSketchSegments(0)

    ' Get start and end point  
    Set swStartPoint = swSketchLine.GetStartPoint2  
    Set swEndPoint = swSketchLine.GetEndPoint2

    ' Create additional lines to define sketch

    ' Set parameters defining the sketch geometry

    dSize = swEndPoint.X - swStartPoint.X  
    dFactor1 = 0.1  
    dFactor2 = 1.25

    ' Add directly and do not display to speed things up  
    swModel.SetAddToDB True  
    swModel.SetDisplayWhenAdded False

    swModel.CreateLine2 swStartPoint.X, swStartPoint.Y, 0#, swStartPoint.X, swStartPoint.Y + dLength, 0#  
    swModel.CreateLine2 swStartPoint.X, swStartPoint.Y + dLength, 0#, swStartPoint.X + dFactor1 \* dSize, swStartPoint.Y + dFactor2 \* dLength, 0#  
    swModel.CreateLine2 swStartPoint.X + dFactor1 \* dSize, swStartPoint.Y + dFactor2 \* dLength, 0#, swEndPoint.X - dFactor1 \* dSize, swStartPoint.Y + dFactor2 \* dLength, 0#  
    swModel.CreateLine2 swEndPoint.X - dFactor1 \* dSize, swStartPoint.Y + dFactor2 \* dLength, 0#, swEndPoint.X, swEndPoint.Y + dLength, 0#  
    swModel.CreateLine2 swEndPoint.X, swEndPoint.Y, 0#, swEndPoint.X, swEndPoint.Y + dLength, 0#

    swModel.SetDisplayWhenAdded True  
    swModel.SetAddToDB False

    ' Commit changes made to the sketch  
    swModel.InsertSketch2 True

    ' Insert the edge flange

    Set aFlangeEdges(0) = swEdge  
    Set aSketchFeats(0) = swSketch

    vFlangeEdges = aFlangeEdges  
    vSketchFeats = aSketchFeats

    Set FeatData = swModel.FeatureManager.**CreateDefinition**(swFmEdgeFlange)  
     
    Call FeatData.**AddEdges**(vFlangeEdges, vSketchFeats)  
    FeatData.**UseDefaultBendRadius** = False  
    FeatData.**BendRadius** = 0.0007366  
    FeatData.**GapDistance** = 0.001  
    FeatData.**BendAngle** = dAngle  
    FeatData.**LockAngle** = True  
    FeatData.**OffsetType** = swFlangeOffsetBlind  
    FeatData.**OffsetDistance** = dLength  
    FeatData.**OffsetDimType** = swFlangeDimTypeInnerVirtualSharp  
    FeatData.**PositionType** = swFlangePositionTypeMaterialInside  
    FeatData.**UsePositionOffset** = True  
    FeatData.**PositionOffsetType** = swFlangeOffsetBlind  
    FeatData.**PositionOffsetDistance** = 0.01  
    FeatData.**UseDefaultBendAllowance** = False  
    Set PBendData = FeatData.**GetCustomBendAllowance**  
    PBendData.**KFactor** = 0.5  
    PBendData.**Type** = swBendAllowanceDeduction  
    FeatData.**SetCustomBendAllowance** PBendData  
    FeatData.**UseDefaultBendRelief** = False  
    FeatData.**UseReliefRatio** = True  
    FeatData.**ReliefRatio** = 0.5  
    FeatData.**AutoReliefType** = swSheetMetalReliefTear  
    FeatData.**ReliefTearType** = swReliefTearTypeRip  
   
    Set edgeFlangeFeat = swModel.FeatureManager.**CreateFeature**(FeatData)

End Sub

Example

[Create Edge Flange (VB.NET)](Create_Edge_Flange_Example_VBNET.htm)  
[Create Edge Flange (C#)](Create_Edge_Flange_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEdgeFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
