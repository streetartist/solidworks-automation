# CropViewJaggedShapeIntensity Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~CropViewJaggedShapeIntensity`

Gets or sets the shape intensity of the jagged outline in this cropped drawing view.
Gets or sets the shape intensity of the jagged outline in this cropped drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CropViewJaggedShapeIntensity As System.Integer
```

```

Dim instance As IView
Dim value As System.Integer
 
instance.CropViewJaggedShapeIntensity = value
 
value = instance.CropViewJaggedShapeIntensity
```

```

System.int CropViewJaggedShapeIntensity {get; set;}
```

```

property System.int CropViewJaggedShapeIntensity {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Shape intensity of the jagged outline; valid range is 1 (most) to 5 (least) (see **Remarks**)

Remarks

Call [IView::IsCropped](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IsCropped.md) to find out if this drawing view is cropped.

IView::CropViewJaggedShapeIntensity is only available when [IView::CropViewJaggedOutline](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~CropViewJaggedOutline.md) is true and [IView::CropViewNoOutline](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~CropViewNoOutline.md) is false.

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
