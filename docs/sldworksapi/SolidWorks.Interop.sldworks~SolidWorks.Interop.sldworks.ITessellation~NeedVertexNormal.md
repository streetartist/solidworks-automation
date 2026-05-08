# NeedVertexNormal Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~NeedVertexNormal`

Gets or sets the need vertex normal option.
Gets or sets the need vertex normal option.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property NeedVertexNormal As System.Boolean
```

```

Dim instance As ITessellation
Dim value As System.Boolean
 
instance.NeedVertexNormal = value
 
value = instance.NeedVertexNormal
```

```

System.bool NeedVertexNormal {get; set;}
```

```

property System.bool NeedVertexNormal {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True generates this information, false does not

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
