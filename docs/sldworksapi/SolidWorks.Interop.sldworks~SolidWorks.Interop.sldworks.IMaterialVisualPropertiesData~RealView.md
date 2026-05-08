# RealView Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMaterialVisualPropertiesData~RealView`

Gets or sets whether textures are displayed in RealView or Standard graphics.
Gets or sets whether textures are displayed in RealView or Standard graphics.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property RealView As System.Boolean
```

```

Dim instance As IMaterialVisualPropertiesData
Dim value As System.Boolean
 
instance.RealView = value
 
value = instance.RealView
```

```

System.bool RealView {get; set;}
```

```

property System.bool RealView {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if textures are RealView graphics, false if Standard graphics

Remarks

[IMaterialVisualPropertiesData::AdvancedGraphics](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMaterialVisualPropertiesData~AdvancedGraphics.md) must be True to set this property.

Example

See [IMaterialVisualPropertiesData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMaterialVisualPropertiesData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMaterialVisualPropertiesData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMaterialVisualPropertiesData.md)  
[IMaterialVisualPropertiesData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMaterialVisualPropertiesData_members.md)  
[IModelDocExtension::ViewDisplayRealView Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ViewDisplayRealView.md)
