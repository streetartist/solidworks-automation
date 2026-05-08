# PropagateVisualProperties Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData~PropagateVisualProperties`

Gets or sets whether to propagate visual properties (e.g., colors, textures, etc.) to all variable pattern instances.
Gets or sets whether to propagate visual properties (e.g., colors, textures, etc.) to all variable pattern instances.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PropagateVisualProperties As System.Boolean
```

```

Dim instance As IDimPatternFeatureData
Dim value As System.Boolean
 
instance.PropagateVisualProperties = value
 
value = instance.PropagateVisualProperties
```

```

System.bool PropagateVisualProperties {get; set;}
```

```

property System.bool PropagateVisualProperties {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to propagate visual properties, false to not

Example

[Delete Instances and Dimensions in Variable Pattern Feature (C#)](Delete_Instances_and_Dimensions_in_Variable_Pattern_Feature_Example_CSharp.htm)  
[Delete Instances and Dimensions in Variable Pattern Feature (VB.NET)](Delete_Instances_and_Dimensions_in_Variable_Pattern_Feature_Example_VBNET.htm)  
[Delete Instances and Dimensions in Variable Pattern Feature (VBA)](Delete_Instances_and_Dimensions_in_Variable_Pattern_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDimPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData.md)  
[IDimPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData_members.md)
