# SetSize Method (ISketchPicture)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~SetSize`

Sets the size of the picture on the sketch.
Sets the size of the picture on the sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetSize( _
   ByVal Width As System.Double, _
   ByVal Height As System.Double, _
   ByVal AspectRatioLocked As System.Boolean _
) As System.Boolean
```

```

Dim instance As ISketchPicture
Dim Width As System.Double
Dim Height As System.Double
Dim AspectRatioLocked As System.Boolean
Dim value As System.Boolean
 
value = instance.SetSize(Width, Height, AspectRatioLocked)
```

```

System.bool SetSize( 
   System.double Width,
   System.double Height,
   System.bool AspectRatioLocked
)
```

```

System.bool SetSize( 
   System.double Width,
   System.double Height,
   System.bool AspectRatioLocked
) 
```

#### Parameters

*Width*
:   Width of the picture in meters

*Height*
:   Height of the picture in meters

*AspectRatioLocked*
:   True to keep a fixed width and height aspect ratio, false to not

#### Return Value

True if the size of the picture is set, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchPicture Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture.md)  
[ISketchPicture Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture_members.md)  
[ISketchPicture::GetSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~GetSize.md)
