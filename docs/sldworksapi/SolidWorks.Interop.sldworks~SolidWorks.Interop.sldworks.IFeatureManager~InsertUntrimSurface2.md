# InsertUntrimSurface2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertUntrimSurface2`

Extends a surface along its natural boundaries or fills interior surface holes, optionally trimming outside these boundaries or holes.
Extends a surface along its natural boundaries or fills interior surface holes, optionally trimming outside these boundaries or holes.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertUntrimSurface2( _
   ByVal FaceUntrimType As System.Integer, _
   ByVal EdgeUntrimType As System.Integer, _
   ByVal Distance As System.Double, _
   ByVal BMerge As System.Boolean, _
   ByVal BTrimOppositeSide As System.Boolean _
) As Feature
```

```

Dim instance As IFeatureManager
Dim FaceUntrimType As System.Integer
Dim EdgeUntrimType As System.Integer
Dim Distance As System.Double
Dim BMerge As System.Boolean
Dim BTrimOppositeSide As System.Boolean
Dim value As Feature
 
value = instance.InsertUntrimSurface2(FaceUntrimType, EdgeUntrimType, Distance, BMerge, BTrimOppositeSide)
```

```

Feature InsertUntrimSurface2( 
   System.int FaceUntrimType,
   System.int EdgeUntrimType,
   System.double Distance,
   System.bool BMerge,
   System.bool BTrimOppositeSide
)
```

```

Feature^ InsertUntrimSurface2( 
   System.int FaceUntrimType,
   System.int EdgeUntrimType,
   System.double Distance,
   System.bool BMerge,
   System.bool BTrimOppositeSide
) 
```

#### Parameters

*FaceUntrimType*
:   Untrim face edge type as defined by [swFaceUntrimType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFaceUntrimType_e.html); valid only if a face is selected

*EdgeUntrimType*
:   Connect endpoints or extend edges as defined by [swEdgeUntrimType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swEdgeUntrimType_e.html); valid only of one or more edges are selected

*Distance*
:   Distance by which to untrim the surface

*BMerge*
:   True to create a surface extension that merges with the original surface, false to create a new, separate surface body

*BTrimOppositeSide*
:   True to remove the surface outside the selected surface edges or interior surface holes, false to not; valid only if BMerge is false

#### Return Value

Pointer to the [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) object

Remarks

This method:

- is valid only for surface parts.
- requires preselection of the face or edges you want to untrim.

For learn more about Untrim Surfaces, see the **SOLIDWORKS Help > Parts and Features > Features > Surfaces > Surface Controls > Untrim Surface** topic.

Example

'VBA

'This example creates a planar polygonal surface, untrims (extends) the surface outside the selected face edges,  
'and trims (removes) the surface inside the selected face edges.  
'=======================================================================  
'Preconditions: Ensure that the specified template exists.  
'  
'Postconditions:  
'1. Creates **Surface-Plane1**.  
'2. Creates **Surface-Untrim1** by untrimming outside all edges of the selected face, not merging with the original part, and trimming inside all edges of the selected face.  
'3. Click on **Surface-Untrim1**. The untrimmed areas are in green.  
'========================================================================  
Dim swApp As SldWorks.SldWorks  
Dim Part As SldWorks.ModelDoc2  
Dim swPart As SldWorks.PartDoc  
Dim skSegment As SldWorks.SketchSegment  
Dim boolstatus As Boolean  
Dim longstatus As Long, longwarnings As Long

Sub main()

    Set swApp = Application.SldWorks  
   
    Dim swSheetWidth As Double  
    swSheetWidth = 0  
    Dim swSheetHeight As Double  
    swSheetHeight = 0  
    Set Part = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2024\templates\Part.prtdot", 0, swSheetWidth, swSheetHeight)  
    Set swPart = Part  
    Set Part = swApp.ActiveDoc  
    Part.SketchManager.InsertSketch True  
    boolstatus = Part.Extension.SelectByID2("Front Plane", "PLANE", -4.90383108306059E-02, 3.86835343160318E-02, 3.91373764799244E-03, False, 0, Nothing, 0)  
    Part.ClearSelection2 True  
    Set skSegment = Part.SketchManager.CreateLine(-0.035002, 0.035119, 0#, 0.025668, 0.036519, 0#)  
    Set skSegment = Part.SketchManager.CreateLine(0.025663, 0.036519, 0#, 0.025201, -0.016451, 0#)  
    Set skSegment = Part.SketchManager.CreateLine(0.025201, -0.016451, 0#, -0.068137, -0.018551, 0#)  
    Set skSegment = Part.SketchManager.CreateLine(-0.068137, -0.018551, 0#, -0.067204, 0.026718, 0#)  
    Set skSegment = Part.SketchManager.CreateLine(-0.067204, 0.026713, 0#, -0.036169, 0.026251, 0#)  
    Set skSegment = Part.SketchManager.CreateLine(-0.036169, 0.026251, 0#, -0.035002, 0.035119, 0#)  
    Part.ClearSelection2 True  
    Part.SketchManager.InsertSketch True  
    Part.SelectionManager.EnableContourSelection = True  
    boolstatus = Part.Extension.SelectByID2("Sketch1", "SKETCHREGION", 2.26345552080154E-02, -0.013184045043844, 0, True, 1, Nothing, 0)  
    boolstatus = Part.**InsertPlanarRefSurface**()  
    Part.ClearSelection2 True  
    boolstatus = Part.Extension.SelectByRay(-4.08355377464196E-02, 1.83176555033939E-02, 0, 0, 0, -1, 7.93376161930438E-04, 2, True, 0, 0)  
    Part.FeatureManager.**InsertUntrimSurface2** 0, 2, 0, False, True  
    Part.SelectionManager.EnableContourSelection = False

End Sub

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[ISurfaceExtendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData.md)
