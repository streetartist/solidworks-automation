# CropViewNoOutline Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~CropViewNoOutline`

Gets or sets whether to show an outline in this cropped drawing view.
Gets or sets whether to show an outline in this cropped drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CropViewNoOutline As System.Boolean
```

```

Dim instance As IView
Dim value As System.Boolean
 
instance.CropViewNoOutline = value
 
value = instance.CropViewNoOutline
```

```

System.bool CropViewNoOutline {get; set;}
```

```

property System.bool CropViewNoOutline {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to not show an outline, false to show an outline

Remarks

Call [IView::IsCropped](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IsCropped.md) to find out if this drawing view is cropped.

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
[IView::CropViewJaggedOutline Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~CropViewJaggedOutline.md)  
[IView::CropViewJaggedShapeIntensity Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~CropViewJaggedShapeIntensity.md)
