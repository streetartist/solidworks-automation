# SketchSplineByEqnParams2 Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchSplineByEqnParams2`

Obsolete. Superseded by ISketchManager::CreateSplineByEqnParams.
Obsolete. Superseded by [ISketchManager::CreateSplineByEqnParams](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSplineByEqnParams.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SketchSplineByEqnParams2( _
   ByVal ParamsIn As System.Object _
) As System.Boolean
```

```

Dim instance As IModelDoc2
Dim ParamsIn As System.Object
Dim value As System.Boolean
 
value = instance.SketchSplineByEqnParams2(ParamsIn)
```

```

System.bool SketchSplineByEqnParams2( 
   System.object ParamsIn
)
```

```

System.bool SketchSplineByEqnParams2( 
   System.Object^ ParamsIn
) 
```

#### Parameters

*ParamsIn*
:   Array containing an array of doubles (see **Remarks**)

#### Return Value

True if created successfully, false if not

Remarks

The parameters are provided as 3 arrays, which for OLE automation are packed into a single SafeArray packed as follows:

[ Dimension, Order, Number of control Points, Periodicity, knot1, knot2,...,ControlPoint1[Dimension], ControlPoint2[Dimension],... ]

Pass control point coordinates to this method in sketch space. The Z value is interpreted as 0. In certain situations, you must transform your b-curve parameters to sketch space with the help of [ISketch::ModelToSketchTransform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~ModelToSketchTransform.md).

NOTE: If the spline being generated is a closed spline, then it must be flagged as periodic. In addition, splines generated in sketches must be G1 continuous. If the data passed to this method does not generate a G1 continuous spline, then it is rejected and a spline is not created. If your data is not G1 continuous, then you must split the spline into multiple G1 segments and call method for each segment.

Example

[Sketch a Spline (VBA)](Sketch_Spline_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::ISketchSplineByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ISketchSplineByEqnParams.md)  
[IModelDoc2::CreateSplineByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateSplineByEqnParams.md)  
[IModelDoc2::CreateSplinesByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateSplinesByEqnParams.md)  
[IModelDoc2::ICreateSplineByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateSplineByEqnParams.md)  
[IModelDoc2::ICreateSplinesByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateSplinesByEqnParams.md)
