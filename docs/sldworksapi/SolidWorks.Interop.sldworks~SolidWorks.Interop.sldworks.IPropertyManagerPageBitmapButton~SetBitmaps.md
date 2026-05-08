# SetBitmaps Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageBitmapButton~SetBitmaps`

Sets the images for this button.
Sets the images for this button.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetBitmaps( _
   ByVal ModuleHandle As System.Integer, _
   ByVal BitmapUp As System.Integer, _
   ByVal BitmapDown As System.Integer, _
   ByVal BitmapDisabled As System.Integer _
) As System.Boolean
```

```

Dim instance As IPropertyManagerPageBitmapButton
Dim ModuleHandle As System.Integer
Dim BitmapUp As System.Integer
Dim BitmapDown As System.Integer
Dim BitmapDisabled As System.Integer
Dim value As System.Boolean
 
value = instance.SetBitmaps(ModuleHandle, BitmapUp, BitmapDown, BitmapDisabled)
```

```

System.bool SetBitmaps( 
   System.int ModuleHandle,
   System.int BitmapUp,
   System.int BitmapDown,
   System.int BitmapDisabled
)
```

```

System.bool SetBitmaps( 
   System.int ModuleHandle,
   System.int BitmapUp,
   System.int BitmapDown,
   System.int BitmapDisabled
) 
```

#### Parameters

*ModuleHandle*
:   Module handle of the application instance that contains the image resource

*BitmapUp*
:   Resource ID of the not-clicked state image resource

*BitmapDown*
:   Resource ID of the clicked state image resource

*BitmapDisabled*
:   Resource ID of the disabled state image resource

#### Return Value

True if successful, false if not

Remarks

If your application must be x64 compatible, then use [IPropertyManagerpageBitmapButton::SetBitmapsx64](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageBitmapButton~SetBitmapsx64.md).

The ModuleHandle argument for this method is the handle to the instance (HINSTANCE) of the user DLL, and the resource IDs for the not-clicked, clicked, and disabled states are the image resource integers. The SOLIDWORKS application loads the images from the user DLL and uses them on this bitmap button control.

You must call this method after calling either of the following methods to create the button control:

- [IPropertyManagerPage2::AddControl](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~AddControl.md) or [IPropertyManagerPage2::IAddControl](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~IAddControl.md)
- [IPropertyManagerPageGroup::AddControl](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageGroup~AddControl.md) or [IPropertyManagerPageGroup::IAddControl](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageGroup~IAddControl.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageBitmapButton Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageBitmapButton.md)  
[IPropertyManagerPageBitmapButton Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageBitmapButton_members.md)
