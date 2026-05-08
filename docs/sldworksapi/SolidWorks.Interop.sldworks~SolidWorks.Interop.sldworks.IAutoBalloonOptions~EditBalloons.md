# EditBalloons Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions~EditBalloons`

Gets and sets whether to use edit balloon options when creating the auto balloon.
Gets and sets whether to use edit balloon options when creating the auto balloon.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property EditBalloons As System.Boolean
```

```

Dim instance As IAutoBalloonOptions
Dim value As System.Boolean
 
instance.EditBalloons = value
 
value = instance.EditBalloons
```

```

System.bool EditBalloons {get; set;}
```

```

property System.bool EditBalloons {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to use edit balloon option as specified in [IAutoBalloonOption::EditBalloonOption](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions~EditBalloonOption.md), false to not

Example

See [IAutoBalloonOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAutoBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions.md)  
[IAutoBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions_members.md)
