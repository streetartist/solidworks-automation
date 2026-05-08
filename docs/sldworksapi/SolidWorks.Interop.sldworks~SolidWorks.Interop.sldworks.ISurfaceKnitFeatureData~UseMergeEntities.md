# UseMergeEntities Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData~UseMergeEntities`

Get or sets whether to merge edges and faces by removing redundant vertices and edges when creating the Surface-Knit feature.
Get or sets whether to merge edges and faces by removing redundant vertices and edges when creating the Surface-Knit feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UseMergeEntities As System.Boolean
```

```

Dim instance As ISurfaceKnitFeatureData
Dim value As System.Boolean
 
instance.UseMergeEntities = value
 
value = instance.UseMergeEntities
```

```

System.bool UseMergeEntities {get; set;}
```

```

property System.bool UseMergeEntities {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to merge edges and faces, false to not

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Example

[Create Knit Surface Feature (VB.NET)](Create_Surface_Knit_Feature_Example_VBNET.htm)  
[Create Knit Surface Feature (VBA)](Create_Surface_Knit_Feature_Example_VB6.htm)  
[Create Knit Surface Feature (C#)](Create_Surface_Knit_Feature_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurfaceKnitFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData.md)  
[ISurfaceKnitFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData_members.md)
