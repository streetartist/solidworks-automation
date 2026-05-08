# Table Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin~Table`

Gets the hole table associated with this datum origin.
Gets the hole table associated with this datum origin.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Table As HoleTable
```

```

Dim instance As IDatumOrigin
Dim value As HoleTable
 
value = instance.Table
```

```

HoleTable Table {get;}
```

```

property HoleTable^ Table {
   HoleTable^ get();
}
```

#### Property Value

Pointer to the [IHoleTable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable.md) object associated with datum origin

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDatumOrigin Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin.md)  
[IDatumOrigin Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin_members.md)
