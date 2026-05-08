# LinkToFile Property (IRenderMaterial)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~LinkToFile`

Gets or sets whether to link instances of the appearance to an appearance file (.p2m).
Gets or sets whether to link instances of the appearance to an appearance file (.p2m).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property LinkToFile As System.Boolean
```

```

Dim instance As IRenderMaterial
Dim value As System.Boolean
 
instance.LinkToFile = value
 
value = instance.LinkToFile
```

```

System.bool LinkToFile {get; set;}
```

```

property System.bool LinkToFile {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to link instances of the appearance to an appearance file (.p2m), false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)
