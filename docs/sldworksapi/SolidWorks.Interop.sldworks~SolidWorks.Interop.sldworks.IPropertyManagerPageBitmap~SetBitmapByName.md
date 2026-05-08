# SetBitmapByName Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageBitmap~SetBitmapByName`

Sets the bitmap for this control.
Sets the bitmap for this control.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetBitmapByName( _
   ByVal ColorBitmap As System.String, _
   ByVal MaskBitmap As System.String _
) As System.Boolean
```

```

Dim instance As IPropertyManagerPageBitmap
Dim ColorBitmap As System.String
Dim MaskBitmap As System.String
Dim value As System.Boolean
 
value = instance.SetBitmapByName(ColorBitmap, MaskBitmap)
```

```

System.bool SetBitmapByName( 
   System.string ColorBitmap,
   System.string MaskBitmap
)
```

```

System.bool SetBitmapByName( 
   System.String^ ColorBitmap,
   System.String^ MaskBitmap
) 
```

#### Parameters

*ColorBitmap*
:   Full path and filename of the bitmap on disk

*MaskBitmap*
:   Full path and filename of the alpha mask bitmap on disk

#### Return Value

True if the bitmap is set for this control, false if not

Remarks

If you are creating a PropertyManager page add-in and ColorBitmap is either invalid or has the wrong path, this method displays an alternative image and returns false.

The typical image format for the two SOLIDWORKS bitmaps is 18 x 18 pixels x 256 colors. Using this method, you can specify a bigger bitmap, e.g., 24 x 24 pixels, to get extra detail. The pixels in MaskBitmap specify transparency through shades of grey with boundaries of black pixels = 100% opaque and white pixels = 100% transparent.

Use [IPropertyManagerPageControl::Top](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl~Top.md) to set the top of the control and use [IPropertyManagerPageControl::Tip](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl~Tip.md) to set the ToolTip.

You can use this method before, during, or after the PropertyManager page is displayed or closed. If you use this method when the PropertyManager page is displayed, use bitmaps that are the same size.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageBitmap Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageBitmap.md)  
[IPropertyManagerPageBitmap Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageBitmap_members.md)
