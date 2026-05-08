# Flip Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~Flip`

Flips the picture, in its same position, either side to side or top to bottom.
Flips the picture, in its same position, either side to side or top to bottom.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Flip( _
   ByVal SideToSide As System.Boolean _
) As System.Boolean
```

```

Dim instance As ISketchPicture
Dim SideToSide As System.Boolean
Dim value As System.Boolean
 
value = instance.Flip(SideToSide)
```

```

System.bool Flip( 
   System.bool SideToSide
)
```

```

System.bool Flip( 
   System.bool SideToSide
) 
```

#### Parameters

*SideToSide*
:   True to flip the picture side to side, false to flip the picture top to bottom (see **Remarks**)

#### Return Value

True if the picture is flipped, false if not

Remarks

|  |  |
| --- | --- |
| If you flip the picture... | Then the [angle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~Angle.md)... |
| side to side | remains the same and the [ISketchPicture::Flipped](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture~Flipped.md) property returns true. |
| top to bottom | increments by 180 and the ISketchPicture::Flipped property returns true. |
| side to side and top to bottom | rotates 180 and ISketchPicture::Flipped returns false. |

Example

See the [ISketchPicture](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchPicture Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture.md)  
[ISketchPicture Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture_members.md)
