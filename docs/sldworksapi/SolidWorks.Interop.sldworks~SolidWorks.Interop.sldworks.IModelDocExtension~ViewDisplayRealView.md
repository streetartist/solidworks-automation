# ViewDisplayRealView Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ViewDisplayRealView`

Gets or sets the RealView Graphics setting.
Gets or sets the RealView Graphics setting.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ViewDisplayRealView As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim value As System.Boolean
 
instance.ViewDisplayRealView = value
 
value = instance.ViewDisplayRealView
```

```

System.bool ViewDisplayRealView {get; set;}
```

```

property System.bool ViewDisplayRealView {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if RealView Graphics is set, false if not

Remarks

When you [apply a material to a part](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SetMaterialPropertyName2.md), use RealView Graphics to display the model with realistic-looking materials. RealView Graphics is available with supported graphics cards only. See the SOLIDWORKS Help for details.

Example

[Get Appearance File Name (C#)](Get_Appearance_Filename_Example_CSharp.htm)  
[Get Appearance File Name (VB.NET)](Get_Appearance_Filename_Example_VBNET.htm)  
[Get Appearance File Name (VBA)](Get_Appearance_Filename_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IMaterialVisualPropertiesData::RealView Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMaterialVisualPropertiesData~RealView.md)
