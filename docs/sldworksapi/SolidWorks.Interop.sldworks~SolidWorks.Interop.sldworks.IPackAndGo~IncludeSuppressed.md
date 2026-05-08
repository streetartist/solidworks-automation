# IncludeSuppressed Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~IncludeSuppressed`

Gets or sets whether to included suppressed components in Pack and Go.
Gets or sets whether to included suppressed components in Pack and Go.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property IncludeSuppressed As System.Boolean
```

```

Dim instance As IPackAndGo
Dim value As System.Boolean
 
instance.IncludeSuppressed = value
 
value = instance.IncludeSuppressed
```

```

System.bool IncludeSuppressed {get; set;}
```

```

property System.bool IncludeSuppressed {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if suppressed components are added to Pack and Go, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPackAndGo Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo.md)  
[IPackAndGo Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo_members.md)
