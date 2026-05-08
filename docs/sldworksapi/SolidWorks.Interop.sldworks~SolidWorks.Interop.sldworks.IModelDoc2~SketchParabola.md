# SketchParabola Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchParabola`

Obsolete. Superseded by ISketchManager::CreateParabola.
Obsolete. Superseded by [ISketchManager::CreateParabola](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateParabola.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SketchParabola( _
   ByVal Val1 As System.Double, _
   ByVal Val2 As System.Double, _
   ByVal Z1 As System.Double, _
   ByVal Val3 As System.Double, _
   ByVal Val4 As System.Double, _
   ByVal Z2 As System.Double, _
   ByVal Val5 As System.Double, _
   ByVal Val6 As System.Double, _
   ByVal Z3 As System.Double, _
   ByVal Val7 As System.Double, _
   ByVal Val8 As System.Double, _
   ByVal Z4 As System.Double _
) 
```

```

Dim instance As IModelDoc2
Dim Val1 As System.Double
Dim Val2 As System.Double
Dim Z1 As System.Double
Dim Val3 As System.Double
Dim Val4 As System.Double
Dim Z2 As System.Double
Dim Val5 As System.Double
Dim Val6 As System.Double
Dim Z3 As System.Double
Dim Val7 As System.Double
Dim Val8 As System.Double
Dim Z4 As System.Double
 
instance.SketchParabola(Val1, Val2, Z1, Val3, Val4, Z2, Val5, Val6, Z3, Val7, Val8, Z4)
```

```

void SketchParabola( 
   System.double Val1,
   System.double Val2,
   System.double Z1,
   System.double Val3,
   System.double Val4,
   System.double Z2,
   System.double Val5,
   System.double Val6,
   System.double Z3,
   System.double Val7,
   System.double Val8,
   System.double Z4
)
```

```

void SketchParabola( 
   System.double Val1,
   System.double Val2,
   System.double Z1,
   System.double Val3,
   System.double Val4,
   System.double Z2,
   System.double Val5,
   System.double Val6,
   System.double Z3,
   System.double Val7,
   System.double Val8,
   System.double Z4
) 
```

#### Parameters

*Val1*
:   X location of the focus of the parabola

*Val2*
:   Y location of the focus of the parabola

*Z1*
:   Z location of the focus of the parabola

*Val3*
:   X location of the apex of the parabola

*Val4*
:   Y location of the apex of the parabola

*Z2*
:   Z location of the apex of the parabola

*Val5*
:   X location of the start of the parabola

*Val6*
:   Y location of the start of the parabola

*Z3*
:   Z lLocation of the start of the parabola

*Val7*
:   X location of the end of the parabola

*Val8*
:   Y location of the end of the parabola

*Z4*
:   Z location of the end of the parabola

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[ISketchParabola Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchParabola.md)
