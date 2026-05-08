# HighQuality Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~HighQuality`

Gets or sets whether to print a drawing in high quality.
Gets or sets whether to print a drawing in high quality.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property HighQuality As System.Boolean
```

```

Dim instance As IPageSetup
Dim value As System.Boolean
 
instance.HighQuality = value
 
value = instance.HighQuality
```

```

System.bool HighQuality {get; set;}
```

```

property System.bool HighQuality {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to print a drawing in high quality, false to not

Remarks

You can [scale draft edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~ScaleDraftEdges.md) in a printed drawing when this property is set to true.

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
