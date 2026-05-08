# SetStandardPictureLabel Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl~SetStandardPictureLabel`

Sets the bitmap's or PNG image's label for this control on a PropertyManager page.
Sets the bitmap's or PNG image's label for this control on a PropertyManager page.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetStandardPictureLabel( _
   ByVal Bitmap As System.Integer _
) As System.Boolean
```

```

Dim instance As IPropertyManagerPageControl
Dim Bitmap As System.Integer
Dim value As System.Boolean
 
value = instance.SetStandardPictureLabel(Bitmap)
```

```

System.bool SetStandardPictureLabel( 
   System.int Bitmap
)
```

```

System.bool SetStandardPictureLabel( 
   System.int Bitmap
) 
```

#### Parameters

*Bitmap*
:   Label type as defined in [swControlBitmapLabelType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swControlBitmapLabelType_e.html)

#### Return Value

True if successful, false if not

Remarks

You can only use this method on a PropertyManager page before the page is displayed, while it is displayed, or when it is closed.

Example

[Cut Body in Half Using Macro Feature (VBA)](Cut_Body_in_Half_using_Macro_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageControl Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl.md)  
[IPropertyManagerPageControl Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl_members.md)
