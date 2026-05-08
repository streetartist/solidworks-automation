# Scale2 Property (IModelView)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~Scale2`

Gets and sets the model view scale factor.
Gets and sets the model view scale factor.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Scale2 As System.Double
```

```

Dim instance As IModelView
Dim value As System.Double
 
instance.Scale2 = value
 
value = instance.Scale2
```

```

System.double Scale2 {get; set;}
```

```

property System.double Scale2 {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Scale factor

Remarks

If you want to zoom in by a factor of 2, then you should get the current scale using this method, multiply the return value by 2, and then pass that value back into this method, which will increase the model view scale.

Using data returned from this property along with information from [IModelView::Orientation3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~Orientation3.md) and [IModelView::Translation3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~Translation3.md) should be multiplied in this order: orientation > scale > transform.

To map your coordinates from 3D space to the screen, use [IModelView::Transform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~Transform.md).

Example

[Get Scale Factor of Each Model View (C++)](Get_Scale_of_Each_Model_View_Example_CPlusPlus_COM.htm)  
[Get Scale Factor of Each Model View (C#)](Get_Scale_of_Each_Model_View_Example_CSharp.htm)  
[Get Scale Factor of Each Model View (VB.NET)](Get_Scale_of_Each_Model_View_Example_VBNET.htm)  
[Get Scale Factor of Each Model View (VBA)](Get_Scale_of_Each_Model_View_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.md)  
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.md)  
[IModelView::GetEyePoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetEyePoint.md)  
[IModelView::GetIsoPlaneDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetIsoPlaneDistance.md)  
[IModelView::GetViewPlaneDistance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetViewPlaneDistance.md)  
[IModelView::IGetEyePoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~IGetEyePoint.md)  
[IModelView::ISetEyePoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~ISetEyePoint.md)  
[IModelView::SetEyePoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~SetEyePoint.md)
