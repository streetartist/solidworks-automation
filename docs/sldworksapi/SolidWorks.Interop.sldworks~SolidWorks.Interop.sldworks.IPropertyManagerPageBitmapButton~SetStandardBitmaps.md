# SetStandardBitmaps Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageBitmapButton~SetStandardBitmaps`

Sets the standard images for this button.
Sets the standard images for this button.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetStandardBitmaps( _
   ByVal Bitmap As System.Integer _
) As System.Boolean
```

```

Dim instance As IPropertyManagerPageBitmapButton
Dim Bitmap As System.Integer
Dim value As System.Boolean
 
value = instance.SetStandardBitmaps(Bitmap)
```

```

System.bool SetStandardBitmaps( 
   System.int Bitmap
)
```

```

System.bool SetStandardBitmaps( 
   System.int Bitmap
) 
```

#### Parameters

*Bitmap*
:   Standard images as defined by [swPropertyManagerPageBitmapButtons\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropertyManagerPageBitmapButtons_e.html)

#### Return Value

True if standard images are set, false if not

Remarks

This is the quickest and easiest way to set images on a bitmap button control after the control is created. The not-clicked, clicked, and disabled states for the control are automatically set by the SOLIDWORKS application.

You must call this method after calling either of the following methods to create the bitmap button control:

- [IPropertyManagerPage2::AddControl](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~AddControl.md) or [IPropertyManagerPage2::IAddControl](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~IAddControl.md)
- [IPropertyManagerPageGroup::AddControl](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageGroup~AddControl.md) or [IPropertyManagerPageGroup::IAddControl](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageGroup~IAddControl.md)

Example

See the [IPropertyManagerPageBitmapButton](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageBitmapButton.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageBitmapButton Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageBitmapButton.md)  
[IPropertyManagerPageBitmapButton Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageBitmapButton_members.md)
