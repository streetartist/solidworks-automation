# ICreateSpline Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateSpline`

Obsolete. Superseded by ISketchManager::ICreateSpline.
Obsolete. Superseded by [ISketchManager::ICreateSpline](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~ICreateSpline.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateSpline( _
   ByVal PointCount As System.Integer, _
   ByRef PointData As System.Double _
) As SketchSegment
```

```

Dim instance As IModelDoc2
Dim PointCount As System.Integer
Dim PointData As System.Double
Dim value As SketchSegment
 
value = instance.ICreateSpline(PointCount, PointData)
```

```

SketchSegment ICreateSpline( 
   System.int PointCount,
   ref System.double PointData
)
```

```

SketchSegment^ ICreateSpline( 
   System.int PointCount,
   System.double% PointData
) 
```

#### Parameters

*PointCount*
:   Number of points in the pointData array

*PointData*
:   Set of X,Y,Z point coordinates to use in creating the spline (see **Remarks**)

#### Return Value

Newly created [spline](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md)

Remarks

This method creates a spline in the active 2D sketch. If a sketch is not active, then a new sketch is created. Use [IModelDoc2::GetActiveSketch2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetActiveSketch2.md) or [IModelDoc2::IGetActiveSketch2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetActiveSketch2.md) to check if the sketch active.

The PointData array is a set of, at least, two X, Y, Z values. The X value for the start point of the spline is PointData[0], the Y value for the start point is PointData[1], and the Z value for the start point is PointData[2]. The X value for the next point is PointData[3], and so on. For the COM interface, the total number of points in the array must be passed in. For the OLE interface, the total number of points are determined automatically, by taking the UBound of the PointData VARIANT and dividing by 3, so be careful to dimension that array correctly.

For COM applications, you can use the object pointer returned from this method to call any APIs on the [ISketchSegment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md) interface. You can obtain the underlying [ISketchSpline](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.md) object by using QueryInterface on the returned ISketchSegment object.

OLE applications can define a new ISketchSegment or ISketchSpline object using the returned Dispatch pointer. Visual Basic applications interpret the pointer for you automatically, so you can use the returned object to call SketchSegment or [ISketchEllipse](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse.md) APIs.

This method does not work with [IModelDoc2::SetAddToDB](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetAddToDB.md) or [IModelDoc2::SetDisplayWhenAdded](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetDisplayWhenAdded.md). It always adds the spline directly to the database (as if IModelDoc2::SetAddToDB(True) was in effect), and you must redraw your document window to see the entities that you added (as if IModelDoc2::SetDisplayWhenAdded(false) was in effect).

In 2D sketches, SOLIDWORKS ignores the Z value in PointData.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::CreateSplineByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateSplineByEqnParams.md)  
[IModelDoc2::CreateSplinesByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateSplinesByEqnParams.md)  
[IModelDoc2::CreateSpline Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateSpline.md)  
[IModelDoc2::ICreateSplineByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateSplineByEqnParams.md)  
[IModelDoc2::ICreateSplinesByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateSplinesByEqnParams.md)
