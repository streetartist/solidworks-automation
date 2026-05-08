# SetPoints Method (ISketchParabola)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchParabola~SetPoints`

Sets all four sketch points for a parabola.
Sets all four sketch points for a parabola.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetPoints( _
   ByVal CenterX As System.Double, _
   ByVal CenterY As System.Double, _
   ByVal CenterZ As System.Double, _
   ByVal ApexX As System.Double, _
   ByVal ApexY As System.Double, _
   ByVal ApexZ As System.Double, _
   ByVal StartX As System.Double, _
   ByVal StartY As System.Double, _
   ByVal StartZ As System.Double, _
   ByVal EndX As System.Double, _
   ByVal EndY As System.Double, _
   ByVal EndZ As System.Double _
) As System.Boolean
```

```

Dim instance As ISketchParabola
Dim CenterX As System.Double
Dim CenterY As System.Double
Dim CenterZ As System.Double
Dim ApexX As System.Double
Dim ApexY As System.Double
Dim ApexZ As System.Double
Dim StartX As System.Double
Dim StartY As System.Double
Dim StartZ As System.Double
Dim EndX As System.Double
Dim EndY As System.Double
Dim EndZ As System.Double
Dim value As System.Boolean
 
value = instance.SetPoints(CenterX, CenterY, CenterZ, ApexX, ApexY, ApexZ, StartX, StartY, StartZ, EndX, EndY, EndZ)
```

```

System.bool SetPoints( 
   System.double CenterX,
   System.double CenterY,
   System.double CenterZ,
   System.double ApexX,
   System.double ApexY,
   System.double ApexZ,
   System.double StartX,
   System.double StartY,
   System.double StartZ,
   System.double EndX,
   System.double EndY,
   System.double EndZ
)
```

```

System.bool SetPoints( 
   System.double CenterX,
   System.double CenterY,
   System.double CenterZ,
   System.double ApexX,
   System.double ApexY,
   System.double ApexZ,
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
:   x coordinate of center (focal) sketch point

*CenterY*
:   y coordinate of center (focal) sketch point

*CenterZ*
:   z coordinate of center (focal) sketch point

*ApexX*
:   x coordinate of apex sketch point

*ApexY*
:   y coordinate of apex sketch point

*ApexZ*
:   z coordinate of apex sketch point

*StartX*
:   x coordinate of start sketch point

*StartY*
:   y coordinate of start sketch point

*StartZ*
:   z coordinate of start sketch point

*EndX*
:   x coordinate of end sketch point

*EndY*
:   y coordinate of end sketch point

*EndZ*
:   z coordinate of end sketch point

#### Return Value

True if all four sketch points are set, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchParabola Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchParabola.md)  
[ISketchParabola Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchParabola_members.md)
