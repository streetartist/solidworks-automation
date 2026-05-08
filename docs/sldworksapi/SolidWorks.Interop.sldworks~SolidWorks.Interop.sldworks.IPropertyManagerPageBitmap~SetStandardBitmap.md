# SetStandardBitmap Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageBitmap~SetStandardBitmap`

Sets the bitmap or PNG image for this control.
Sets the bitmap or PNG image for this control.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetStandardBitmap( _
   ByVal Bitmap As System.Integer _
) As System.Boolean
```

```

Dim instance As IPropertyManagerPageBitmap
Dim Bitmap As System.Integer
Dim value As System.Boolean
 
value = instance.SetStandardBitmap(Bitmap)
```

```

System.bool SetStandardBitmap( 
   System.int Bitmap
)
```

```

System.bool SetStandardBitmap( 
   System.int Bitmap
) 
```

#### Parameters

*Bitmap*
:   Control standard type as defined in [swBitmapControlStandardTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBitmapControlStandardTypes_e.html)

#### Return Value

True if the bitmap or PNG image is set, false if not

Remarks

You can use this method before, during, or after the PropertyManager page is displayed or closed. If you use this method when the PropertyManager page is displayed, use a bitmap or PNG image that is the same size.

Example

See the [IPropertyManagerPageBitmap](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageBitmap.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageBitmap Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageBitmap.md)  
[IPropertyManagerPageBitmap Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageBitmap_members.md)
