# FeatureManagerSplitterPosition Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FeatureManagerSplitterPosition`

Splits the FeatureManager design tree and gets or sets the location of the split bar in the FeatureManager design tree panel.
Splits the FeatureManager design tree and gets or sets the location of the split bar in the FeatureManager design tree panel.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FeatureManagerSplitterPosition As System.Double
```

```

Dim instance As IModelDoc2
Dim value As System.Double
 
instance.FeatureManagerSplitterPosition = value
 
value = instance.FeatureManagerSplitterPosition
```

```

System.double FeatureManagerSplitterPosition {get; set;}
```

```

property System.double FeatureManagerSplitterPosition {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Percentage value between 0 and 1, which sets the location of the split bar in the FeatureManager design tree panel and the size of each split FeatureManager design tree (see **Remarks**)

Remarks

|  |  |
| --- | --- |
| **Setting this property to...** | **Results in the split panel bar..**. |
| 0 | Remaining above the FeatureManager design tree. |
| 1 | Moving below the FeatureManager design tree. |
| >0 and <1 | Setting the size of the split FeatureManager design trees within the FeatureManager design tree panel.  For example, if you specify:   - 0.5, then each FeatureManager design tree takes up 50 percent of the panel, and the split bar is located between them. - 0.8, then the bottom FeatureManager design tree takes up 80 percent of the panel, the top FeatureManager design tree takes up 20 percent of the panel, and the split bar is located between them. |

Example

[Add ActiveX Tabs to FeatureManager Design Tree (C#)](Add_ActiveX_Tabs_to_FeatureManager_Design_Tree_Example_CSharp.htm)  
[Add ActiveX Tabs to FeatureManager Design Tree (VB.NET)](Add_ActiveX_Tabs_to_FeatureManager_Design_Tree_Example_VBNET.htm)  
[Add ActiveX Tabs to FeatureManager Design Tree (VBA)](Add_ActiveX_Tabs_to_FeatureManager_Design_Tree_Example_VB.htm)  
[Split FeatureManager Design Tree and Position Splitter (C#)](Split_FeatureManager_Design_Tree_and_Position_Splitter_Example_CSharp.htm)  
[Split FeatureManager Design Tree and Position Splitter (VB.NET)](Split_FeatureManager_Design_Tree_and_Position_Splitter_Example_VBNET.htm)  
[Split FeatureManager Design Tree and Position Splitter (VBA)](Split_FeatureManager_Design_Tree_and_Position_Splitter_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
