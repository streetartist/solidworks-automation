# FirstItem Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions~FirstItem`

Gets and sets the first balloon item.
Gets and sets the first balloon item.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FirstItem As System.Object
```

```

Dim instance As IAutoBalloonOptions
Dim value As System.Object
 
instance.FirstItem = value
 
value = instance.FirstItem
```

```

System.object FirstItem {get; set;}
```

```

property System.Object^ FirstItem {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

[IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)

Remarks

See the SOLIDWORKS Help for additional details about autoballoons.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAutoBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions.md)  
[IAutoBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions_members.md)
