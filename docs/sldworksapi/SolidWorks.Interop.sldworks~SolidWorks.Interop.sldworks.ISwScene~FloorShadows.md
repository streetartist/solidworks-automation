# FloorShadows Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~FloorShadows`

Gets or sets whether to show shadows cast by the model on the scene floor.
Gets or sets whether to show shadows cast by the model on the scene floor.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FloorShadows As System.Boolean
```

```

Dim instance As ISwScene
Dim value As System.Boolean
 
instance.FloorShadows = value
 
value = instance.FloorShadows
```

```

System.bool FloorShadows {get; set;}
```

```

property System.bool FloorShadows {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to show shadows cast by the model, false to not

Example

See the [ISwScene](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.md)  
[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.md)
