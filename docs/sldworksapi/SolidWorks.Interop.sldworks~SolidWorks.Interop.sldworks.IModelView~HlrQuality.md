# HlrQuality Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~HlrQuality`

Gets or sets the hidden-line removal quality property of this model view.
Gets or sets the hidden-line removal quality property of this model view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property HlrQuality As System.Integer
```

```

Dim instance As IModelView
Dim value As System.Integer
 
instance.HlrQuality = value
 
value = instance.HlrQuality
```

```

System.int HlrQuality {get; set;}
```

```

property System.int HlrQuality {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Type of HLR done as defined in [swHlrQuality\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swHlrQuality_e.html)

Example

[Get and Set Model View HLR Quality (VBA)](Get_and_Set_Model_View_HLR_Quality_Example_VB.htm)  
[Get and Set Model View HLR Quality (VB.NET)](Get_and_Set_Model_View_HLR_Quality_Example_VBNET.htm)  
[Get and Set Model View HLR Quality (C#)](Get_and_Set_Model_View_HLR_Quality_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.md)  
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.md)  
[IModelView::DynamicMode Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~DynamicMode.md)  
[IModelView::DisplayMode Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~DisplayMode.md)  
[IModelView::StopDynamics Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~StopDynamics.md)  
[IModelView::StartDynamics Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~StartDynamics.md)
