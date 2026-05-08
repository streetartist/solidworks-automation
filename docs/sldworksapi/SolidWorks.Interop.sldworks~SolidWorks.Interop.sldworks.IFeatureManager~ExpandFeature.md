# ExpandFeature Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ExpandFeature`

Expands the specified component in the specified FeatureManager design tree pane.
Expands the specified component in the specified FeatureManager design tree pane.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ExpandFeature( _
   ByVal Component As System.Object, _
   ByVal FeatureName As System.String, _
   ByVal WhichPane As System.Integer _
) As System.Boolean
```

```

Dim instance As IFeatureManager
Dim Component As System.Object
Dim FeatureName As System.String
Dim WhichPane As System.Integer
Dim value As System.Boolean
 
value = instance.ExpandFeature(Component, FeatureName, WhichPane)
```

```

System.bool ExpandFeature( 
   System.object Component,
   System.string FeatureName,
   System.int WhichPane
)
```

```

System.bool ExpandFeature( 
   System.Object^ Component,
   System.String^ FeatureName,
   System.int WhichPane
) 
```

#### Parameters

*Component*
:   [Component](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)

*FeatureName*
:   Name of a feature in Component

*WhichPane*
:   FeatureManager design tree pane in which to expand Component as defined in [swFeatMgrPane\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFeatMgrPane_e.html)

#### Return Value

True if the specified component is expanded in the specified FeatureManager design tree pane, false if not

Example

[Expand Component in Specified FeatureManager Design Tree Pane (C#)](Expand_Component_in_Specified_FeatureManager_Design_Tree_Pane_Example_CSharp.htm)  
[Expand Component in Specified FeatureManager Design Tree Pane (VB.NET)](Expand_Component_in_Specified_FeatureManager_Design_Tree_Pane_Example_VBNET.htm)  
[Expand Component in Specified FeatureManager Design Tree Pane (VBA)](Expand_Component_in_Specified_FeatureManager_Design_Tree_Pane_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[ITreeControlItem::Expanded Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem~Expanded.md)
