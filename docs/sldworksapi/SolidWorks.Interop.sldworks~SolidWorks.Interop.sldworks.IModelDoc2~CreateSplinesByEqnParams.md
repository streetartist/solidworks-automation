# CreateSplinesByEqnParams Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateSplinesByEqnParams`

Obsolete. Superseded by ISketchManager::CreateSplinesByEqnParams.
Obsolete. Superseded by [ISketchManager::CreateSplinesByEqnParams](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSplinesByEqnParams.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateSplinesByEqnParams( _
   ByVal ParamsIn As System.Object _
) As System.Object
```

```

Dim instance As IModelDoc2
Dim ParamsIn As System.Object
Dim value As System.Object
 
value = instance.CreateSplinesByEqnParams(ParamsIn)
```

```

System.object CreateSplinesByEqnParams( 
   System.object ParamsIn
)
```

```

System.Object^ CreateSplinesByEqnParams( 
   System.Object^ ParamsIn
) 
```

#### Parameters

*ParamsIn*
:   Array containing an array of doubles to use in creating the spline (see **Remarks**)

#### Return Value

Array containing an array of objects of the newly created splines

Remarks

The parameters are provided as three arrays, which for OLE automation are packed into a single SafeArray, which is packed as follows:

[ Dimension, Order, Number of control Points, Periodicity, knot1, knot2,...,ControlPoint1[Dimension], ControlPoint2[Dimension],... ]

Pass the control point coordinates to this routine in sketch space. The Z value is  interpreted as 0. In certain situations, you must transform your B-curve parameters to sketch space using [ISketch::ModelToSketchTransform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~ModelToSketchTransform.md).

NOTE: If the generated spline is a closed spline, then it must be flagged as periodic. Additionally, splines generated in sketches must be G1 continuous. If the data passed to this method does not generate a G1 continuous spline, then it is rejected and a spline is not created. If your data is not G1 continuous, then you must split the spline into multiple G1 segments and call this method for each segment.

For the OLE interface, you can use the returned object pointer directly to call any APIs on the [ISketchSpline](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.md) interface or its base class, [ISketchSegment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md).

This method does not work with [IModelDoc2::SetAddToDB](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetAddToDB.md) or [IModelDoc2::SetDisplayWhenAdded](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetDisplayWhenAdded.md). It always adds the spline directly to the database (as if IModelDoc2::SetAddToDB(True) is in effect), and you must redraw your document window to see the entities that you added (as if IModelDoc2::SetDisplayWhenAdded(false) is in effect).

To create 3D splines, see [IModelDoc2::InsertCurveFilePoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertCurveFilePoint.md) and related functions.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::CreateSpline Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateSpline.md)  
[IModelDoc2::CreateSplineByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateSplineByEqnParams.md)  
[IModelDoc2::ICreateSpline Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateSpline.md)  
[IModelDoc2::ICreateSplineByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateSplineByEqnParams.md)  
[IModelDoc2::ICreateSplinesByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateSplinesByEqnParams.md)  
[IModelDoc2::InsertCurveFile Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertCurveFile.md)  
[IModelDoc2::InsertCurveFileBegin Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertCurveFileBegin.md)  
[IModelDoc2::InsertCurveFileEnd Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertCurveFileEnd.md)
