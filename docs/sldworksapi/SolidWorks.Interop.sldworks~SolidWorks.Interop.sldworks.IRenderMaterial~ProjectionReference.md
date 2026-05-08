# ProjectionReference Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~ProjectionReference`

Gets or sets the projection direction for mapping the appearance.
Gets or sets the projection direction for mapping the appearance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ProjectionReference As System.Integer
```

```

Dim instance As IRenderMaterial
Dim value As System.Integer
 
instance.ProjectionReference = value
 
value = instance.ProjectionReference
```

```

System.int ProjectionReference {get; set;}
```

```

property System.int ProjectionReference {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

- 0 = XY

1 = ZX

2 = YZ

3 = Current View

4 = Selected Reference

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)
