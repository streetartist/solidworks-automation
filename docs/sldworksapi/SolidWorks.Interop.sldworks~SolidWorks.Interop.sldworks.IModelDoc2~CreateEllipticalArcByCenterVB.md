# CreateEllipticalArcByCenterVB Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateEllipticalArcByCenterVB`

Obsolete. Superseded by SketchManager::CreateEllipticalArc.
Obsolete. Superseded by [SketchManager::CreateEllipticalArc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateEllipticalArc.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateEllipticalArcByCenterVB( _
   ByVal CenterX As System.Double, _
   ByVal CenterY As System.Double, _
   ByVal CenterZ As System.Double, _
   ByVal MajorX As System.Double, _
   ByVal MajorY As System.Double, _
   ByVal MajorZ As System.Double, _
   ByVal MinorX As System.Double, _
   ByVal MinorY As System.Double, _
   ByVal MinorZ As System.Double, _
   ByVal StartX As System.Double, _
   ByVal StartY As System.Double, _
   ByVal StartZ As System.Double, _
   ByVal EndX As System.Double, _
   ByVal EndY As System.Double, _
   ByVal EndZ As System.Double _
) As System.Boolean
```

```

Dim instance As IModelDoc2
Dim CenterX As System.Double
Dim CenterY As System.Double
Dim CenterZ As System.Double
Dim MajorX As System.Double
Dim MajorY As System.Double
Dim MajorZ As System.Double
Dim MinorX As System.Double
Dim MinorY As System.Double
Dim MinorZ As System.Double
Dim StartX As System.Double
Dim StartY As System.Double
Dim StartZ As System.Double
Dim EndX As System.Double
Dim EndY As System.Double
Dim EndZ As System.Double
Dim value As System.Boolean
 
value = instance.CreateEllipticalArcByCenterVB(CenterX, CenterY, CenterZ, MajorX, MajorY, MajorZ, MinorX, MinorY, MinorZ, StartX, StartY, StartZ, EndX, EndY, EndZ)
```

```

System.bool CreateEllipticalArcByCenterVB( 
   System.double CenterX,
   System.double CenterY,
   System.double CenterZ,
   System.double MajorX,
   System.double MajorY,
   System.double MajorZ,
   System.double MinorX,
   System.double MinorY,
   System.double MinorZ,
   System.double StartX,
   System.double StartY,
   System.double StartZ,
   System.double EndX,
   System.double EndY,
   System.double EndZ
)
```

```

System.bool CreateEllipticalArcByCenterVB( 
   System.double CenterX,
   System.double CenterY,
   System.double CenterZ,
   System.double MajorX,
   System.double MajorY,
   System.double MajorZ,
   System.double MinorX,
   System.double MinorY,
   System.double MinorZ,
   System.double StartX,
   System.double StartY,
   System.double StartZ,
   System.double EndX,
   System.double EndY,
   System.double EndZ
) 
```

#### Parameters

*CenterX*
:   X values for the ellipse center point

*CenterY*
:   Y values for the ellipse center point

*CenterZ*
:   Z values for the ellipse center point

*MajorX*
:   X values for a point on the ellipse and on the major axis

*MajorY*
:   Y values for a point on the ellipse and on the major axis

*MajorZ*
:   Z values for a point on the ellipse and on the major axis

*MinorX*
:   X values for a point on the ellipse and on the minor axis

*MinorY*
:   Y values for a point on the ellipse and on the minor axis

*MinorZ*
:   Z values for a point on the ellipse and on the minor axis

*StartX*
:   X values for CCW elliptical arc start point

*StartY*
:   Y values for CCW elliptical arc start point

*StartZ*
:   Z values for CCW elliptical arc start point

*EndX*
:   X values for CCW elliptical arc end point

*EndY*
:   Y values for CCW elliptical arc end point

*EndZ*
:   Z values for CCW elliptical arc end point

#### Return Value

True if successfully created, false otherwise

Remarks

The Start\* and End\* arguments should be specified in a counter-clockwise (CCW) manner.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::ICreateEllipse2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateEllipse2.md)  
[IModelDoc2::ICreateEllipticalArc2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateEllipticalArc2.md)  
[IModelDoc2::ICreateEllipticalArcByCenter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreateEllipticalArcByCenter.md)  
[IModelDoc2::CreateEllipse2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateEllipse2.md)  
[IModelDoc2::CreateEllipticalArc2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateEllipticalArc2.md)  
[IModelDoc2::CreateEllipticalArcByCenter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateEllipticalArcByCenter.md)
