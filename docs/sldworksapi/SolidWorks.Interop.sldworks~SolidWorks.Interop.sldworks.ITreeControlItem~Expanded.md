# Expanded Property (ITreeControlItem)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem~Expanded`

Gets or sets whether to expand this item in the FeatureManager design tree.
Gets or sets whether to expand this item in the FeatureManager design tree.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Expanded As System.Boolean
```

```

Dim instance As ITreeControlItem
Dim value As System.Boolean
 
instance.Expanded = value
 
value = instance.Expanded
```

```

System.bool Expanded {get; set;}
```

```

property System.bool Expanded {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to expand, false to collapse

Example

[Expand or Collapse FeatureManager Design Tree Nodes (VBA)](Expand_and_Collapse_FeatureManager_Design_Tree_Nodes_VB.htm)  
[Expand or Collapse FeatureManager Design Tree Nodes (VB.NET)](Expand_and_Collapse_FeatureManager_Design_Tree_Nodes_Example_VBNET.htm)  
[Expand or Collapse FeatureManager Design Tree Nodes (C#)](Expand_and_Collapse_FeatureManager_Design_Tree_Nodes_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITreeControlItem Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem.md)  
[ITreeControlItem Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem_members.md)  
[IFeatureManager::ExpandFeature Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ExpandFeature.md)
