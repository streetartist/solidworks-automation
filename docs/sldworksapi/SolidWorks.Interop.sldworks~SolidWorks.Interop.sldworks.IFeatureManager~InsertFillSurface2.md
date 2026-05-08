# InsertFillSurface2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertFillSurface2`

Inserts a fill-surface feature in the model.
Inserts a fill-surface feature in the model.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertFillSurface2( _
   ByVal Resolutions As System.Integer, _
   ByVal Options As System.Integer, _
   ByVal VPatchBoundaries As System.Object, _
   ByVal VCurvatureControlType As System.Object, _
   ByVal VFaces As System.Object, _
   ByVal VConstraintCurves As System.Object _
) As Feature
```

```

Dim instance As IFeatureManager
Dim Resolutions As System.Integer
Dim Options As System.Integer
Dim VPatchBoundaries As System.Object
Dim VCurvatureControlType As System.Object
Dim VFaces As System.Object
Dim VConstraintCurves As System.Object
Dim value As Feature
 
value = instance.InsertFillSurface2(Resolutions, Options, VPatchBoundaries, VCurvatureControlType, VFaces, VConstraintCurves)
```

```

Feature InsertFillSurface2( 
   System.int Resolutions,
   System.int Options,
   System.object VPatchBoundaries,
   System.object VCurvatureControlType,
   System.object VFaces,
   System.object VConstraintCurves
)
```

```

Feature^ InsertFillSurface2( 
   System.int Resolutions,
   System.int Options,
   System.Object^ VPatchBoundaries,
   System.Object^ VCurvatureControlType,
   System.Object^ VFaces,
   System.Object^ VConstraintCurves
) 
```

#### Parameters

*Resolutions*
:   Controls the resolution or quality of the surface (see **Remarks**)

*Options*
:   Options as defined in [swFeatureFillSurfaceOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFillSurfaceOptions_e.html)

*VPatchBoundaries*
:   Array of [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) or [sketches](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md) for the patch boundaries

*VCurvatureControlType*
:   Array of curve control methods as defined in [swContactType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swContactType_e.html)

*VFaces*
:   Array of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) to use for direction

*VConstraintCurves*
:   Array of constraint curves ([edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) or [sketches](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md))

#### Return Value

Pointer to the [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) object

Remarks

You must use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) and the following Mark values to select edges that bound the surface to be filled:

- Boundary curves = 1
- Boundary with contact curvature control = 257
- Boundary with tangent curvature control = 513
- Constraint curves or internal curves = 4

The resolution argument can be set to 1, 2, or 3. The higher the value, the better the resolution.

Use the [IBody2::Diagnose](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Diagnose.md) and the [IDiagnoseResult](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDiagnoseResult.md) APIs to get the gaps to fill.

Example

[Insert Fill-surface Feature (C#)](Insert_Fill-surface_Feature_Example_CSharp.htm)  
[Insert Fill-surface Feature (VB.NET)](Insert_Fill-surface_Feature_Example_VBNET.htm)  
[Insert Fill-surface Feature (VBA)](Insert_Fill-surface_Feature_Example_VB.htm)  
[Get and Fill Gaps in Body (C#)](Get_and_Fill_Gaps_in_Body_Example_CSharp.htm)  
[Get and Fill Gaps in Body (VB.NET)](Get_and_Fill_Gaps_in_Body_Example_VBNET.htm)  
[Get and Fill Gaps in Body (VBA)](Get_and_Fill_Gaps_in_Body_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IFillSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData.md)
