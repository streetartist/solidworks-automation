# SplitTools Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~SplitTools`

Gets or sets the tools used to make the split.
Gets or sets the tools used to make the split.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SplitTools As System.Object
```

```

Dim instance As ISplitLineFeatureData
Dim value As System.Object
 
instance.SplitTools = value
 
value = instance.SplitTools
```

```

System.object SplitTools {get; set;}
```

```

property System.Object^ SplitTools {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of tools used to make the split

Remarks

[Reference planes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md), [planar model faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md), and [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) are valid tools for a split.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISplitLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData.md)  
[ISplitLineFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData_members.md)  
[ISplitLineFeatureData::GetSplitToolsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~GetSplitToolsCount.md)  
[ISplitLineFeatureData::IGetSplitTools Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~IGetSplitTools.md)  
[ISplitLineFeatureData::ISetSplitTools Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~ISetSplitTools.md)
