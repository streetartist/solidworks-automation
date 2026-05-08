# NeedEdgeFinMap Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~NeedEdgeFinMap`

Gets or sets the need edge fin map option.
Gets or sets the need edge fin map option.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property NeedEdgeFinMap As System.Boolean
```

```

Dim instance As ITessellation
Dim value As System.Boolean
 
instance.NeedEdgeFinMap = value
 
value = instance.NeedEdgeFinMap
```

```

System.bool NeedEdgeFinMap {get; set;}
```

```

property System.bool NeedEdgeFinMap {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True generates this information, false does not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.md)  
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.md)
