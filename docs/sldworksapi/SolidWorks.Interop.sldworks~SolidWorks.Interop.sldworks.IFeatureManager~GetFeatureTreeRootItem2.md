# GetFeatureTreeRootItem2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~GetFeatureTreeRootItem2`

Gets the root item of the FeatureManager design tree in the specified pane.
Gets the root item of the FeatureManager design tree in the specified pane.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFeatureTreeRootItem2( _
   ByVal WhichPane As System.Integer _
) As TreeControlItem
```

```

Dim instance As IFeatureManager
Dim WhichPane As System.Integer
Dim value As TreeControlItem
 
value = instance.GetFeatureTreeRootItem2(WhichPane)
```

```

TreeControlItem GetFeatureTreeRootItem2( 
   System.int WhichPane
)
```

```

TreeControlItem^ GetFeatureTreeRootItem2( 
   System.int WhichPane
) 
```

#### Parameters

*WhichPane*
:   FeatureManager design tree pane as defined in [swFeatMgrPane\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatMgrPane_e.html)

#### Return Value

[ITreeControlItem](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem.md)

Example

[Expand or Collapse FeatureManager Design Tree Nodes (VBA)](Expand_and_Collapse_FeatureManager_Design_Tree_Nodes_VB.htm)  
[Expand or Collapse FeatureManager Design Tree Nodes (VB.NET)](Expand_and_Collapse_FeatureManager_Design_Tree_Nodes_Example_VBNET.htm)  
[Expand or Collapse FeatureManager Design Tree Nodes (C#)](Expand_and_Collapse_FeatureManager_Design_Tree_Nodes_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)
