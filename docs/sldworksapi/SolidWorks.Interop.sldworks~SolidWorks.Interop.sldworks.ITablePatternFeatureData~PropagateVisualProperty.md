# PropagateVisualProperty Property (ITablePatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~PropagateVisualProperty`

Gets or sets whether to propagate visual properties (e.g., colors, textures, etc.) in the table-driven pattern feature.
Gets or sets whether to propagate visual properties (e.g., colors, textures, etc.) in the table-driven pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PropagateVisualProperty As System.Boolean
```

```

Dim instance As ITablePatternFeatureData
Dim value As System.Boolean
 
instance.PropagateVisualProperty = value
 
value = instance.PropagateVisualProperty
```

```

System.bool PropagateVisualProperty {get; set;}
```

```

property System.bool PropagateVisualProperty {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to propagate visual properties, false to not

Example

See the [ITablePatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITablePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData.md)  
[ITablePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData_members.md)
