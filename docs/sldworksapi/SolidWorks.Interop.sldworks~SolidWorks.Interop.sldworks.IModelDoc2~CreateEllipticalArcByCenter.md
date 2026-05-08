# CreateEllipticalArcByCenter Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateEllipticalArcByCenter`

Obsolete. Superseded by SketchManager::CreateEllipticalArc.
Obsolete. Superseded by [SketchManager::CreateEllipticalArc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateEllipticalArc.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateEllipticalArcByCenter( _
   ByVal Center As System.Object, _
   ByVal Major As System.Object, _
   ByVal Minor As System.Object, _
   ByVal Start As System.Object, _
   ByVal End As System.Object _
) As System.Boolean
```

```

Dim instance As IModelDoc2
Dim Center As System.Object
Dim Major As System.Object
Dim Minor As System.Object
Dim Start As System.Object
Dim End As System.Object
Dim value As System.Boolean
 
value = instance.CreateEllipticalArcByCenter(Center, Major, Minor, Start, End)
```

```

System.bool CreateEllipticalArcByCenter( 
   System.object Center,
   System.object Major,
   System.object Minor,
   System.object Start,
   System.object End
)
```

```

System.bool CreateEllipticalArcByCenter( 
   System.Object^ Center,
   System.Object^ Major,
   System.Object^ Minor,
   System.Object^ Start,
   System.Object^ End
) 
```

#### Parameters

*Center*
:   Array of 3 doubles(x1, y1, z1) in meters that describe the ellipse center

*Major*
:   Array of 3 doubles (x1, y1, z1) in meters that describe a point on the ellipse and on the major axis

*Minor*
:   Array of 3 doubles (x1, y1, z1) in meters that describe a point on the ellipse and on the minor axis

*Start*
:   Array of 3 doubles (x1, y1, z1) in meters that describe the start point of the ellipse

*End*
:   Array of 3 doubles (x1, y1, z1) in meters that describe the end point of the ellipse

#### Return Value

True if successfully created, false otherwise

Remarks

The Start and End arguments should be specified in a counter-clockwise (CCW) manner.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::ICreateEllipticalArcByCenter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateEllipticalArcByCenter.md)  
[IModelDoc2::ICreateEllipticalArc2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateEllipticalArc2.md)  
[IModelDoc2::ICreateEllipse2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateEllipse2.md)  
[IModelDoc2::CreateEllipticalArc2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateEllipticalArc2.md)  
[IModelDoc2::CreateEllipse2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateEllipse2.md)  
[IModelDoc2::CreateEllipticalArcByCenterVB Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateEllipticalArcByCenterVB.md)
