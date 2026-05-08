# CropViewJaggedOutline Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~CropViewJaggedOutline`

Gets or sets whether to use a jagged outline in this cropped drawing view.
Gets or sets whether to use a jagged outline in this cropped drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CropViewJaggedOutline As System.Boolean
```

```

Dim instance As IView
Dim value As System.Boolean
 
instance.CropViewJaggedOutline = value
 
value = instance.CropViewJaggedOutline
```

```

System.bool CropViewJaggedOutline {get; set;}
```

```

property System.bool CropViewJaggedOutline {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to use a jagged outline, false to not (see **Remarks**)

Remarks

Call [IView::IsCropped](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IsCropped.md) to find out if this drawing view is cropped.

IView::CropViewJaggedOutline is only available when [IView::CropViewNoOutline](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~CropViewNoOutline.md) is false.

To set the intensity of the jagged outline, call [IView::CropViewJaggedShapeIntensity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~CropViewJaggedShapeIntensity.md).

Example

[Crop Drawing View Using Jagged Outline (C#)](Crop_Drawing_View_Using_Jagged_Outline_Example_CSharp.htm)  
[Crop Drawing View Using Jagged Outline (VB.NET)](Crop_Drawing_View_Using_Jagged_Outline_Example_VBNET.htm)  
[Crop Drawing View Using Jagged Outline (VBA)](Crop_Drawing_View_Using_Jagged_Outline_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::Crop2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~Crop2.md)
