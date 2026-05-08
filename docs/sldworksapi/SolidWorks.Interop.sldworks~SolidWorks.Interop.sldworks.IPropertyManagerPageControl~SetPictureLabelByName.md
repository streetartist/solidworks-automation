# SetPictureLabelByName Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl~SetPictureLabelByName`

Sets the bitmap label for this control on a PropertyManager page.
Sets the bitmap label for this control on a PropertyManager page.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetPictureLabelByName( _
   ByVal ColorBitmap As System.String, _
   ByVal MaskBitmap As System.String _
) As System.Boolean
```

```

Dim instance As IPropertyManagerPageControl
Dim ColorBitmap As System.String
Dim MaskBitmap As System.String
Dim value As System.Boolean
 
value = instance.SetPictureLabelByName(ColorBitmap, MaskBitmap)
```

```

System.bool SetPictureLabelByName( 
   System.string ColorBitmap,
   System.string MaskBitmap
)
```

```

System.bool SetPictureLabelByName( 
   System.String^ ColorBitmap,
   System.String^ MaskBitmap
) 
```

#### Parameters

*ColorBitmap*
:   Fully qualified path to the location of the bitmap (i.e., the graphic to use) on disk

*MaskBitmap*
:   Fully qualified path to the location of the alpha mask bitmap on disk

#### Return Value

True if successful, false if not

Remarks

The image format for the two bitmaps is 18 x 18 pixels x 256 colors. The pixels in MaskBitmap specify transparency through shades of grey with boundaries of black pixels = 100% opaque and white pixels = 100% transparent.

You can only use this method on a PropertyManager page before the page is displayed, while it is displayed, or when it is closed.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageControl Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl.md)  
[IPropertyManagerPageControl Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl_members.md)
