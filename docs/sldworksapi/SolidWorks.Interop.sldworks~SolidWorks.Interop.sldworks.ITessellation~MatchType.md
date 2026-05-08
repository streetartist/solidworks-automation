# MatchType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~MatchType`

Gets or sets the type of Parasolid facet match for the tessellation.
Gets or sets the type of Parasolid facet match for the tessellation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property MatchType As System.Integer
```

```

Dim instance As ITessellation
Dim value As System.Integer
 
instance.MatchType = value
 
value = instance.MatchType
```

```

System.int MatchType {get; set;}
```

```

property System.int MatchType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Type of match as defined by [swTesselationMatchType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTesselationMatchType_e.html)

Example

[Tessellate a Body (C#)](Tessellate_a_Body_Example_CSharp.htm)  
[Tessellate a Body (VB.NET)](Tessellate_a_Body_Example_VBNET.htm)  
[Tessellate a Body (VBA)](Tessellate_a_Body_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.md)  
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.md)
