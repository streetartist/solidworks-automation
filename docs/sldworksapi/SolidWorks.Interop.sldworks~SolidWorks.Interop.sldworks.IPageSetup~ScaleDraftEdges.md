# ScaleDraftEdges Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~ScaleDraftEdges`

Gets or sets whether to scale draft edges when printing a drawing in high quality.
Gets or sets whether to scale draft edges when printing a drawing in high quality.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ScaleDraftEdges As System.Boolean
```

```

Dim instance As IPageSetup
Dim value As System.Boolean
 
instance.ScaleDraftEdges = value
 
value = instance.ScaleDraftEdges
```

```

System.bool ScaleDraftEdges {get; set;}
```

```

property System.bool ScaleDraftEdges {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to scale draft edges when printing a drawing in high quality, false to not

Remarks

This property is only valid when [IPageSetup::HighQuality](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~HighQuality.md) is set to true.

Example

[Get Whether Draft Edges Scaled in Printed Drawing (C#)](Get_Whether_Draft_Edges_Scaled_in_Printed_Drawing_Example_CSharp.htm)  
[Get Whether Draft Edges Scaled in Printed Drawing (VB.NET)](Get_Whether_Draft_Edges_Scaled_in_Printed_Drawing_Example_VBNET.htm)  
[Get Whether Draft Edges Scaled in Printed Drawing (VBA)](Get_Whether_Draft_Edges_Scaled_in_Printed_Drawing_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPageSetup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup.md)  
[IPageSetup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup_members.md)
