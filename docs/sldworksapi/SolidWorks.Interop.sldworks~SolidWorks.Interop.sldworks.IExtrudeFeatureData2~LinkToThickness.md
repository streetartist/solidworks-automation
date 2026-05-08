# LinkToThickness Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~LinkToThickness`

Gets or sets whether to link the depth of an extruded boss to the thickness of the base feature.
Gets or sets whether to link the depth of an extruded boss to the thickness of the base feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property LinkToThickness As System.Boolean
```

```

Dim instance As IExtrudeFeatureData2
Dim value As System.Boolean
 
instance.LinkToThickness = value
 
value = instance.LinkToThickness
```

```

System.bool LinkToThickness {get; set;}
```

```

property System.bool LinkToThickness {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to link the depth of an extruded boss to the thickness of the base feature, false to not

Remarks

This property applies to [sheet metal parts](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.md) only.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.md)  
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.md)
