# Object Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem~Object`

Gets the SOLIDWORKS object associated with this item in the FeatureManager design tree.
Gets the SOLIDWORKS object associated with this item in the FeatureManager design tree.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Object As System.Object
```

```

Dim instance As ITreeControlItem
Dim value As System.Object
 
value = instance.Object
```

```

System.object Object {get;}
```

```

property System.Object^ Object {
   System.Object^ get();
}
```

#### Property Value

SOLIDWORKS object associated with this item in the FeatureManager design tree (see **Remarks**)

Remarks

Currently only [features](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) and [components](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) are supported. Null is returned for sub-components of an assembly loaded hidden with a selective open.

Use [ITreeControlItem::ObjectType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem~ObjectType.md) to determine the SOLIDWORKS object type.

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
