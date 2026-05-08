# SetCoordinates Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~SetCoordinates`

Sets the position of this sketch text.
Sets the position of this sketch text.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetCoordinates( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Boolean
```

```

Dim instance As ISketchText
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Boolean
 
value = instance.SetCoordinates(X, Y, Z)
```

```

System.bool SetCoordinates( 
   System.double X,
   System.double Y,
   System.double Z
)
```

```

System.bool SetCoordinates( 
   System.double X,
   System.double Y,
   System.double Z
) 
```

#### Parameters

*X*
:   X coordinate of the sketch text position

*Y*
:   Y coordinate of the sketch text position

*Z*
:   Z coordinate of the sketch text position

#### Return Value

True if the sketch text position is successfully set, false if not

Remarks

To set the sketch text position, you must be editing the sketch. See [IModelDoc2::EditSketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditSketch.md) or [ISketchManager::InsertSketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~InsertSketch.md).

To get the position of this sketch text, use [ISketchText::GetCoordinates](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~GetCoordinates.md) and [ISketchText::IGetCoordinates](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText~IGetCoordinates.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchText Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText.md)  
[ISketchText Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText_members.md)
