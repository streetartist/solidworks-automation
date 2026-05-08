# CreateSplinesByEqnParams Method (ISketchManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSplinesByEqnParams`

Obsolete. Superseded by ISketchManager::CreateSplinesByEqnParams2.
Obsolete. Superseded by [ISketchManager::CreateSplinesByEqnParams2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSplinesByEqnParams2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateSplinesByEqnParams( _
   ByVal Parameters As System.Object _
) As System.Object
```

```

Dim instance As ISketchManager
Dim Parameters As System.Object
Dim value As System.Object
 
value = instance.CreateSplinesByEqnParams(Parameters)
```

```

System.object CreateSplinesByEqnParams( 
   System.object Parameters
)
```

```

System.Object^ CreateSplinesByEqnParams( 
   System.Object^ Parameters
) 
```

#### Parameters

*Parameters*
:   Array containing an array of doubles to use in creating the spline (see **Remarks**)

#### Return Value

Array of [sketch segments](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md) of the newly created splines

Remarks

The Properties array contains four longs (placed in the first four doubles in the array):

- Dimension
- Order
- Number of Control Points
- Periodicity ( true or false)

The Knots array contains doubles with (Number of Control Points + Order) elements.

The size of the ControlPoints array is based upon the curve dimension.

- Dimension = 2 then each Control Point is an array of 2 doubles ( x, y )
- Dimension = 3 then each Control Point is an array of 3 doubles ( x, y, z)
- Dimension = 4 then each Control Point is an array of 4 doubles ( x, y, z, w ) where w = weight

The parameters are provided as three arrays.

Pass the control point coordinates to this routine in sketch space. The Z value is  interpreted as 0. In certain situations, you must transform your B-curve parameters to sketch space using [ISketch::ModelToSketchTransform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~ModelToSketchTransform.md).

**NOTE:** If the spline being generated is a closed spline, then it must be flagged as periodic. If the data passed to this method does not generate a G1 continuous spline, then it creates multiple G1 continuous spline segments.

This method does not work with [ISketchManager::AddToDB](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~AddToDB.md) or [ISketchManager::DisplayWhenAdded](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~DisplayWhenAdded.md). It always adds the spline directly to the database (as if ISketchManager::AddToDB(True) is in effect), and you must redraw your document window to see the entities that you added (as if ISketchManager::DisplayWhenAdded(False) is in effect).

To create 3D splines, see [IModelDoc2::InsertCurveFilePoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertCurveFilePoint.md) and related functions.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)  
[ISketchManager::CreateSpline Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSpline.md)  
[ISketchManager::CreateSplineByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSplineByEqnParams.md)  
[ISketchManager::ICreateSpline Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~ICreateSpline.md)  
[ISketchManager::ICreateSplineByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~ICreateSplineByEqnParams.md)  
[ISketchManager::ICreateSplinesByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~ICreateSplinesByEqnParams.md)
