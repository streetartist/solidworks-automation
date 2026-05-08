# IncludeDrawings Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~IncludeDrawings`

Gets or sets whether to add the model's drawing documents to Pack and Go.
Gets or sets whether to add the model's drawing documents to Pack and Go.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property IncludeDrawings As System.Boolean
```

```

Dim instance As IPackAndGo
Dim value As System.Boolean
 
instance.IncludeDrawings = value
 
value = instance.IncludeDrawings
```

```

System.bool IncludeDrawings {get; set;}
```

```

property System.bool IncludeDrawings {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if the model's drawings documents are added to Pack and Go, false if not

Example

[Pack and Go an Assembly (C#)](Pack_and_Go_an_Assembly_Example_CSharp.htm)  
[Pack and Go an Assembly (VB.NET)](Pack_and_Go_an_Assembly_Example_VBNET.htm)  
[Pack and Go an Assembly (VBA)](Pack_and_Go_an_Assembly_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPackAndGo Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo.md)  
[IPackAndGo Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo_members.md)
