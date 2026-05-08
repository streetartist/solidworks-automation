# ObjectType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem~ObjectType`

Gets the type of SOLIDWORKS object for this item in the FeatureManager design tree.
Gets the type of SOLIDWORKS object for this item in the FeatureManager design tree.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property ObjectType As System.Integer
```

```

Dim instance As ITreeControlItem
Dim value As System.Integer
 
value = instance.ObjectType
```

```

System.int ObjectType {get;}
```

```

property System.int ObjectType {
   System.int get();
}
```

#### Property Value

Type of SOLIDWORKS object for this item in the FeatureManager design tree as defined by [swTreeControlItemType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTreeControlItemType_e.html)

Remarks

Currently only [features](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) and [components](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) are supported. Null is returned for sub-components of an assembly loaded hidden with a selective open.

Use [ITreeControlItem::Object](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem~Object.md) to get the SOLIDWORKS object associated with this item.

Example

[Traverse FeatureManager Design Tree (VBA)](Traverse_FeatureManager_Design_Tree_VB.htm)  
[Expand or Collapse FeatureManager Design Tree Nodes (VBA)](Expand_and_Collapse_FeatureManager_Design_Tree_Nodes_VB.htm)  
[Expand or Collapse FeatureManager Design Tree Nodes (VB.NET)](Expand_and_Collapse_FeatureManager_Design_Tree_Nodes_Example_VBNET.htm)  
[Expand or Collapse FeatureManager Design Tree Nodes (C#)](Expand_and_Collapse_FeatureManager_Design_Tree_Nodes_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITreeControlItem Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem.md)  
[ITreeControlItem Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem_members.md)
