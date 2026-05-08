# GetFloorNormal Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~GetFloorNormal`

Gets the normal to the floor of this scene.
Gets the normal to the floor of this scene.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GetFloorNormal( _
   ByRef Point As MathPoint, _
   ByRef Normal As MathVector _
) 
```

```

Dim instance As ISwScene
Dim Point As MathPoint
Dim Normal As MathVector
 
instance.GetFloorNormal(Point, Normal)
```

```

void GetFloorNormal( 
   out MathPoint Point,
   out MathVector Normal
)
```

```

void GetFloorNormal( 
   [Out] MathPoint^ Point,
   [Out] MathVector^ Normal
) 
```

#### Parameters

*Point*
:   [IMathPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md)

*Normal*
:   [IMathVector](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md)

Example

See the [ISwScene](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.md)  
[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.md)
