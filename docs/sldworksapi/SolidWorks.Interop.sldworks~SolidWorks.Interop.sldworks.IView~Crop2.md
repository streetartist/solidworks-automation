# Crop2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~Crop2`

Crops this view using the selected closed sketch profile.
Crops this view using the selected closed sketch profile.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Crop2( _
   ByVal JaggedOutline As System.Boolean, _
   ByVal NoOutline As System.Boolean, _
   ByVal ShapeIntensity As System.Integer _
) As System.Integer
```

```

Dim instance As IView
Dim JaggedOutline As System.Boolean
Dim NoOutline As System.Boolean
Dim ShapeIntensity As System.Integer
Dim value As System.Integer
 
value = instance.Crop2(JaggedOutline, NoOutline, ShapeIntensity)
```

```

System.int Crop2( 
   System.bool JaggedOutline,
   System.bool NoOutline,
   System.int ShapeIntensity
)
```

```

System.int Crop2( 
   System.bool JaggedOutline,
   System.bool NoOutline,
   System.int ShapeIntensity
) 
```

#### Parameters

*JaggedOutline*
:   True to use a jagged outline, false to not; only valid if NoOutline is false

*NoOutline*
:   True to not show an outline, false to show an outline

*ShapeIntensity*
:   Shape intensity of the jagged outline; valid range is 1 (most) to 5 (least); only valid if JaggedOutline is true

#### Return Value

Crop view status as defined in [swCropViewErrors\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCropViewErrors_e.html)

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
[IView::IsCropped Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IsCropped.md)  
[IView::CropViewJaggedOutline Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~CropViewJaggedOutline.md)  
[IView::CropViewJaggedShapeIntensity Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~CropViewJaggedShapeIntensity.md)  
[IView::CropViewNoOutline Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~CropViewNoOutline.md)
