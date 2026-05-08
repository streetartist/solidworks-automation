# Edges Property (ISimpleFilletFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~Edges`

Gets or sets the edges for this simple radius fillet.
Gets or sets the edges for this simple radius fillet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Edges As System.Object
```

```

Dim instance As ISimpleFilletFeatureData2
Dim value As System.Object
 
instance.Edges = value
 
value = instance.Edges
```

```

System.object Edges {get; set;}
```

```

property System.Object^ Edges {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

[Edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.md)  
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.md)  
[ISimpleFilletFeatureData2::GetEdgeCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetEdgeCount.md)  
[ISimpleFilletFeatureData2::IGetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IGetEdges.md)  
[ISimpleFilletFeatureData2::ISetEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ISetEdges.md)
