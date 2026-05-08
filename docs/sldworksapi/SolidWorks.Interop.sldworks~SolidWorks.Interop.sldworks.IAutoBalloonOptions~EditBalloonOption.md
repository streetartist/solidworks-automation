# EditBalloonOption Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions~EditBalloonOption`

Gets and sets edit balloon options.
Gets and sets edit balloon options.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property EditBalloonOption As System.Integer
```

```

Dim instance As IAutoBalloonOptions
Dim value As System.Integer
 
instance.EditBalloonOption = value
 
value = instance.EditBalloonOption
```

```

System.int EditBalloonOption {get; set;}
```

```

property System.int EditBalloonOption {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Edit balloon option as specified in [swEditBalloonOption\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swEditBalloonOption_e.html); valid only if [IAutoBalloonOptions::EditBalloons](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions~EditBalloons.md) is true

Example

See [IAutoBalloonOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAutoBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions.md)  
[IAutoBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions_members.md)
