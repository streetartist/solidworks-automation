# GetOrigin Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~GetOrigin`

Gets the origin of the picture on the sketch.
Gets the origin of the picture on the sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GetOrigin( _
   ByRef X As System.Double, _
   ByRef Y As System.Double _
) 
```

```

Dim instance As ISketchPicture
Dim X As System.Double
Dim Y As System.Double
 
instance.GetOrigin(X, Y)
```

```

void GetOrigin( 
   out System.double X,
   out System.double Y
)
```

```

void GetOrigin( 
   [Out] System.double X,
   [Out] System.double Y
) 
```

#### Parameters

*X*
:   x coordinate

*Y*
:   y coordinate

Remarks

The coordinates in meters indicate the position of the lower-left corner of the picture in sketch space.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchPicture Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture.md)  
[ISketchPicture Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture_members.md)  
[ISketchPicture::SetOrigin Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~SetOrigin.md)
