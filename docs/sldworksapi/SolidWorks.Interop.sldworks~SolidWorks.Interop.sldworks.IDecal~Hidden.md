# Hidden Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~Hidden`

Gets or sets whether the decal hidden.
Gets or sets whether the decal hidden.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Hidden As System.Boolean
```

```

Dim instance As IDecal
Dim value As System.Boolean
 
instance.Hidden = value
 
value = instance.Hidden
```

```

System.bool Hidden {get; set;}
```

```

property System.bool Hidden {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if the decal is hidden, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDecal Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal.md)  
[IDecal Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal_members.md)
