# DepthReference Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBrokenOutSectionFeatureData~DepthReference`

Gets or sets the geometry reference that defines the depth of exposure of inner details of the model in the broken-out section feature.
Gets or sets the geometry reference that defines the depth of exposure of inner details of the model in the broken-out section feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DepthReference As Entity
```

```

Dim instance As IBrokenOutSectionFeatureData
Dim value As Entity
 
instance.DepthReference = value
 
value = instance.DepthReference
```

```

Entity DepthReference {get; set;}
```

```

property Entity^ DepthReference {
   Entity^ get();
   void set (    Entity^ value);
}
```

#### Property Value

[IEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.md) (see **Remarks**)

Remarks

Before setting this property, you must set [IBrokenOutSectionFeatureData::EditSketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBrokenOutSectionFeatureData~EditSketch.md) to false.

To set the depth reference you can either:

- Set this property to an [IEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.md) object.

    -or-

- Set this property to null and select the depth geometry in the drawing view.

Example

[Get Broken-Out Section Feature Data (VBA)](Get_Broken_Out_Section_Feature_Data_Example_VB.htm)  
[Get Broken-Out Section Feature Data (VB.NET)](Get_Broken_Out_Section_Feature_Data_Example_VBNET.htm)  
[Get Broken-Out Section Feature Data (C#)](Get_Broken_Out_Section_Feature_Data_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBrokenOutSectionFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBrokenOutSectionFeatureData.md)  
[IBrokenOutSectionFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBrokenOutSectionFeatureData_members.md)  
[IBrokenOutSectionFeatureData::Depth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBrokenOutSectionFeatureData~Depth.md)
