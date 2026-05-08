# ICreateEllipticalArcByCenter Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateEllipticalArcByCenter`

Creates an elliptical arc trimmed between two points.
Creates an elliptical arc trimmed between two points.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ICreateEllipticalArcByCenter( _
   ByRef Center As System.Double, _
   ByRef Major As System.Double, _
   ByRef Minor As System.Double, _
   ByRef Start As System.Double, _
   ByRef End As System.Double _
) 
```

```

Dim instance As IModelDoc2
Dim Center As System.Double
Dim Major As System.Double
Dim Minor As System.Double
Dim Start As System.Double
Dim End As System.Double
 
instance.ICreateEllipticalArcByCenter(Center, Major, Minor, Start, End)
```

```

void ICreateEllipticalArcByCenter( 
   ref System.double Center,
   ref System.double Major,
   ref System.double Minor,
   ref System.double Start,
   ref System.double End
)
```

```

void ICreateEllipticalArcByCenter( 
   System.double% Center,
   System.double% Major,
   System.double% Minor,
   System.double% Start,
   System.double% End
) 
```

#### Parameters

*Center*
:   Array of 3 doubles (x1, y1, z1) in meters that describe the ellipse center

*Major*
:   :   Array of 3 doubles (x1, y1, z1) in meters that describe a point on the ellipse and on the major axis

*Minor*
:   :   Array of 3 doubles (x1, y1, z1) in meters that describe a point on the ellipse and on the minor axis

*Start*
:   :   Array of 3 doubles (x1, y1, z1) in meters that describe the start point of the ellipse

*End*
:   Array of 3 doubles (x1, y1, z1) in meters that describe the end point of the ellipse

#### Return Value

True if successfully created, false if not

Remarks

The Start and End arguments should be specified in a counter-clockwise (CCW) manner.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::CreateEllipse2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateEllipse2.md)  
[IModelDoc2::CreateEllipticalArc2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateEllipticalArc2.md)  
[IModelDoc2::CreateEllipticalArcByCenter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateEllipticalArcByCenter.md)  
[IModelDoc2::CreateEllipticalArcByCenterVB Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateEllipticalArcByCenterVB.md)  
[IModelDoc2::ICreateEllipse2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateEllipse2.md)  
[IModelDoc2::ICreateEllipticalArc2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateEllipticalArc2.md)
