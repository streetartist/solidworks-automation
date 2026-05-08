# CreateLine2 Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateLine2`

Obsolete. Superseded by SketchManager::CreateLine.
Obsolete. Superseded by [SketchManager::CreateLine](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateLine.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateLine2( _
   ByVal P1x As System.Double, _
   ByVal P1y As System.Double, _
   ByVal P1z As System.Double, _
   ByVal P2x As System.Double, _
   ByVal P2y As System.Double, _
   ByVal P2z As System.Double _
) As System.Object
```

```

Dim instance As IModelDoc2
Dim P1x As System.Double
Dim P1y As System.Double
Dim P1z As System.Double
Dim P2x As System.Double
Dim P2y As System.Double
Dim P2z As System.Double
Dim value As System.Object
 
value = instance.CreateLine2(P1x, P1y, P1z, P2x, P2y, P2z)
```

```

System.object CreateLine2( 
   System.double P1x,
   System.double P1y,
   System.double P1z,
   System.double P2x,
   System.double P2y,
   System.double P2z
)
```

```

System.Object^ CreateLine2( 
   System.double P1x,
   System.double P1y,
   System.double P1z,
   System.double P2x,
   System.double P2y,
   System.double P2z
) 
```

#### Parameters

*P1x*
:   X value of the line start point

*P1y*
:   Y value of the line start point

*P1z*
:   Z value of the line start point

*P2x*
:   X value of the line end point

*P2y*
:   Y value of the line end point

*P2z*
:   Z value of the line end point

#### Return Value

Newly created sketch line

Remarks

If a sketch is not active, then the line is not created and NULL is returned. You can check for an active sketch using [IModelDoc2::GetActiveSketch2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetActiveSketch2.md) or [IModelDoc2::IGetActiveSketch2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetActiveSketch2.md).

For COM applications, the underlying [ISketchLine](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine.md) object can be obtained using QueryInterface on the [ISketchSegment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.md) object returned. C++ Dispatch applications can define a new ISketchLine or ISketchSegment object that uses this Dispatch pointer. Visual Basic applications interpret the pointer for you automatically so you can use the returned object to call ISketchSegment or ISketchLine functions.

[IModelDoc2::SetAddToDB](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetAddToDB.md) and [IModelDoc2::SetDisplayWhenAdded](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetDisplayWhenAdded.md) increase performance during entity creation by adding entities directly to the SOLIDWORKS database. IModelDoc2::SetAddToDB also avoids inferencing.

When this method is used with a drawing document, this method creates the line relative to the active drawing view, [IDrawingDoc::ActiveDrawingView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ActiveDrawingView.md) or [IDrawingDoc::IActiveDrawingView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IActiveDrawingView.md).

Example

[Calculate Closest Distance Between Faces (VBA)](Calculate_Closest_Distance_Between_Faces_Example_VB.htm)  
[Calculate Closest Distance Between Model Components (VBA)](Calculate_Closest_Distance_Between_Model_Components_Example_VB.htm)  
[Create Section View at Specified Location (VBA)](Create_Section_View_at_Specified_Location_Example_VB.htm)  
[Find Outside Edges of Face (VBA)](Find_Outside_Edges_of_Face_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::ICreateLine2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateLine2.md)
