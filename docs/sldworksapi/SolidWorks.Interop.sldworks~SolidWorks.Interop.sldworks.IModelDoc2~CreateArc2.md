# CreateArc2 Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateArc2`

Obsolete. Superseded by ISketchManager::CreateArc.
Obsolete. Superseded by [ISketchManager::CreateArc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateArc.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateArc2( _
   ByVal XC As System.Double, _
   ByVal YC As System.Double, _
   ByVal Zc As System.Double, _
   ByVal Xp1 As System.Double, _
   ByVal Yp1 As System.Double, _
   ByVal Zp1 As System.Double, _
   ByVal Xp2 As System.Double, _
   ByVal Yp2 As System.Double, _
   ByVal Zp2 As System.Double, _
   ByVal Direction As System.Short _
) As System.Object
```

```

Dim instance As IModelDoc2
Dim XC As System.Double
Dim YC As System.Double
Dim Zc As System.Double
Dim Xp1 As System.Double
Dim Yp1 As System.Double
Dim Zp1 As System.Double
Dim Xp2 As System.Double
Dim Yp2 As System.Double
Dim Zp2 As System.Double
Dim Direction As System.Short
Dim value As System.Object
 
value = instance.CreateArc2(XC, YC, Zc, Xp1, Yp1, Zp1, Xp2, Yp2, Zp2, Direction)
```

```

System.object CreateArc2( 
   System.double XC,
   System.double YC,
   System.double Zc,
   System.double Xp1,
   System.double Yp1,
   System.double Zp1,
   System.double Xp2,
   System.double Yp2,
   System.double Zp2,
   System.short Direction
)
```

```

System.Object^ CreateArc2( 
   System.double XC,
   System.double YC,
   System.double Zc,
   System.double Xp1,
   System.double Yp1,
   System.double Zp1,
   System.double Xp2,
   System.double Yp2,
   System.double Zp2,
   System.short Direction
) 
```

#### Parameters

*XC*
:   X value of the circle center point in meters

*YC*
:   Y value of the circle center point in meters

*Zc*
:   Z value of the circle center point in meters

*Xp1*
:   X value of the start point of the arc in meters

*Yp1*
:   Y value of the start point of the arc in meters

*Zp1*
:   Z value of the start point of the arc in meters

*Xp2*
:   X value of the end point of the arc in meters

*Yp2*
:   Y value of the end point of the arc in meters

*Zp2*
:   Z value of the end point of the arc in meters

*Direction*
:   - +1 : Go from the start point to the end point in a counter-clockwise direction
    - -1 : Go from the start point to the end point in a clockwise direction

#### Return Value

Newly created arc (see **Remarks**)

Remarks

This method creates a partial arc in the active 2D sketch. If a sketch is not active, then a new sketch is created. You can check for an active sketch using [IModelDoc2::GetActiveSketch2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetActiveSketch2.md) or [IModelDoc2::IGetActiveSketch2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetActiveSketch2.md).

For COM applications, the object pointer returned from this method can be used to call any APIs on the [ISketchSegment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md) interface. The underlying [ISketchArc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc.md) object can be obtained using QueryInterface on the returned ISketchSegment object.

OLE applications can define a new ISketchSegment or ISketchArc object using the returned Dispatch pointer. Visual Basic applications interpret the pointer for you automatically, so you can use the returned object to call ISketchSegment or ISketchArc functions.

[IModelDoc2::SetAddToDB](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetAddToDB.md) and [IModelDoc2::SetDisplayWhenAdded](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetDisplayWhenAdded.md) increase performance during entity creation by adding entities directly to the SOLIDWORKS database.

- IModelDoc2::SetAddToDB also avoids some of the peculiarities involved with creating entities via the user interface, such as inferencing, automatic relations, and snapping to the grid. Adding entities directly to the database also increases the performance of this API. When you are done creating entities, it is important to call IModelDoc2::SetAddToDB(false), to restore SOLIDWORKS to its normal operating mode.
- This method also works with IModelDoc2::SetDisplayWhenAdded. If you have called IModelDoc2::SetAddToDB(True), additional performance can be gained by calling IModelDoc2::SetDisplayWhenAdded(false) to disable immediate display of entities as they are added to the database. When you are done creating all of your sketch entities, you must redraw your document window (see [IModelDoc2::GraphicsRedraw2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GraphicsRedraw2.md)) to see the entities that you added. You should also restore the original display settings by calling IModelDoc2::SetDisplayWhenAdded(True).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
