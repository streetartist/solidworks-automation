# ShowRuler Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator~ShowRuler`

Gets or sets whether to display a ruler when the handle moves.
Gets or sets whether to display a ruler when the handle moves.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ShowRuler As System.Boolean
```

```

Dim instance As IDragArrowManipulator
Dim value As System.Boolean
 
instance.ShowRuler = value
 
value = instance.ShowRuler
```

```

System.bool ShowRuler {get; set;}
```

```

property System.bool ShowRuler {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to display a ruler when the handle moves, false to not

Example

See [IDragArrowManipulator](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDragArrowManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator.md)  
[IDragArrowManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator_members.md)
