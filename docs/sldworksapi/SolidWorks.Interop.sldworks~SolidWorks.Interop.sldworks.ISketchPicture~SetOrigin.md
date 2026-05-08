# SetOrigin Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~SetOrigin`

Sets the origin of the picture of the sketch.
Sets the origin of the picture of the sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetOrigin( _
   ByVal X As System.Double, _
   ByVal Y As System.Double _
) As System.Boolean
```

```

Dim instance As ISketchPicture
Dim X As System.Double
Dim Y As System.Double
Dim value As System.Boolean
 
value = instance.SetOrigin(X, Y)
```

```

System.bool SetOrigin( 
   System.double X,
   System.double Y
)
```

```

System.bool SetOrigin( 
   System.double X,
   System.double Y
) 
```

#### Parameters

*X*
:   x coordinate

*Y*
:   y coordinate

#### Return Value

True if the origin is set, false if not

Remarks

The coordinates in meters indicate the position of the lower-left corner of the picture in sketch space.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchPicture Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture.md)  
[ISketchPicture Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture_members.md)  
[ISketchPicture::GetOrigin Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~GetOrigin.md)
