# Flipped Property (ISketchPicture)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~Flipped`

Gets whether the picture has been flipped in the sketch.
Gets whether the picture has been flipped in the sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Flipped As System.Boolean
```

```

Dim instance As ISketchPicture
Dim value As System.Boolean
 
value = instance.Flipped
```

```

System.bool Flipped {get;}
```

```

property System.bool Flipped {
   System.bool get();
}
```

#### Property Value

True if the picture has been flipped either side to side or top to bottom, false if not (see **Remarks**)

Remarks

When a picture has not been flipped, as when you initially insert it, the bottom of the picture is defined by starting at the origin and proceeding in the direction of the [angle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~Angle.md). If a picture has been flipped, then the bottom of the picture is defined by starting at the origin and proceeding in a direction opposite the angle. In other words, the picture is mirrored or reflected, but not duplicated.

If a picture has been [flipped](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~Flip.md) both side to side and top to bottom, then this property returns false.

Example

See the [ISketchPicture](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchPicture Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture.md)  
[ISketchPicture Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture_members.md)  
[ISketchPicture::GetOrigin Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~GetOrigin.md)  
[ISketchPicture::SetOrigin Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~SetOrigin.md)
